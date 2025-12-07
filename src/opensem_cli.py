import shutil
import argparse
import sys
import os
import importlib
import yaml

WORKSPACE_ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT_FILE = os.path.join(WORKSPACE_ROOT, '../.openssme_project')

def run_forge(project):
    if project is None:
        project = get_current_project()
        if not project:
            print("No project specified and no current project set.")
            return

    print(f"Running Data Forge for project: {project}")
    
    # Load config
    config_path = os.path.join(WORKSPACE_ROOT, '../configs', project, 'data_config.yaml')
    if not os.path.exists(config_path):
        print(f"Config file not found: {config_path}. Using defaults.")
        config = {}
    else:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f) or {}

    # Set default paths if not present
    config.setdefault('raw_data_dir', os.path.join(WORKSPACE_ROOT, '../data', project, 'raw'))
    config.setdefault('processed_data_dir', os.path.join(WORKSPACE_ROOT, '../data', project, 'processed'))
    
    # Determine Forge Class
    forge_class_path = config.get('forge_class', 'opensem.forge.TextForge')
    module_name, class_name = forge_class_path.rsplit('.', 1)
    
    try:
        module = importlib.import_module(module_name)
        ForgeClass = getattr(module, class_name)
    except (ImportError, AttributeError) as e:
        print(f"Error loading Forge class '{forge_class_path}': {e}")
        return

    # Instantiate and run
    try:
        forge = ForgeClass(config)
        forge.run()
    except Exception as e:
        print(f"Data Forge failed: {e}")

def delete_project(name):
    # Confirm deletion
    confirm = input(f"Are you sure you want to delete SEM project '{name}' and all its data? [y/N]: ").strip().lower()
    if confirm != 'y':
        print("Deletion cancelled.")
        return
    
    removed_any = False
    for base in ['data', 'models', 'configs']:
        path = os.path.join(WORKSPACE_ROOT, '../', base, name)
        if os.path.exists(path):
            shutil.rmtree(path)
            print(f"Deleted {path}")
            removed_any = True
            
    # Remove current project if matches
    current = get_current_project()
    if current == name:
        if os.path.exists(PROJECT_FILE):
            os.remove(PROJECT_FILE)
        print(f"Current project '{name}' removed from context.")
        
    if not removed_any:
        print(f"No directories found for project '{name}'.")
import shutil
import argparse
import sys
import os

WORKSPACE_ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT_FILE = os.path.join(WORKSPACE_ROOT, '../.openssme_project')

# Current project helpers
def get_current_project():
    if os.path.exists(PROJECT_FILE):
        with open(PROJECT_FILE, 'r') as f:
            return f.read().strip()
    return None

def set_current_project(name):
    with open(PROJECT_FILE, 'w') as f:
        f.write(name)
    print(f"Current project set to '{name}'.")

def add_data(project, files):
    if project is None:
        project = get_current_project()
        if not project:
            print("No project specified and no current project set. Use 'set-project <name>' or specify a project.")
            return
    raw_dir = os.path.join(WORKSPACE_ROOT, '../data', project, 'raw')
    if not os.path.exists(raw_dir):
        print(f"Project '{project}' does not exist or raw folder missing.")
        return
    for f in files:
        if not os.path.exists(f):
            print(f"File or folder not found: {f}")
            continue
        if os.path.isdir(f):
            # Add all files in the folder (non-recursive)
            for item in os.listdir(f):
                item_path = os.path.join(f, item)
                if os.path.isfile(item_path):
                    dest = os.path.join(raw_dir, os.path.basename(item_path))
                    shutil.copy2(item_path, dest)
                    print(f"Copied {item_path} to {raw_dir}")
        else:
            dest = os.path.join(raw_dir, os.path.basename(f))
            shutil.copy2(f, dest)
            print(f"Copied {f} to {raw_dir}")

def list_projects():
    data_dir = os.path.join(WORKSPACE_ROOT, '../data')
    if not os.path.exists(data_dir):
        print("No data directory found.")
        return
    projects = [d for d in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, d))]
    print("SEM Projects:")
    for p in projects:
        print(f"- {p}")

def status(project):
    print(f"Status for SEM project: {project}")
    # Check for existence of key directories/files
    base_path = os.path.join(WORKSPACE_ROOT, '../data', project)
    if not os.path.exists(base_path):
        print("  Project not found.")
        return
    for sub in ['raw', 'processed', 'golden']:
        sub_path = os.path.join(base_path, sub)
        print(f"  {sub}: {'Exists' if os.path.exists(sub_path) else 'Missing'}")
    # Models
    model_path = os.path.join(WORKSPACE_ROOT, '../models', project)
    print(f"  models: {'Exists' if os.path.exists(model_path) else 'Missing'}")
    # Configs
    config_path = os.path.join(WORKSPACE_ROOT, '../configs', project)
    print(f"  configs: {'Exists' if os.path.exists(config_path) else 'Missing'}")

def init_workspace():
    # Create base directories if not exist
    for d in ['data', 'models', 'configs', 'scripts', 'src']:
        path = os.path.join(WORKSPACE_ROOT, f'../{d}')
        os.makedirs(path, exist_ok=True)

    # Create conda environment if it does not exist
    env_name = "openssme"
    # Check if conda is available
    conda_check = os.system("conda --version > /dev/null 2>&1")
    if conda_check != 0:
        print("Conda is not installed or not in PATH. Please install Miniconda or Anaconda.")
        return

    # Check if environment exists
    envs = os.popen("conda env list").read()
    if env_name not in envs:
        print(f"Creating conda environment '{env_name}'...")
        req_path = os.path.join(WORKSPACE_ROOT, '../requirements.txt')
        # Create environment and install requirements
        os.system(f"conda create -y -n {env_name} python=3.10")
        os.system(f"conda run -n {env_name} pip install -r {req_path}")
        print(f"Conda environment '{env_name}' created and requirements installed.")
    else:
        print(f"Conda environment '{env_name}' already exists.")

    print("Initialized OpenSSME workspace.")

def new_project(name):
    # Create SEM project subdirectories
    for d in [f'data/{name}/raw', f'data/{name}/processed', f'data/{name}/golden', f'models/{name}/adapters', f'configs/{name}']:
        path = os.path.join(WORKSPACE_ROOT, '../', d)
        os.makedirs(path, exist_ok=True)
    # Create empty config files
    for f in ['train_config.yaml', 'eval_config.yaml']:
        config_file = os.path.join(WORKSPACE_ROOT, '../configs', name, f)
        if not os.path.exists(config_file):
            with open(config_file, 'w') as cf:
                cf.write(f'# {f} for {name}\n')
    
    # Create data_config.yaml with default strategy
    data_config_file = os.path.join(WORKSPACE_ROOT, '../configs', name, 'data_config.yaml')
    if not os.path.exists(data_config_file):
        with open(data_config_file, 'w') as cf:
            cf.write(f"""# Data Forge Configuration for {name}
forge_class: "opensem.forge.TextForge"
params:
  teacher_model: "gpt-4o-mini"
""")

    print(f"Created new SEM project: {name}")
    set_current_project(name)

def main():
    parser = argparse.ArgumentParser(description='openssme')
    subparsers = parser.add_subparsers(dest='command')

    # init
    subparsers.add_parser('init', help='Initialize OpenSSME workspace')
    # new
    new_parser = subparsers.add_parser('new', help='Create a new SEM project')
    new_parser.add_argument('name', help='SEM project name')
    # list-projects
    subparsers.add_parser('list-projects', help='List all SEM projects')
    # status
    status_parser = subparsers.add_parser('status', help='Show status for a SEM project')
    status_parser.add_argument('project', help='SEM project name')
    # add-data
    add_data_parser = subparsers.add_parser('add-data', help='Add data files to SEM project raw folder')
    add_data_parser.add_argument('files', nargs='+', help='Files or folders to add')
    add_data_parser.add_argument('--project', help='SEM project name (optional, defaults to current project)', default=None)
    # run-forge
    run_forge_parser = subparsers.add_parser('run-forge', help='Run the Data Forge pipeline')
    run_forge_parser.add_argument('--project', help='SEM project name (optional, defaults to current project)', default=None)
    # set-project
    set_project_parser = subparsers.add_parser('set-project', help='Set the current SEM project')
    set_project_parser.add_argument('name', help='SEM project name')
    # delete
    delete_parser = subparsers.add_parser('delete', help='Delete a SEM project and all its data')
    delete_parser.add_argument('name', help='SEM project name')

    args = parser.parse_args()
    if args.command == 'init':
        init_workspace()
    elif args.command == 'new':
        new_project(args.name)
    elif args.command == 'list-projects':
        list_projects()
    elif args.command == 'status':
        status(args.project)
    elif args.command == 'add-data':
        add_data(args.project, args.files)
    elif args.command == 'run-forge':
        run_forge(args.project)
    elif args.command == 'set-project':
        set_current_project(args.name)
    elif args.command == 'delete':
        delete_project(args.name)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()

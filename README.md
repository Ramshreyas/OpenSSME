# OpenSSME

OpenSSME is a light-weight framework for creating Small Expert Models. It provides simple commands to initialize workspaces, create projects, add data, and manage configurations.

## Features
- Initialize SEM workspace
- Create new SEM projects
- Add data files to projects
- Manage project configurations and models
- Delete projects safely

## Getting Started

### Prerequisites
- Python 3.10+
- Conda (Miniconda or Anaconda)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Ramshreyas/OpenSSME.git
   cd OpenSSME
   ```

2. Initialize the workspace and environment:
   ```bash
   python opensem.py init
   ```
   This command will create the necessary folder structure and a Conda environment named `opensem` with all dependencies installed.

3. Activate the environment:
   ```bash
   conda activate opensem
   ```

### Usage
All commands are run from the project root using the CLI entry point `opensem.py`:

#### 1. Initialize the workspace
(If you haven't already done so in the installation step)
```bash
python opensem.py init
```

#### 2. Create a new SEM project
```bash
python opensem.py new <project_name>
```
Example:
```bash
python opensem.py new testsem
```

#### 3. Add data to your project
```bash
python opensem.py add-data <file_or_folder>
```
Example:
```bash
python opensem.py add-data war-and-peace.pdf
```

#### 4. Run Data Forge
Process raw data into training datasets using the configured strategy.
```bash
python opensem.py run-forge --project <project_name>
```

#### 5. List all projects
```bash
python opensem.py list-projects
```

#### 6. Delete a project
```bash
python opensem.py delete <project_name>
```

## Data Forge Strategies
OpenSEM uses a flexible "Strategy Pattern" for data processing. You can configure which strategy to use in `configs/<project>/data_config.yaml`.

**Default Strategy: TextForge**
- Supports `.txt`, `.md`, and `.pdf` files.
- Extracts text and prepares it for synthesis.

To create a custom strategy, extend `opensem.forge.BaseForge` and update your config file.

## Tutorials
Check out the `notebooks/` directory for interactive tutorials:
- `notebooks/data_forge_tutorial.ipynb`: Learn how to use and extend the Data Forge module.

## Project Structure
```
OpenSEM/
├── configs/
├── data/
├── models/
├── notebooks/
├── src/
│   └── opensem/
│       └── forge/
├── opensem.py
├── requirements.txt
```

## Contributing
Pull requests and issues are welcome!

## License
MIT

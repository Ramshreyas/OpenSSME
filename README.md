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
- Python 3.7+
- (Optional) Create a virtual environment:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

### Usage
All commands are run from the project root using the CLI entry point `opensem.py`:

#### 1. Initialize the workspace
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

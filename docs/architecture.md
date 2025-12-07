# Architecture

OpenSSME is designed to be modular. Understanding the project structure and the underlying design patterns will help you get the most out of the framework.

## Project Structure

When you initialize an OpenSSME workspace, you get a standard structure:

```text
openssme_workspace/
├── opensem.py              # The CLI entry point
├── configs/                # Configuration files for your projects
│   └── my_project/
│       ├── data_config.yaml   # Config for Data Forge
│       └── train_config.yaml  # Config for Training (Future)
├── data/                   # Data storage
│   └── my_project/
│       ├── raw/            # Your input files (PDFs, txt)
│       ├── processed/      # Synthesized JSONL files
│       └── golden/         # Golden test sets
├── src/                    # Source code
│   └── opensem/            # Core library
└── models/                 # Saved model adapters
```

## The Strategy Pattern

The heart of OpenSSME's extensibility is the **Strategy Pattern**. We define abstract base classes (Interfaces) for key components, and you can provide your own implementations.

### The `BaseForge` Interface

For the **Data Forge** stage, everything inherits from `BaseForge`.

```python
class BaseForge(ABC):
    @abstractmethod
    def load_data(self) -> List[str]:
        pass

    @abstractmethod
    def synthesize(self, raw_data: List[str]) -> List[Dict[str, Any]]:
        pass

    @abstractmethod
    def format_data(self, synthesized_data: List[Dict[str, Any]]) -> None:
        pass
```

*   **Default Implementation**: `TextForge` is the default strategy. It loads text/PDFs and uses an LLM to synthesize instruction pairs.
*   **Custom Implementation**: You can write a `PIIMaskingForge`, `ImageCaptioningForge`, or `FinancialForecastingForge` by simply inheriting from `BaseForge` and implementing these three methods.

You then tell OpenSSME which strategy to use in your `data_config.yaml`:

```yaml
forge_class: "my_custom_module.MyForge"
```

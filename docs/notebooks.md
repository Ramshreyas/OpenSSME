# Interactive Notebooks

The best way to learn is by doing. We have prepared Jupyter Notebooks that allow you to experiment with the OpenSSME API directly.

## Available Notebooks

### 1. Data Forge Tutorial
**Location**: `notebooks/data_forge_tutorial.ipynb`

This notebook covers:
*   **Setup**: Importing OpenSSME libraries.
*   **Standard Pipeline**: Running `TextForge` to synthesize data from text.
*   **Custom Extension**: Implementing a `PIIMaskingForge` to redact names from text using an LLM, demonstrating how to extend the framework for custom tasks.
*   **Deployment**: How to take your notebook code and deploy it to the CLI.

---

*To run these notebooks, ensure you have installed the development dependencies:*
```bash
pip install ipykernel
```

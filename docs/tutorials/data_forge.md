# Data Forge Tutorial

The **Data Forge** is the first stage of the OpenSSME pipeline. Its job is to transform raw, unstructured data into high-quality, structured training data (Instruction-Input-Output pairs).

## Standard Flow: Text Synthesis

By default, OpenSSME uses the `TextForge` strategy.

1.  **Input**: Text files, Markdown files, or PDFs in `data/<project>/raw`.
2.  **Process**:
    *   Chunks the text.
    *   Sends chunks to a "Teacher" LLM (Gemini 2.0 Flash).
    *   Prompts the Teacher to generate instruction-response pairs based on the text.
3.  **Output**: A JSONL file in `data/<project>/processed/train.jsonl`.

### Configuration
You can control this behavior in `configs/<project>/data_config.yaml`:

```yaml
forge_class: "opensem.forge.text_forge.TextForge"
params:
  teacher_model: "gemini-2.0-flash"
  max_chars_per_doc: 10000
  chunk_size: 2000
```

## Advanced Flow: Custom Strategies

OpenSSME shines when you need to do something specific. Let's say you want to build a model that **redacts PII (Personally Identifiable Information)**. You don't just want generic synthesis; you want a specific transformation.

### 1. Create a Custom Forge Class

Create a python file `src/my_project/pii_forge.py`:

```python
from opensem.forge import TextForge
import google.generativeai as genai
import os

class PIIMaskingForge(TextForge):
    def synthesize(self, raw_data):
        # Custom logic to ask LLM to redact names
        model = genai.GenerativeModel('gemini-2.0-flash')
        results = []
        for doc in raw_data:
            prompt = f"Redact all names in this text: {doc}"
            response = model.generate_content(prompt)
            results.append({
                "instruction": "Redact PII",
                "input": doc,
                "output": response.text
            })
        return results
```

### 2. Update Configuration

Point your project to this new class in `configs/<project>/data_config.yaml`:

```yaml
forge_class: "my_project.pii_forge.PIIMaskingForge"
```

### 3. Run

```bash
python opensem.py run-forge --project <project>
```

OpenSEM will now load your custom class and execute your specific logic!

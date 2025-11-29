# OpenSEM MVP Progress Tracker

This file breaks down the MVP implementation into fine-grained, actionable tasks. As tasks are completed, mark them as **[x]** and add notes as needed. The structure supports multiple SEM projects using shared scaffolding.

---

## 1. Project Setup
[ ] Create base directory structure for multi-SEM support
[ ] Add `.gitignore` for Python, Node.js, model files, and data
[ ] Initialize git repository
[ ] Create `requirements.txt` and install base dependencies
[ ] Create template configs (`train_config.yaml`, `eval_config.yaml`)
[ ] Document directory conventions for multiple SEMs
[ ] Create `scripts/` folder for utility scripts (e.g., new project creation, data formatting)
[ ] Plan CLI app (`opensem-cli`) for project and workflow management
[ ] Design CLI commands: `init`, `new-project`, `run-forge`, `train`, `evaluate`, etc.
[ ] Implement basic CLI app structure in `src/` or as standalone entry point
[ ] Add initial utility scripts to `scripts/` (e.g., create new SEM project)

## 2. Data Forge - Setup
- [ ] Implement data ingestion from `data/raw` (support .txt, .md)
- [ ] Integrate external API for instruction/output synthesis
- [ ] Allow teacher model configuration (e.g., GPT-4o, GPT-4o-mini)
- [ ] Format output to JSONL (ShareGPT format)
- [ ] Implement train/test split (90/10)
- [ ] Save processed data to `data/processed` per SEM project

## 3. Data Forge - Trial/Test Domain
- [ ] Select a test domain (e.g., medical, legal, technical)
- [ ] Populate `data/raw` with sample documents
- [ ] Run synthesis to create training pairs
- [ ] Create and verify a golden set in `data/golden`
- [ ] Validate processed data format and quality

## 4. Training Floor - Baseline Test Creation
- [ ] Implement baseline evaluation using `judge.py`
- [ ] Integrate Promptfoo for baseline scoring
- [ ] Use vanilla base model (e.g., Llama-3.2-3B)
- [ ] Iterate on baseline test prompts and golden set
- [ ] Document baseline results

## 5. Finetune - Local/Cloud
- [ ] Implement hardware detection (local/cloud)
- [ ] Configure Unsloth for training (YAML-driven)
- [ ] Enforce VRAM limits for local (4090)
- [ ] Enable full utilization for cloud (A100/H100)
- [ ] Save LoRA adapters to `models/adapters/{run_name}` per SEM
- [ ] Track training runs with Weights & Biases

## 6. Test Against Baseline
- [ ] Load fine-tuned adapter and rerun evaluation
- [ ] Compare fine-tuned results to baseline
- [ ] Output CLI summary table

## 7. Iterate Finetune & Test
- [ ] Refine training parameters/configs
- [ ] Repeat finetuning and evaluation for improved results
- [ ] Document iterations and findings

## 8. Report Generation
- [ ] Generate performance report (accuracy, improvement %)
- [ ] Summarize results for each SEM project
- [ ] Document lessons learned and next steps

---

**Notes:**
- Each SEM project should have its own subdirectory under `data/`, `models/`, and configs, but share core scripts and logic.
- Update this file regularly as tasks are completed or requirements change.

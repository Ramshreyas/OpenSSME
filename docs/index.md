# OpenSSME

**OpenSSME** (Open Source Small Model Expert) is a lightweight, extensible framework designed to be the "factory" for creating Small Expert Models (SEMs).

In a world dominated by massive General Purpose LLMs, OpenSSME empowers developers to build specialized, efficient, and domain-specific models that run faster and cheaper.

## Core Philosophy

*   **Lightweight**: Minimal dependencies, easy to install, and runs on standard hardware.
*   **Extensible**: Built on the **Strategy Pattern**, allowing you to swap out every component (Data Synthesis, Training, Evaluation) with your own custom logic.
*   **Pipeline-Driven**: A clear, three-stage process to go from raw data to a deployed expert model.

## The Pipeline

OpenSSME divides the model creation process into three distinct stages:

1.  **Data Forge** (Current Focus):
    *   Ingest raw data (PDFs, Text, Markdown).
    *   Synthesize high-quality instruction-tuning datasets using a "Teacher" LLM (e.g., Gemini, GPT-4).
    *   Format data for training.

2.  **Training Floor** (Coming Soon):
    *   Fine-tune small base models (e.g., Llama-3-8B, Gemma-2B) on your synthesized data.
    *   Support for LoRA and QLoRA for efficient training.

3.  **Evaluation Arena** (Coming Soon):
    *   Benchmark your expert model against the Teacher model.
    *   Generate reports on accuracy, hallucination rate, and domain specificity.

## Getting Started

Ready to build your first model? Jump straight into the action:

[**🚀 Go to Quick Start Guide**](tutorials/quick_start.md){ .md-button .md-button--primary }

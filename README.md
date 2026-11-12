# AI Sunday Classes

Each dated class folder contains standalone notebooks. Upload any notebook to Google Colab; no repository clone, helper file, or dataset upload is required. The notebook installs missing dependencies and includes its own sample data.

| Class date | Folder |
| --- | --- |
| 10 August 2026 | [LLM Foundations](classes/2026-08-10_LLM_Foundations/) |
| 1 November 2026 | [AI Evaluation](classes/2026-11-01_AI_Evaluation/) |

Dates preserve the original folders. RAG material remains with the evaluation class until its actual teaching date is assigned.

## Teach and share with Colab

1. Upload one notebook at https://colab.research.google.com/ and run setup first.
2. For Gemini notebooks, add your own `GEMINI_API_KEY` under Colab Secrets and enable notebook access. Otherwise the first API call asks for a hidden key. Notebook 04 needs no key. Foundations downloads public models; its Anthropic demo is optional.
3. Run cells in order. Internet, model availability, and sufficient API quota are required.
4. Share with Viewer access. Students choose **File → Save a copy in Drive**, connect to their own runtime, and supply their own key. Your Secrets are not included in their copy.
5. Clear outputs containing private information before sharing. Download generated results before the session ends; Colab runtime files are temporary.

## One local environment for all classes

Colab does not use your local `.venv`. For optional local work, run once from this repository root:

```powershell
uv sync
# Only if a root .env does not already exist:
Copy-Item .env.example .env
uv run python -m ipykernel install --user --name ai-sunday-classes --display-name "AI Sunday Classes"
uv run jupyter lab
```

Put your key in the existing root `.env`. Select the **AI Sunday Classes** kernel for every notebook. There is no dependency project inside a class folder.

For the next class, create `classes/YYYY-MM-DD_Topic/` and copy [the Colab template](templates/colab_class_template.ipynb) into it. Include setup, helpers and sample data directly in the notebook. Add any new local dependency to the root `pyproject.toml` and run `uv sync`.

## Private material

Instructor solutions, generated instructor data, `.env`, `.venv`, caches, and archives are ignored by Git. Originals are preserved locally under `_local_archive/before_colab_reorganization/`. Do not upload private files manually.

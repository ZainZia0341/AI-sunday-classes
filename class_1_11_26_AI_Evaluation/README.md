# Evals for AI Engineers: Hands-on Notebooks (Chapters 1-6)

Runnable Python examples for the first 6 chapters of *Evals for AI Engineers*.
LLM: **Google Gemini API**. Package manager: **uv**.

| Notebook | Chapter | What you run |
|---|---|---|
| `01_introduction.ipynb` | 1 | Specification gulf, Analyze → Measure → Improve, guardrails, monitoring, model migration |
| `02_llms_and_evaluation_basics.ipynb` | 2 | Single call, conversation, prompt template, BM25 / embedding / hybrid (RRF), tool + agent loop, absolute vs comparative evals |
| `03_error_analysis.ipynb` | 3 | Dimensions → tuples → synthetic queries, open / axial coding, labeling table, prevalence, saturation |
| `04_collaborative_evaluation.ipynb` | 4 | Percent agreement, Cohen / weighted / Fleiss kappa (no LLM needed) |
| `05_automated_evaluators.ipynb` | 5 | Code-based evals, LLM-as-judge, train/dev/test split, TPR/TNR, corrected success rate + bootstrap CI, Pass@k, Precision/Recall@k, diversity |
| `06_multi_turn_conversations.ipynb` | 6 | Session judge, length buckets, user simulator, isolating a failure, perturbation tests |

The two coding assignments are in 07_class_assignments.ipynb. Chapter notebooks contain examples only.
All prompts and sample data live in `data/eval_data.json` (edit it to experiment).

## 1. Install uv

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## 2. Get a free Gemini API key

Create a key at <https://aistudio.google.com/apikey>.

## 3. Set up the project

```bash
git clone <your-repo-url>
cd <repo-folder>

uv sync                      # creates .venv and installs everything
cp .env.example .env         # Windows: copy .env.example .env
```

Open `.env` and paste your key:

```
GEMINI_API_KEY=your-key-here
```

## 4. Run the notebooks

```bash
uv run jupyter lab
```

Open a notebook and run the cells from top to bottom.
In VS Code: open the notebook, choose the kernel **`.venv`** (Python 3), then *Run All*.

## Notes

- **Free-tier rate limits:** if you see `[retry ...] waiting 10s`, that is normal. The helper waits and tries again.
- **Model names:** default is `gemini-2.5-flash` (chat) and `gemini-embedding-001` (embeddings). If Google retires a name, set `GEMINI_MODEL` / `GEMINI_EMBED_MODEL` in `.env`.
- LLM outputs vary a little between runs, so your numbers may differ slightly from your classmates'.
- Notebook 4 needs no API key at all.

## Project files

```
common.py            # small helpers: ask(), chat(), embed(), load_data()
data/eval_data.json  # prompts + sample emails, traces, labels, conversations
0X_*.ipynb           # one notebook per chapter
pyproject.toml       # dependencies (uv reads this)
.env.example         # copy to .env
```

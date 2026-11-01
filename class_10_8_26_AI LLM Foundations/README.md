# AI / LLM Foundations notebook

Use the project's Python 3.12 virtual environment (`.venv`) as the notebook kernel.

Install the locked dependencies with `uv sync`, then execute all cells and save
their outputs with:

```powershell
.\.venv\Scripts\python.exe run_notebook.py
```

The runner resolves the notebook and cache from its own project directory, so
it also works when launched with an absolute path from another directory.
Temporary kernel files stay on the project drive and are removed after the run.

The first run downloads GPT-2, MiniLM, and Qwen2.5-0.5B-Instruct. Models are
cached in `.model_cache` on the project drive, outside version control. The
notebook uses standard HTTP downloads because accelerated Xet downloads stalled
on this machine.

The optional Anthropic API example is skipped by default. To run it, set
`RUN_ANTHROPIC_DEMO=1`, `ANTHROPIC_API_KEY`, and `ANTHROPIC_MODEL` to a model ID
available to your account. This example uses paid API access; keys should never
be saved in the notebook.

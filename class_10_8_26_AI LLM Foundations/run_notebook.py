"""Execute the class notebook with this interpreter and save its outputs."""
from pathlib import Path
import sys
import os
import asyncio

# Standard HTTP downloads avoid stalled Xet transfers on this machine.
os.environ.setdefault("HF_HUB_DISABLE_XET", "1")

import nbformat
from nbclient import NotebookClient
from jupyter_client.kernelspec import KernelSpecManager
from tempfile import TemporaryDirectory
import json


def main():
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    path = Path(__file__).resolve().with_name("LLM_Class_Simplified.ipynb")
    os.environ["NOTEBOOK_PROJECT_DIR"] = str(path.parent)
    notebook = nbformat.read(path, as_version=4)
    for cell in notebook.cells:
        if cell.cell_type == "code":
            cell.outputs = []
            cell.execution_count = None
    with TemporaryDirectory(dir=path.parent, prefix=".notebook-kernel-") as temporary:
        kernel_dir = Path(temporary) / "class-env"
        kernel_dir.mkdir()
        (kernel_dir / "kernel.json").write_text(json.dumps({
            "argv": [sys.executable, "-m", "ipykernel_launcher", "-f", "{connection_file}"],
            "display_name": "Class virtual environment", "language": "python",
        }), encoding="utf-8")
        manager = KernelSpecManager(kernel_dirs=[temporary])
        client = NotebookClient(
            notebook, timeout=1800, kernel_name="class-env",
            resources={"metadata": {"path": str(path.parent)}},
        )
        client.km = client.create_kernel_manager()
        client.km.kernel_spec_manager = manager
        client.on_cell_start = lambda cell, cell_index, **kwargs: print(
            f"Cell {cell_index + 1}/{len(notebook.cells)}: {cell.cell_type}", flush=True
        )
        try:
            client.execute()
        finally:
            nbformat.write(notebook, path)
    print("Notebook completed successfully.")


if __name__ == "__main__":
    main()

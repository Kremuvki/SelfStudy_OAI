#!/usr/bin/env python3
"""
Clean Jupyter notebooks by removing outputs and execution counts.
This script helps maintain clean version control by stripping execution data.
"""

import argparse
import json
import sys
from pathlib import Path


def clean_notebook(notebook_path: Path) -> bool:
    """
    Clean a single notebook by removing outputs and execution counts.

    Args:
        notebook_path: Path to the notebook file

    Returns:
        True if notebook was modified, False otherwise
    """
    try:
        with open(notebook_path, "r", encoding="utf-8") as f:
            notebook = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"❌ Error reading {notebook_path}: {e}")
        return False

    modified = False
    
    # Clean cells
    for cell in notebook.get("cells", []):
        # Remove execution count
        if "execution_count" in cell and cell["execution_count"] is not None:
            cell["execution_count"] = None
            modified = True

        # Remove outputs
        if "outputs" in cell and cell["outputs"]:
            cell["outputs"] = []
            modified = True
        
        # Remove metadata that can cause diffs
        if "metadata" in cell:
            metadata_to_remove = ["collapsed", "scrolled", "execution"]
            for key in metadata_to_remove:
                if key in cell["metadata"]:
                    del cell["metadata"][key]
                    modified = True
    
    # Clean notebook-level metadata
    if "metadata" in notebook:
        if "widgets" in notebook["metadata"]:
            del notebook["metadata"]["widgets"]
            modified = True

    # Write back if modified
    if modified:
        try:
            with open(notebook_path, "w", encoding="utf-8") as f:
                json.dump(notebook, f, indent=1, ensure_ascii=False)
                f.write("\n")  # Add trailing newline
            print(f"✅ Cleaned {notebook_path}")
        except Exception as e:
            print(f"❌ Error writing {notebook_path}: {e}")
            return False
    else:
        print(f"✨ {notebook_path} was already clean")

    return modified


def find_notebooks(path: Path, recursive: bool = True) -> list[Path]:
    """Find all notebook files in the given path."""
    if recursive:
        return list(path.rglob("*.ipynb"))
    else:
        return list(path.glob("*.ipynb"))


def main():
    """Main function to clean notebooks."""
    parser = argparse.ArgumentParser(
        description="Clean Jupyter notebooks by removing outputs and execution counts"
    )
    parser.add_argument(
        "paths", 
        nargs="*", 
        default=["."], 
        help="Paths to notebooks or directories (default: current directory)",
    )
    parser.add_argument(
        "--no-recursive",
        action="store_true",
        help="Don't search recursively in directories",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true", 
        help="Show what would be cleaned without making changes",
    )
    
    args = parser.parse_args()
    
    notebook_paths = []
    
    # Collect all notebook paths
    for path_str in args.paths:
        path = Path(path_str)
        
        if not path.exists():
            print(f"❌ Path does not exist: {path}")
            sys.exit(1)

        if path.is_file() and path.suffix == ".ipynb":
            notebook_paths.append(path)
        elif path.is_dir():
            notebook_paths.extend(find_notebooks(path, not args.no_recursive))
        else:
            print(f"⚠️  Skipping {path} (not a notebook or directory)")

    if not notebook_paths:
        print("📝 No notebooks found to clean")
        return

    print(f"🔍 Found {len(notebook_paths)} notebook(s) to process")

    if args.dry_run:
        print("🏃 DRY RUN MODE - no changes will be made")
        for nb_path in notebook_paths:
            print(f"   Would clean: {nb_path}")
        return
    
    # Clean notebooks
    modified_count = 0
    for nb_path in notebook_paths:
        if clean_notebook(nb_path):
            modified_count += 1

    print(f"\n🎉 Processed {len(notebook_paths)} notebooks")
    print(f"📝 Modified {modified_count} notebooks")
    print(f"✨ {len(notebook_paths) - modified_count} were already clean")


if __name__ == "__main__":
    main() 

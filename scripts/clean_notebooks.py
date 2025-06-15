#!/usr/bin/env python3
"""
Script to clean Jupyter notebooks by removing outputs and execution counts.
This helps keep notebooks clean in version control.
"""

import argparse
import json
import os
from pathlib import Path


def clean_notebook(notebook_path):
    """Clean a single notebook file."""
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    # Clean cells
    for cell in notebook.get('cells', []):
        # Remove outputs
        if 'outputs' in cell:
            cell['outputs'] = []
        
        # Remove execution count
        if 'execution_count' in cell:
            cell['execution_count'] = None
    
    # Remove kernel metadata
    if 'metadata' in notebook and 'kernelspec' in notebook['metadata']:
        notebook['metadata']['kernelspec'] = {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        }
    
    # Write cleaned notebook
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=2, ensure_ascii=False)
        f.write('\n')  # Add final newline
    
    print(f"Cleaned: {notebook_path}")


def main():
    parser = argparse.ArgumentParser(description="Clean Jupyter notebooks")
    parser.add_argument(
        "paths", 
        nargs="*", 
        default=["."], 
        help="Paths to notebooks or directories (default: current directory)"
    )
    parser.add_argument(
        "--recursive", 
        "-r", 
        action="store_true", 
        help="Search recursively in directories"
    )
    
    args = parser.parse_args()
    
    notebook_files = []
    
    for path_str in args.paths:
        path = Path(path_str)
        
        if path.is_file() and path.suffix == '.ipynb':
            notebook_files.append(path)
        elif path.is_dir():
            pattern = "**/*.ipynb" if args.recursive else "*.ipynb"
            notebook_files.extend(path.glob(pattern))
    
    if not notebook_files:
        print("No notebook files found.")
        return
    
    for notebook_file in notebook_files:
        try:
            clean_notebook(notebook_file)
        except Exception as e:
            print(f"Error cleaning {notebook_file}: {e}")


if __name__ == "__main__":
    main() 
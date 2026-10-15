#!/usr/bin/env bash
set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo "Building cv_en.tex..."
docker run --rm -v "$(pwd)":/data -w /data texlive/texlive xelatex cv_en.tex
echo "Building cv_pt.tex..."
docker run --rm -v "$(pwd)":/data -w /data texlive/texlive xelatex cv_pt.tex

echo "Done. PDF files generated:"
ls -l *.pdf
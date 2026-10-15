# PDF Generation from LaTeX

This directory contains LaTeX source files for Eduardo França's CV in English (`cv_en.tex`) and Portuguese (`cv_pt.tex`). The files are designed to be compiled with XeLaTeX to use the Inter and Newsreader fonts (as used in the HTML version).

## Requirements

- Docker (to run a TeX Live container)
- No local TeX installation needed.

## Generating PDFs

Run the provided script `build.sh` to compile both CVs:

```bash
./build.sh
```

This will produce `cv_en.pdf` and `cv_pt.pdf` in the same directory.

### Manual Docker Commands

If you prefer to run manually:

```bash
# Compile English CV
docker run --rm -v "$(pwd)":/data -w /data texlive/texlive xelatex cv_en.tex

# Compile Portuguese CV
docker run --rm -v "$(pwd)":/data -w /data texlive/texlive xelatex cv_pt.tex
```

Each command will produce a PDF file.

## Notes

- The LaTeX sources use the `moderncv` package with the `classic` style and blue color theme.
- Fonts are set via `fontspec` to Inter (sans-serif). If the container does not have these fonts, they will fallback to defaults; however, the TeX Live image includes a wide variety of fonts.
- Ensure you have sufficient disk space for the container.

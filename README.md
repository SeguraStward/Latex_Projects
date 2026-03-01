# LaTeX Docker Environment

A complete LaTeX development environment using Docker with the full TeX Live distribution.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) (with Docker Compose)
- [VS Code](https://code.visualstudio.com/) (optional, for IDE integration)
- [LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop) extension (optional)

## Quick Start

```bash
# 1. Initial setup (build Docker image — only needed once)
chmod +x init.sh compile.sh
./init.sh

# 2. Create a new project
./compile.sh new my-paper

# 3. Edit your document
#    Open projects/my-paper/main.tex in VS Code

# 4. Compile
./compile.sh my-paper
```

## Project Structure

```
Latex_Projects/
├── Dockerfile              # Docker image definition
├── docker-compose.yml      # Docker Compose services
├── compile.sh              # Main compilation script
├── init.sh                 # One-time setup script
├── .vscode/                # VS Code configuration
│   ├── settings.json       # LaTeX Workshop + Docker integration
│   └── extensions.json     # Recommended extensions
├── projects/               # Your LaTeX projects live here
│   ├── example/            # Example project (test/reference)
│   │   ├── main.tex
│   │   ├── sections/
│   │   ├── figures/
│   │   └── references/
│   └── my-paper/           # Your projects...
│       └── main.tex
└── README.md
```

## Usage

### compile.sh Commands

| Command | Description |
|---|---|
| `./compile.sh <project>` | Compile with latexmk + pdfLaTeX |
| `./compile.sh <project> xelatex` | Compile with XeLaTeX |
| `./compile.sh <project> lualatex` | Compile with LuaLaTeX |
| `./compile.sh <project> clean` | Remove build artifacts |
| `./compile.sh <project> shell` | Open shell inside container |
| `./compile.sh <project> watch` | Auto-recompile on file changes |
| `./compile.sh new <name>` | Create new project from template |
| `./compile.sh list` | List all projects |

### VS Code Integration

With the LaTeX Workshop extension installed, the workspace is pre-configured to:

- **Auto-compile on save** — saves trigger Docker-based compilation
- **PDF preview in tab** — view PDF output directly in VS Code
- **SyncTeX** — click on PDF to jump to source, and vice versa
- **Hide build artifacts** — aux/log/etc. files are hidden from explorer

Available recipes (select from the LaTeX Workshop status bar):
- `latexmk (Docker)` — recommended, handles bibliography automatically
- `xelatex (Docker)` — for custom OpenType/TrueType fonts
- `lualatex (Docker)` — for Lua scripting and advanced font features
- `pdflatex only (Docker)` — single pdfLaTeX pass (fast, no bib)

### Direct Docker Commands

```bash
# Run any LaTeX command
docker compose run --rm latex "pdflatex main.tex"

# Interactive shell
docker compose run --rm --entrypoint /bin/bash latex

# Check installed packages
docker compose run --rm latex "tlmgr list --only-installed | wc -l"
```

## Engines Comparison

| Engine | Best For | Font Support |
|---|---|---|
| **pdfLaTeX** | Most documents, fastest compilation | Type1, limited OTF |
| **XeLaTeX** | Documents with custom system fonts | Full OpenType/TrueType |
| **LuaLaTeX** | Advanced scripting, custom fonts | Full OpenType/TrueType |

**Recommendation:** Use pdfLaTeX (default) unless you need custom fonts or Lua scripting.

## Tips

- Place images in `projects/<name>/figures/`
- Place bibliography in `projects/<name>/references/references.bib`
- Split long documents into `sections/` files using `\input{sections/chapter1}`
- Use `latexmk` (default) — it automatically determines how many passes are needed and runs biber/bibtex when necessary

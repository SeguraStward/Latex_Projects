#!/usr/bin/env bash
# =============================================================================
# compile.sh — Compile LaTeX projects using Docker
# =============================================================================
# Usage:
#   ./compile.sh <project-name>          Compile with latexmk (recommended)
#   ./compile.sh <project-name> clean    Remove build artifacts
#   ./compile.sh <project-name> shell    Open a shell inside the container
#   ./compile.sh <project-name> watch    Watch and auto-recompile on changes
#   ./compile.sh new <project-name>      Create a new project from template
# =============================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECTS_DIR="$SCRIPT_DIR/projects"
COMPOSE_CMD="docker compose -f $SCRIPT_DIR/docker-compose.yml"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

info()  { echo -e "${BLUE}[INFO]${NC} $*"; }
ok()    { echo -e "${GREEN}[OK]${NC} $*"; }
warn()  { echo -e "${YELLOW}[WARN]${NC} $*"; }
err()   { echo -e "${RED}[ERROR]${NC} $*" >&2; }

usage() {
    echo "Usage: $0 <project-name> [command]"
    echo ""
    echo "Commands:"
    echo "  (default)    Compile project with latexmk -pdf"
    echo "  clean        Remove auxiliary/build files"
    echo "  shell        Open interactive shell in container"
    echo "  watch        Watch for changes and auto-recompile"
    echo "  xelatex      Compile with XeLaTeX engine"
    echo "  lualatex     Compile with LuaLaTeX engine"
    echo "  manim        List scenes in animations/scenes.py"
    echo "  manim <Scene> Render scene in low quality (preview)"
    echo "  manim-hq <Scene> Render scene in 1080p60 (final)"
    echo ""
    echo "Special commands:"
    echo "  new <name>   Create a new project from template"
    echo "  list         List all projects"
    echo ""
    echo "Examples:"
    echo "  $0 my-paper                      # Compile my-paper/main.tex"
    echo "  $0 my-paper clean                # Clean build artifacts"
    echo "  $0 my-paper manim                # List available scenes"
    echo "  $0 my-paper manim TitleScene     # Preview render"
    echo "  $0 my-paper manim-hq TitleScene  # High quality render"
    echo "  $0 new thesis                    # Create new project 'thesis'"
    exit 1
}

# Ensure projects directory exists
mkdir -p "$PROJECTS_DIR"

# --- Command: list ---
if [[ "${1:-}" == "list" ]]; then
    info "Projects in $PROJECTS_DIR:"
    for dir in "$PROJECTS_DIR"/*/; do
        if [ -d "$dir" ]; then
            name=$(basename "$dir")
            if [ -f "$dir/main.tex" ]; then
                echo -e "  ${GREEN}●${NC} $name"
            else
                echo -e "  ${YELLOW}○${NC} $name (no main.tex)"
            fi
        fi
    done
    exit 0
fi

# --- Command: new ---
if [[ "${1:-}" == "new" ]]; then
    PROJECT_NAME="${2:?Error: provide a project name. Usage: $0 new <name>}"
    PROJECT_PATH="$PROJECTS_DIR/$PROJECT_NAME"

    if [ -d "$PROJECT_PATH" ]; then
        err "Project '$PROJECT_NAME' already exists at $PROJECT_PATH"
        exit 1
    fi

    info "Creating new project: $PROJECT_NAME"
    mkdir -p "$PROJECT_PATH"/{figures,sections,references,animations}

    # Copy template if it exists, otherwise create minimal main.tex
    if [ -f "$PROJECTS_DIR/_template/main.tex" ]; then
        cp -r "$PROJECTS_DIR/_template/"* "$PROJECT_PATH/"
        ok "Created from template"
    else
        cat > "$PROJECT_PATH/main.tex" << 'LATEX'
\documentclass[12pt,a4paper]{article}

% --- Packages ---
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[english]{babel}
\usepackage{amsmath,amssymb,amsthm}
\usepackage{graphicx}
\usepackage[colorlinks=true,linkcolor=blue,citecolor=blue,urlcolor=blue]{hyperref}
\usepackage{geometry}
\usepackage{booktabs}
\usepackage{microtype}

\geometry{margin=1in}

% --- Document Info ---
\title{Your Title Here}
\author{Your Name}
\date{\today}

\begin{document}

\maketitle

\begin{abstract}
    Your abstract here.
\end{abstract}

\tableofcontents
\newpage

\section{Introduction}
Your introduction here.

\section{Methods}
Your methods here.

\section{Results}
Your results here.

\section{Conclusion}
Your conclusion here.

% \bibliographystyle{plain}
% \bibliography{references/references}

\end{document}
LATEX
        ok "Created with default template"
    fi

    # Create Manim animations template
    cat > "$PROJECT_PATH/animations/scenes.py" << 'PYTHON'
from manim import *

class TitleScene(Scene):
    def construct(self):
        title = Text("Your Research Title", font_size=48)
        subtitle = Text("Your Name", font_size=32, color=GRAY)
        subtitle.next_to(title, DOWN)
        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait(2)


class FormulaScene(Scene):
    def construct(self):
        formula = MathTex(r"E = mc^2")
        self.play(Write(formula))
        self.wait(2)
PYTHON
    ok "Created animations/scenes.py template"

    ok "Project created at: $PROJECT_PATH"
    echo "  Edit: $PROJECT_PATH/main.tex"
    echo "  Compile: $0 $PROJECT_NAME"
    echo "  Animate: $0 $PROJECT_NAME manim TitleScene"
    exit 0
fi

# --- Validate project ---
PROJECT_NAME="${1:?$(usage)}"
COMMAND="${2:-compile}"
PROJECT_PATH="$PROJECTS_DIR/$PROJECT_NAME"

if [ ! -d "$PROJECT_PATH" ]; then
    err "Project '$PROJECT_NAME' not found in $PROJECTS_DIR"
    echo "  Create it with: $0 new $PROJECT_NAME"
    echo "  Or list projects: $0 list"
    exit 1
fi

if [ ! -f "$PROJECT_PATH/main.tex" ]; then
    err "No main.tex found in $PROJECT_PATH"
    exit 1
fi

# --- Execute command ---
case "$COMMAND" in
    compile)
        info "Compiling $PROJECT_NAME with latexmk (pdfLaTeX)..."
        $COMPOSE_CMD run --rm -w "/workspace/projects/$PROJECT_NAME" latex \
            "latexmk -pdf -interaction=nonstopmode -file-line-error main.tex"
        ok "Output: $PROJECT_PATH/main.pdf"
        ;;
    xelatex)
        info "Compiling $PROJECT_NAME with XeLaTeX..."
        $COMPOSE_CMD run --rm -w "/workspace/projects/$PROJECT_NAME" latex \
            "latexmk -xelatex -interaction=nonstopmode -file-line-error main.tex"
        ok "Output: $PROJECT_PATH/main.pdf"
        ;;
    lualatex)
        info "Compiling $PROJECT_NAME with LuaLaTeX..."
        $COMPOSE_CMD run --rm -w "/workspace/projects/$PROJECT_NAME" latex \
            "latexmk -lualatex -interaction=nonstopmode -file-line-error main.tex"
        ok "Output: $PROJECT_PATH/main.pdf"
        ;;
    clean)
        info "Cleaning build artifacts in $PROJECT_NAME..."
        $COMPOSE_CMD run --rm -w "/workspace/projects/$PROJECT_NAME" latex \
            "latexmk -C && rm -f *.bbl *.run.xml *.synctex.gz"
        ok "Cleaned"
        ;;
    shell)
        info "Opening shell in container (project: $PROJECT_NAME)..."
        docker compose -f "$SCRIPT_DIR/docker-compose.yml" run --rm \
            -w "/workspace/projects/$PROJECT_NAME" --entrypoint /bin/bash latex
        ;;
    watch)
        info "Watching $PROJECT_NAME for changes (Ctrl+C to stop)..."
        $COMPOSE_CMD run --rm -w "/workspace/projects/$PROJECT_NAME" latex \
            "echo 'Watching for .tex changes...' && while true; do \
                inotifywait -r -e modify,create --include '\.tex$' . 2>/dev/null; \
                echo \"[\$(date '+%H:%M:%S')] Recompiling...\"; \
                latexmk -pdf -interaction=nonstopmode main.tex 2>&1 | tail -3; \
            done"
        ;;
    manim)
        SCENE="${3:-}"
        ANIMATIONS_DIR="$PROJECT_PATH/animations"
        if [ ! -d "$ANIMATIONS_DIR" ]; then
            err "No existe la carpeta animations/ en $PROJECT_PATH"
            exit 1
        fi
        if [ -z "$SCENE" ]; then
            info "Escenas disponibles en $PROJECT_NAME/animations/:"
            grep -rh "^class S" "$ANIMATIONS_DIR"/*.py 2>/dev/null \
                | sed 's/class \(S[^(]*\).*/  \1/'
        else
            # Buscar en que archivo esta la clase
            SCENE_FILE=$(grep -rl "^class $SCENE" "$ANIMATIONS_DIR"/*.py 2>/dev/null | head -1)
            if [ -z "$SCENE_FILE" ]; then
                err "Escena '$SCENE' no encontrada en ningun archivo .py de animations/"
                exit 1
            fi
            SCENE_BASENAME=$(basename "$SCENE_FILE")
            info "Renderizando '$SCENE' desde $SCENE_BASENAME (baja calidad)..."
            docker compose -f "$SCRIPT_DIR/docker-compose.yml" run --rm \
                -w "/workspace/projects/$PROJECT_NAME/animations" manim \
                manim -ql "$SCENE_BASENAME" "$SCENE"
            ok "Output: $ANIMATIONS_DIR/media/videos/${SCENE_BASENAME%.py}/480p15/${SCENE}.mp4"
        fi
        ;;
    manim-hq)
        SCENE="${3:?Error: indica el nombre de la escena. Uso: $0 $PROJECT_NAME manim-hq <Escena>}"
        ANIMATIONS_DIR="$PROJECT_PATH/animations"
        SCENE_FILE=$(grep -rl "^class $SCENE" "$ANIMATIONS_DIR"/*.py 2>/dev/null | head -1)
        if [ -z "$SCENE_FILE" ]; then
            err "Escena '$SCENE' no encontrada en ningun archivo .py de animations/"
            exit 1
        fi
        SCENE_BASENAME=$(basename "$SCENE_FILE")
        info "Renderizando '$SCENE' desde $SCENE_BASENAME (1080p60)..."
        docker compose -f "$SCRIPT_DIR/docker-compose.yml" run --rm \
            -w "/workspace/projects/$PROJECT_NAME/animations" manim \
            manim -qh "$SCENE_BASENAME" "$SCENE"
        ok "Output: $ANIMATIONS_DIR/media/videos/${SCENE_BASENAME%.py}/1080p60/${SCENE}.mp4"
        ;;
    *)
        err "Unknown command: $COMMAND"
        usage
        ;;
esac

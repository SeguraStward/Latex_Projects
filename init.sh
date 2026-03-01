#!/usr/bin/env bash
# =============================================================================
# init.sh — One-time setup: build Docker image and verify installation
# =============================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

info()  { echo -e "${BLUE}[INFO]${NC} $*"; }
ok()    { echo -e "${GREEN}[OK]${NC} $*"; }

echo "============================================="
echo "  LaTeX Docker Environment Setup"
echo "============================================="
echo ""

# Step 1: Build Docker image
info "Building Docker image (this may take a few minutes on first run)..."
docker compose -f "$SCRIPT_DIR/docker-compose.yml" build latex

# Step 2: Verify TeX Live
info "Verifying TeX Live installation..."
docker compose -f "$SCRIPT_DIR/docker-compose.yml" run --rm latex \
    "pdflatex --version | head -1 && echo '' && \
     xelatex --version | head -1 && echo '' && \
     lualatex --version | head -1 && echo '' && \
     latexmk --version | head -1 && echo '' && \
     biber --version | head -1"

# Step 3: Create projects directory
mkdir -p "$SCRIPT_DIR/projects"

# Step 4: Compile example if it exists
if [ -f "$SCRIPT_DIR/projects/example/main.tex" ]; then
    info "Compiling example project..."
    "$SCRIPT_DIR/compile.sh" example
fi

echo ""
echo "============================================="
ok "Setup complete!"
echo "============================================="
echo ""
echo "Quick start:"
echo "  ./compile.sh new my-paper    # Create a new project"
echo "  ./compile.sh my-paper        # Compile a project"
echo "  ./compile.sh list            # List all projects"
echo ""

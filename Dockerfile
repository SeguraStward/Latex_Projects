# =============================================================================
# LaTeX Development Environment
# Based on the official TeX Live full distribution
# =============================================================================
FROM texlive/texlive:latest

LABEL maintainer="LaTeX Projects"
LABEL description="Full TeX Live environment for compiling LaTeX documents"

# Install additional useful tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    # PDF utilities
    ghostscript \
    poppler-utils \
    # File watching for auto-compilation
    inotify-tools \
    # Common utilities
    make \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /workspace

# Default command: keep container running or compile if args are passed
ENTRYPOINT ["/bin/bash"]

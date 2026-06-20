# =========================
# 🧱 BUILD STAGE
# =========================
FROM python:3.12-slim AS builder

ENV DEBIAN_FRONTEND=noninteractive

# Install only what is needed to build/install dependencies
RUN apt-get update && apt-get install -y \
    curl \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install UV
RUN curl -Ls https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

# Copy dependency definitions first (better caching)
COPY pyproject.toml uv.lock* /app/

# Install Python dependencies into UV environment
RUN uv sync --frozen || uv pip install pygame


# =========================
# 🎮 RUNTIME STAGE
# =========================
FROM python:3.12-slim

ENV DEBIAN_FRONTEND=noninteractive

# --- ONLY runtime SDL dependencies (NO -dev packages) ---
RUN apt-get update && apt-get install -y \
    libsdl2-2.0-0 \
    libsdl2-image-2.0-0 \
    libsdl2-mixer-2.0-0 \
    libsdl2-ttf-2.0-0 \
    libgl1 \
    libglib2.0-0 \
    libxext6 \
    libxrender1 \
    libsm6 \
    libx11-6 \
    && rm -rf /var/lib/apt/lists/*

# Environment tuning for Docker + pygame
ENV SDL_VIDEODRIVER=x11
ENV SDL_AUDIODRIVER=dummy
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONPATH=/app

# Copy UV from builder
COPY --from=builder /root/.local /root/.local
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

# Copy installed environment + project
COPY --from=builder /app /app
COPY . /app

# Optional: sanity check pygame import at build time
RUN uv run python -c "import pygame; print('pygame OK:', pygame.version.ver)"

# Launch game
#CMD ["uv", "run", "python", "SimpsonsTrivia.py"]
CMD ["uv", "run", "python", "main.py"]
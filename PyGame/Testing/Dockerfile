FROM python:3.12-slim

# Avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# System dependencies required by pygame (SDL, audio, fonts)
RUN apt-get update && apt-get install -y \
    gcc \
    git \
    curl \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    libgstreamer1.0-0 \
    libgstreamer-plugins-base1.0-0 \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    && rm -rf /var/lib/apt/lists/*

# Install UV (Astral package manager)
RUN curl -Ls https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"

# Set working directory
WORKDIR /app

# Copy dependency files first (better Docker layer caching)
COPY pyproject.toml uv.lock* /app/

# Install dependencies using UV
RUN uv sync --frozen || uv pip install pygame

# Copy full project (engine, assets, game code, entry point)
COPY . /app

# Ensure assets are discoverable
ENV PYTHONPATH=/app

# Default entry point
CMD ["uv", "run", "python", "SimpsonsTrivia.py"]
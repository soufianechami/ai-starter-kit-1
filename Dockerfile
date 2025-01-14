# Use an official Python runtime as a parent image
FROM python:3.11.5-bookworm as builder

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    poppler-utils \
    tesseract-ocr \
    qpdf \
    make \
    ffmpeg \
    libsm6 \
    libxext6 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory in the container
WORKDIR /app

# Copy only the requirements file first
COPY base-requirements.txt .

# Upgrade pip and install project dependencies
RUN pip install --upgrade pip

# Use BuildKit's cache mount to speed up pip installs
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r base-requirements.txt

# Final stage
FROM python:3.11.5-slim-bookworm

# Copy installed packages from builder stage
COPY --from=builder /usr/local /usr/local

# Install runtime system dependencies
RUN apt-get update && apt-get install -y \
    poppler-utils \
    tesseract-ocr \
    qpdf \
    ffmpeg \
    libsm6 \
    libxext6 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory in the container
WORKDIR /app

# Copy the application code
COPY . .

# Copy the startup script and make it executable
COPY docker-startup.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-startup.sh

# Expose the ports for the parsing service and Streamlit
EXPOSE 8005 8501

# Set the startup script as the entrypoint
ENTRYPOINT ["/usr/local/bin/docker-startup.sh"]

# Default command
CMD ["/bin/bash"]
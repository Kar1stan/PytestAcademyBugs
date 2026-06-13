# Use official Python runtime as base image
FROM python:3.14

# Set working directory in container
WORKDIR /app

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    # Prevent Python from writing .pyc files to disk
    PYTHONDONTWRITEBYTECODE=1 \
    # Prevent pip from caching packages
    PIP_NO_CACHE_DIR=1
# Set the directory for pip cache

# Copy requirements.txt and install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Install Playwright browsers and system dependencies
# The --with-deps flag automatically installs all required system packages
RUN playwright install --with-deps

# Copy project files
COPY . .

# Create allure-results directory if it doesn't exist
RUN mkdir -p allure-results

# Default command - run pytest
CMD ["pytest", "--alluredir=allure-results"]
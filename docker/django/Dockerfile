# Base image - official Python on Alpine (lightweight)
FROM python:3.11-slim

# Why we set this:
# PYTHONDONTWRITEBYTECODE = dont create .pyc files
# PYTHONUNBUFFERED = show logs immediately in terminal
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create working directory inside container
WORKDIR /app

# Copy requirements first (Docker layer caching - faster rebuilds)
COPY ../../app/backend/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire backend code
COPY ../../app/backend .

# Expose port 8000
EXPOSE 8000

# Command to run when container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

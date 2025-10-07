FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy exporter script
COPY system_metrics_exporter.py .

# Expose port inside container
EXPOSE 8080

# Run exporter
CMD ["python", "system_metrics_exporter.py"]

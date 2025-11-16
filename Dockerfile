# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Expose the port Render expects
EXPOSE 10000

# Start the Flask app using gunicorn
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:10000"]

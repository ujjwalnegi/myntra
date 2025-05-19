# Use the official Python image (closest to your version)
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your project files
COPY . .

# Default command to run tests
CMD ["pytest", "--maxfail=1", "--disable-warnings", "-v"]

# Use a lightweight Python image
FROM python:3.11-slim-buster

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code
COPY main.py .

# Set the working directory to the source code folder

# Start the application using uvicorn
CMD ["python", "main.py"]
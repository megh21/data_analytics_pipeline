# Use a lightweight Python base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
# COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir  pykafka 
# -r requirements.txt

# Copy the Python script into the container
COPY generate_data.py .

# Run the Python script when the container launches
CMD ["python", "generate_data.py"]

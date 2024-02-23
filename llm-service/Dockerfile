# Use an NVIDIA CUDA base image
FROM nvidia/cuda:latest

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    wget \
    md5sum \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set up a working directory
WORKDIR /app

# Upgrade pip
RUN pip3 install --no-cache-dir --upgrade pip

# Install Python dependencies
# Note: This assumes you have a requirements.txt file listing all needed packages.
# If Llama 2 has specific Python package requirements, they should be included in this file.
COPY requirements.txt /app/
RUN pip3 install --no-cache-dir -r requirements.txt

# Assuming you have a script to download Llama 2 models as per README instructions
# and it's named `download_models.sh`. This script should automate the download process,
# accepting necessary parameters like the signed URL for model download.
COPY download_models.sh /app/
RUN chmod +x /app/download_models.sh
# You would need to run this script manually or automate it with environment variables
# since it requires interaction (URL input). Docker build process can't handle interactive input.

# Copy the Llama 2 application into the container
# Make sure all necessary scripts and code files are included.
COPY . /app

# Expose the port the app runs on if your app includes a web server or API interface
EXPOSE 5000

# Command to run your Llama 2 inference script
# Replace `your_inference_script.py` with your actual Llama 2 inference script name.
# Ensure your script is executable and properly configured for the downloaded models.
CMD ["python3", "your_inference_script.py"]

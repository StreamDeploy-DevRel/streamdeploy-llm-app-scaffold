FROM nvidia/cuda:latest

# Install Python and pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Set up a working directory
WORKDIR /app

# Copy the Llama 2 application into the container
COPY . /app

# Install dependencies
RUN pip3 install --no-cache-dir -e .

# Expose the port the app runs on
EXPOSE 5000

# Run the Llama 2 inference script
CMD ["python3", "your_inference_script.py"]

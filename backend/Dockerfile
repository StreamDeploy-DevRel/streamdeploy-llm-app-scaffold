# Start from the official Go image to create a build artifact.
FROM python

# Copy local code to the container image.
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /app/src

# Run the web service on container startup.
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]

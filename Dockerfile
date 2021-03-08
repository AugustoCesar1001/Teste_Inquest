# Use python 3.8.1 container image
FROM python:3.8.1

# Set the Working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the dependences
RUN pip install -r requirements.txt

CMD ["run.py"]
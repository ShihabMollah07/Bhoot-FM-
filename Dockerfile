# Base Python image
FROM python:3.10.8-slim-buster

# Update and install system dependencies
RUN apt update && apt upgrade -y
RUN apt install git -y

# Copy and install Python requirements
COPY requirements.txt /requirements.txt
RUN pip3 install -U pip && pip3 install -U -r /requirements.txt

# Create a working directory and copy the bot files
WORKDIR /app
COPY . .

# Command to run the bot when the container starts
CMD ["python", "bot.py"]

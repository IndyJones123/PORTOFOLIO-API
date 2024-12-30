# Python + PYARMOR

# FROM ubuntu:20.04 

# RUN dpkg --add-architecture i386 && \
#     apt-get update && \
#     apt-get install -y wine32

# # Set the working directory
# WORKDIR /app

# # Copy required files into the image
# COPY /asd/portofolio.exe .  
# COPY /asd/confighttp.xml .

# # Ensure the executable has proper permissions
# # RUN chmod +x ./portofolio.exe

# # Command to run the executable using Wine
# # CMD ["ls", "-l", "./"]
# CMD ["wine", "./portofolio.exe"]




# If its Python

# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY requirements.txt /app/

RUN pip install psycopg2-binary 

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the .whl file into the container (assuming it's in the current directory)
COPY MainModuleADM-0.0.2-py3-none-any.whl /app/

# Install the .whl file
RUN pip install /app/MainModuleADM-0.0.2-py3-none-any.whl

# Copy the rest of the current directory contents into the container at /app
COPY . /app

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Define environment variable
ENV PYTHONUNBUFFERED=1

# # Run uvicorn server
CMD ["uvicorn", "portofolio:app", "--host", "0.0.0.0", "--port", "8000"]




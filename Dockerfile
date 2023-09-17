# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variable to prevent buffering of Python output
ENV PYTHONUNBUFFERED 1

# Install PostgreSQL and the PostgreSQL client
RUN apt-get update \
    && apt-get install -y postgresql postgresql-client

# Set the working directory within the container
WORKDIR /zhongwen

# Copy the requirements.txt file into the container
COPY requirements.txt /zhongwen/

# Install project dependencies using pip
RUN pip install -r requirements.txt

# Create the Django project
RUN django-admin startproject zhongwen .
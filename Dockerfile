# Use an official Python runtime as a parent image
FROM python:3

# nginx
FROM nginx

RUN rm /etc/nginx/conf.d/default.conf
COPY mysite.conf /etc/nginx/conf.d

# Set environment variable to prevent buffering of Python output
ENV PYTHONUNBUFFERED 1

# Create a directory for your Django project
RUN mkdir /zhongwen

# Set the working directory within the container
WORKDIR /zhongwen

# Copy the requirements.txt file into the container
COPY requirements.txt /zhongwen/

# Install project dependencies using pip
RUN pip install -r requirements.txt

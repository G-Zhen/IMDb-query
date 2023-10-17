# Use the official Python image as the base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the local code to the container
COPY . .

# Install any required dependencies
RUN pip install -r website/requirements.txt 

# Expose the port your Flask app will run on (e.g., 5000)
EXPOSE 5000

# Define the command to run your Flask app
CMD [ "python", "app.py" ]  
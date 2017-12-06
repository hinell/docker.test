# Use an official Python runtime as a parent image
FROM python:alpine

# Define environment variable
ENV NAME="DOCKER IS RUNNING" CONT_WRK_DIR=/app

# Set the working directory to /app
WORKDIR ${CONT_WRK_DIR}

# Copy the current directory contents into the container at /app
ADD ./requirements.txt ${CONT_WRK_DIR}

# VOLUME ["./app"]
# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

#FROM pyenv
#
# ENV NAME=World CONT_WRK_DIR=/app
#
#WORKDIR ${CONT_WRK_DIR}
#
ADD . ${CONT_WRK_DIR}
#
EXPOSE 80

#
## Run app.py when the container launches
CMD ["python", "app.py"]


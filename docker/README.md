<!--nginx logo -->
<br />
<div align="center">
   <img src="docker.png" alt="Logo" width="150" height="100">

<h3 align="center">Docker Guide.</h3>
</div>

# Docker Guide
This guide provides instructions on how to build, run, and manage your application using Docker. By containerizing your application, you can ensure consistency across different environments and streamline the deployment process.

## Prerequisites

* [![Docker][Docker]][Docker-url]

## Installation
You can install Docker and FastAPI using pip:
```bash
pip install docker
pip install fastapi
```

## What is Docker ?
- Docker is an open-source platform that enables developers to automate the deployment, scaling, and management of applications inside lightweight containers. Containers bundle the software, libraries, and dependencies together, ensuring consistency across multiple environments.


## Use cases of Docker :
1. **Microservices**: Deploy individual services in isolated containers.
2. **Continuous Integration/Continuous Deployment (CI/CD)**: Streamline the testing and deployment process.
3. **Environment Consistency**: Ensure that your application runs the same in development, testing, and production.
4. **Resource Efficiency**: Containers are lightweight and share the host system's kernel, making them more efficient than traditional virtual machines.


## What is Docker container ?
- A Docker container is a standardized unit of software that encapsulates code and its dependencies, ensuring that the application runs quickly and reliably from one computing environment to another.

## What is Docker Image ?
- A Docker image is a read-only template that contains the application's code, runtime, libraries, and settings needed to run the application. It is the blueprint from which containers are created.

## What is a Dockerfile?
- A Dockerfile is a script containing a series of instructions on how to build a Docker image. It defines the steps needed to create the image, including the base image to use, the application files to copy, and the commands to run.

### Example of Dockerfile:
```bash
# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE $SERVER_PORT

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
```

## Key Instructions in Dockerfile:
1. FROM: Specifies the base image to use for the Docker image.
2. WORKDIR: Sets the working directory inside the container.
3. COPY: Copies files from the host to the container.
4. RUN: Executes commands in the container, such as installing dependencies.
5. EXPOSE: Informs Docker that the container listens on the specified network ports at runtime.
6. CMD: Provides the command to run when the container starts.

## Building and Running a Docker Image
1. Build an image using the command:
    ```bash
    docker build -t image-name .
    ```
- -t is used to tag the image with a name.
- . specifies the location of the Dockerfile (current directory).

2. Run the built image:
    ```bash
    docker run -p 8000:8000 image-name
    ```
where internal and external ports are specified.

3. To list all the images, run the following command:
    ```bash
    docker images
    ```

4. To list all running docker container, run the following command:
    ```bash
    docker ps -a
    ```

## Basic Docker commands
1. To check the version of Docker, run the following command:
    ```bash
    docker -v
    ```

2. To check the version of Docker-compose, run the following command:
    ```bash
    docker-compose --version
    ```

3. To List all images, run the following command:
    ```bash
    docker images ls
    ```

4. To list all images ID only, run the following command:
    ```bash
    docker images ls -q
    ```

5. To check the networks on the machine:
    ```bash
    docker network ls
    ```

6. To remove a docker image, run the following command:
    ```bash
    docker rmi <image_id>
    ```

## Docker Compose
- Docker Compose is a tool for defining and running multi-container Docker applications. It uses a YAML file to configure the application's services, networks, and volumes. With a single command, you can start all services defined in the configuration.

### Example of 'docker-compose.yml'
```bash
version: '3'
services:
  web:
    image: image-name
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/code
    depends_on:
      - db
  db:
    image: postgres
    environment:
      POSTGRES_DB: example
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password

```

## Commands to use Docker Compose:
Build and start the services:
```bash
docker-compose up --build
```

Stop the services:
```bash
docker-compose down
```

Start the services without rebuilding:
```bash
docker-compose up
```

[Docker]: https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://docs.docker.com/
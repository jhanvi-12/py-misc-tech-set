<!--nginx logo -->
<br />
<div align="center">
   <img src="nginx.png" alt="Logo" width="120" height="100">

<h3 align="center">Nginx Guide.</h3>
</div>

# FastAPI Deployment Guide

This guide outlines the steps to deploy a FastAPI application using Gunicorn as the WSGI server and Nginx as a reverse proxy server on a Linux-based system.

## Prerequisites

- Python 3.x installed on your system.
- Nginx installed and configured.
- Systemd installed (for managing services).
- Basic knowledge of Linux command line.

## Setup

1. Clone your FastAPI project repository:

    ```bash
    git clone <your_repository_url>
    cd <your_project_directory>
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install required Python packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

## Deployment Steps

1. **Create a Systemd Service File:**

    Create a systemd service file (e.g., `fastapi.service`) in `/etc/systemd/system/` with the following content:

    ```ini
    [Unit]
    Description=FastAPI Application
    After=network.target

    [Service]
    User=<your_username>
    Group=<your_group>
    WorkingDirectory=<path_to_your_project_directory>
    ExecStart=/usr/local/bin/gunicorn --workers 5 --threads 2 --timeout 120 --bind unix:<your_sock_file_name> -m 007 -k uvicorn.workers.UvicornWorker main:app

    [Install]
    WantedBy=multi-user.target
    ```

    Replace `<your_username>` and `<your_group>` with your system's username and group, respectively. Replace `<path_to_your_project_directory>` with the absolute path to your FastAPI project directory and `<your_sock_file_name>` with your sock file name to bind workers that will start your FastAPI application on port sock file.

### let's break down each line in the provided configuration file along with the -k and -m options:

- [Unit]: This section defines metadata about the systemd unit (service) including its description and dependencies.
    1. **Description**=FastAPI Application: Describes the purpose or function of the service, which in this case is a FastAPI application.

    2. **After**=network.target: Specifies that this service should start after the network is up, ensuring network dependencies are met.


- [Service]: This section specifies how the service should be executed.
    1. **User=<your_username>**: Specifies the user account under which the service should run. Replace <your_username> with the desired username.

    2. **Group=<your_group>**: Specifies the group under which the service should run. Replace <your_group> with the desired group name.

    3. **WorkingDirectory=<path_to_your_project_directory>**: Sets the working directory for the service, which is the directory where the service will run. Replace <path_to_your_project_directory> with the actual path to your project directory.

    4. **ExecStart=/usr/local/bin/gunicorn --workers 5 --threads 2 --timeout 120 --bind unix:<your_sock_file_name> -m 007 -k uvicorn.workers.UvicornWorker main:app**: Defines the command to start the service. Here's the breakdown of options:

        * **--workers 5**: Specifies the number of worker processes. In this case, it's set to 5, meaning there will be 5 worker processes handling requests concurrently.

        * **--threads 2**: Specifies the number of worker threads per worker process. It's set to 2, meaning each worker process will handle up to 2 threads concurrently.

        * **--timeout 120**: Sets the maximum time a worker can take to respond to a request. In this case, it's set to 120 seconds.

        * **--bind unix:<your_sock_file_name>**: Specifies the socket file to bind to. Replace <your_sock_file_name> with the desired name of the socket file.

        * **-m 007**: Sets the umask for the worker processes. The umask controls the default permissions for newly created files. Here, it's set to 007, which means the permissions are set to 770 (rwxrwx---).

        * **-k uvicorn.workers.UvicornWorker**: Specifies the worker class to use. Here, it's using the UvicornWorker from the uvicorn package.

        * **main:app**: Specifies the Python module and the FastAPI application object to be run by Gunicorn. main is the Python module (main.py) and app is the FastAPI application object.


- [Install]: This section specifies when the service should be installed and started.
    
    1. **WantedBy**=multi-user.target: Specifies the target that this service should be installed into. multi-user.target is a systemd target that represents the normal boot-up state of the system where multiple users are logged in.

2. **Start and Enable the Service:**

    ```bash
    sudo systemctl start fastapi
    sudo systemctl enable fastapi
    sudo systemctl status fastapi
    ```

    This will start the FastAPI service and enable it to start on system boot.

3. **Configure Nginx as a Reverse Proxy:**

    Create a new server block in your Nginx configuration file (usually located in `/etc/nginx/sites-available/` or `/etc/nginx/conf.d/`) with the following content:

    ```nginx
    server {
        listen 80;
        server_name example.com;

        location / {
            proxy_pass http://127.0.0.1:8000;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }
    ```

    Replace `example.com` with your domain name or server IP address.

4. **Test Nginx Configuration and Restart Nginx:**

    Test the Nginx configuration for syntax errors:

    ```bash
    sudo nginx -t
    ```

    If the test is successful, restart Nginx:

    ```bash
    sudo systemctl restart nginx
    sudo systemctl enable nginx
    sudo systemctl status nginx
    ```

5. **Install Certbot and Create SSL Certificate:**

    Install Certbot:

    ```bash
    sudo apt-get update
    sudo apt-get install certbot python3-certbot-nginx
    ```

    After installing Certbot, run the following command to obtain an SSL certificate for your domain:

    ```bash
    sudo certbot --nginx -d example.com
    ```

    Replace `example.com` with your domain name. Certbot will automatically detect your Nginx configuration and configure SSL for your domain.

## Conclusion

Your FastAPI application should now be deployed and accessible via Nginx. You can further customize the Nginx configuration or Gunicorn settings based on your requirements.
# Software Load Balancing with Flask, Docker, and Nginx

This repository contains code for setting up software load balancing using Flask, Docker, and Nginx.

## Prerequisites

Ensure you have Docker installed on your system before proceeding.

## Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/sabarinathan1611/software_load_balancer.git
   cd software_load_balancer
   ```

2. Build and run the Docker containers:

   ```bash
   docker-compose up -d --build --scale app=4
   ```

This will build the Docker images and start the containers for Flask application and Nginx.

## Configuration

### Nginx Configuration

The Nginx configuration is specified in `nginx.conf` file. The configuration proxies requests from port 80 to the Flask application running on port 5000.

### Docker Compose Configuration

The `docker-compose.yml` file orchestrates the setup by defining services for the Flask application and Nginx. It ensures that Nginx depends on the Flask application so that Nginx can proxy requests to it.

### Flask Application

The Flask application resides in the `app` directory. It contains the following files:

- `wsgi.py`: Defines the Flask application and a route that returns the container ID for load balancing purposes.
- `requirements.txt`: Contains the dependencies required by the Flask application.
- `Dockerfile`: Specifies how to build the Docker image for the Flask application.

## Usage

Once the setup is complete and the Docker containers are running, you can access the load-balanced Flask application by visiting `http://localhost` in your web browser.

## Contributors

- [Sabarinathan V](https://github.com/sabarinathan1611)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

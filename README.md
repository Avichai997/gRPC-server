# MNIST gRPC Service and Client

## Overview

This project implements a gRPC service that streams MNIST dataset samples to a client. The service loads the MNIST data and sends each image with its label to the client via a gRPC stream.

## Setup and Running

### Prerequisites

- Docker
- Python 3.8 or higher
- gRPC tools for Python

#### Download and Install Docker

- **Windows**: Download Docker Desktop from [Docker's official website](https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe) and follow the installation instructions.
- **Mac**: Download Docker Desktop from [Docker's official website](https://desktop.docker.com/mac/stable/Docker.dmg) and follow the installation instructions.
- **Linux**: Follow the installation guide for your specific distribution from [Docker's official documentation](https://docs.docker.com/engine/install/#server).

#### Download and Install Python

- **Windows**: Download Python from [Python's official website](https://www.python.org/ftp/python/3.8.10/python-3.8.10-amd64.exe) and follow the installation instructions.
- **Mac**: Install Python using Homebrew:
  brew install python@3.8

- **Linux**: Use the package manager for your distribution:
  - **Ubuntu**:
    sudo apt update
    sudo apt install python3.8

  - **CentOS/RHEL**:
    sudo yum install python38

#### Install gRPC Tools for Python

1. Open a terminal or command prompt.
2. Run the following command to install gRPC tools:
   pip install grpcio grpcio-tools

### Installation

1. Clone the repository.
   git clone <repository-url>
   cd <repository-directory>

2. Install the required Python packages.
   pip install -r requirements.txt

### Running the Service and Client

1. Build and run the Docker containers.
   docker-compose up --build

2. The client will connect to the service and start receiving MNIST samples, displaying each image and its label.

### Testing

- To test the service, you can use any gRPC client to connect to `localhost:50051` and call the `GetTrainingSamples` method.
- Ensure the service is running and responding correctly by checking the logs in the Docker containers.

### Deployment

- The service and client are containerized using Docker, making it easy to deploy on any system with Docker installed.
- For production deployment, consider using orchestration tools like Kubernetes to manage the containers.

### Code Style

- The code adheres to PEP 8 standards for Python.
- Proper documentation and comments are included for clarity.

## Useful Links

- [gRPC Python Quickstart](https://grpc.io/docs/languages/python/quickstart/)
- [MNIST Dataset](http://yann.lecun.com/exdb/mnist/)
- [TensorFlow MNIST](https://www.tensorflow.org/datasets/catalog/mnist)

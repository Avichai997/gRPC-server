# MNIST gRPC Service and Client

## Overview

This project implements a gRPC service that streams MNIST dataset samples to a client. The service loads the MNIST data and sends each image with its label to the client via a gRPC stream.

## Setup and Running

### Prerequisites

- Docker
- Python 3.8 or higher
- gRPC tools for Python

### Installation

1. Clone the repository.
   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```
2. Install the required Python packages.
   ```sh
    pip install -r requirements.txt
   ```

### Running the Service and Client

1. Build and run the Docker containers.
    ```sh
    docker-compose up --build
   ```

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

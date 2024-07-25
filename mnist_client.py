import time
import grpc
import mnist_pb2
import mnist_pb2_grpc
import numpy as np
import cv2
import os
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def run():
    retries = 15
    while retries > 0:
        try:
            # Connect to the gRPC server
            with grpc.insecure_channel("mnist_service:50051") as channel:
                stub = mnist_pb2_grpc.MnistServiceStub(channel)
                request = mnist_pb2.DataRequest()

                # Stream samples from the server
                for idx, response in enumerate(stub.GetTrainingSamples(request)):
                    # Convert image bytes to numpy array
                    img = np.frombuffer(response.image, dtype=np.uint8).reshape(28, 28)
                    label = response.label

                    # Save the image
                    image_path = (
                        f"/app/mnist_images/mnist_image_{idx}_label_{label}.png"
                    )
                    os.makedirs(os.path.dirname(image_path), exist_ok=True)
                    cv2.imwrite(image_path, img)
                    logging.info(f"Saved MNIST Image: {image_path} with Label: {label}")

                    if idx >= 15:  # Limit the number of images saved to 16
                        break
            break
        except grpc.RpcError as e:
            logging.error(f"RPC error: {e}")
            retries -= 1
            time.sleep(5)

    if retries == 0:
        logging.error("Failed to connect to the server after multiple attempts")


if __name__ == "__main__":
    run()

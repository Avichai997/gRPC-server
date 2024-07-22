import time
import grpc
import mnist_pb2
import mnist_pb2_grpc
import numpy as np
import cv2
import os


def run():
    retries = 15
    while retries > 0:
        try:
            with grpc.insecure_channel("mnist_service:50051") as channel:
                stub = mnist_pb2_grpc.MnistServiceStub(channel)
                request = mnist_pb2.DataRequest()
                for idx, response in enumerate(stub.GetTrainingSamples(request)):
                    img = np.frombuffer(response.image, dtype=np.uint8).reshape(28, 28)
                    label = response.label
                    image_path = (
                        f"/app/mnist_images/mnist_image_{idx}_label_{label}.png"
                    )
                    os.makedirs(os.path.dirname(image_path), exist_ok=True)
                    cv2.imwrite(image_path, img)
                    print(f"Saved MNIST Image: {image_path} with Label: {label}")
                    if idx >= 15:  # Limit the number of images saved to 10
                        break
            break
        except grpc.RpcError as e:
            print(f"Retrying in 5 seconds: {e}")
            retries -= 1
            time.sleep(5)


if __name__ == "__main__":
    run()

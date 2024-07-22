import grpc
from concurrent import futures
import mnist_pb2
import mnist_pb2_grpc
import tensorflow as tf
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class MnistService(mnist_pb2_grpc.MnistServiceServicer):
    def GetTrainingSamples(self, request, context):
        try:
            # Load MNIST dataset
            (x_train, y_train), _ = tf.keras.datasets.mnist.load_data()

            # Stream samples to the client
            for img, label in zip(x_train, y_train):
                # Create a Sample message with image bytes and label
                sample = mnist_pb2.Sample(image=img.tobytes(), label=int(label))
                yield sample
        except Exception as e:
            logging.error(f"Error in GetTrainingSamples: {str(e)}")
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)


def serve():
    # Create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mnist_pb2_grpc.add_MnistServiceServicer_to_server(MnistService(), server)

    # Add insecure port for the server
    server.add_insecure_port("0.0.0.0:50051")
    server.start()
    logging.info("Server started on port 50051")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()

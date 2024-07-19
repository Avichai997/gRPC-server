import grpc
from concurrent import futures
import mnist_pb2
import mnist_pb2_grpc
import tensorflow as tf
import numpy as np


class MnistService(mnist_pb2_grpc.MnistServiceServicer):
    def GetTrainingSamples(self, request, context):
        try:
            (x_train, y_train), _ = tf.keras.datasets.mnist.load_data()
            for img, label in zip(x_train, y_train):
                sample = mnist_pb2.Sample(image=img.tobytes(), label=int(label))
                yield sample
        except Exception as e:
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mnist_pb2_grpc.add_MnistServiceServicer_to_server(MnistService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()

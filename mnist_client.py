import grpc
import mnist_pb2
import mnist_pb2_grpc
import numpy as np
import cv2

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = mnist_pb2_grpc.MnistServiceStub(channel)
        request = mnist_pb2.DataRequest()
        for response in stub.GetTrainingSamples(request):
            img = np.frombuffer(response.image, dtype=np.uint8).reshape(28, 28)
            label = response.label
            cv2.imshow('MNIST Image', img)
            print(f'Label: {label}')
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break

if __name__ == '__main__':
    run()

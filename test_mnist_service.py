import pytest
from concurrent import futures
import grpc
import mnist_pb2
import mnist_pb2_grpc
from mnist_service import MnistService


@pytest.fixture(scope="module")
def grpc_add_to_server():
    return mnist_pb2_grpc.add_MnistServiceServicer_to_server


@pytest.fixture(scope="module")
def grpc_servicer():
    return MnistService()


@pytest.fixture(scope="module")
def grpc_stub_cls(grpc_channel):
    return mnist_pb2_grpc.MnistServiceStub


def test_get_training_samples(grpc_stub):
    request = mnist_pb2.DataRequest()
    responses = grpc_stub.GetTrainingSamples(request)
    for response in responses:
        assert len(response.image) > 0
        assert isinstance(response.label, int)
        break  # Just check the first sample to avoid long test run

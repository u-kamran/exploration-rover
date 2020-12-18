import grpc

from protos.builds import sensor_pb2
from protos.builds import sensor_pb2_grpc

from google.protobuf.json_format import ParseDict
from google.protobuf.json_format import MessageToDict


HOST = 'localhost'
PORT = '50051'


class PrimaryController():

    def __init__(self, stub):
        self.stub = stub

    def activate_module(self):
        response = self.stub.ActivateModule(
            sensor_pb2.ActivateRequest(
                module_uuid='dca63b5c-a935-4b43-936e-0a469c844121'
            )
        )
        response = MessageToDict(response)
        print(
            f"\n[Activate Module] Received Response:"
            f"\nstatus code: {response['statusCode']}"
            f"\nmessage: {response['message']}\n"
        )

    def collect_soil_sample(self):
        message = ParseDict({
                "soil_sample_location": {
                    "x_coordinate": 10.1,
                    "y_coordinate": 20.2,
                    "z_coordinate": 30.3
                }
            },
            sensor_pb2.CollectRequest()
        )
        response = self.stub.CollectSoilSample(message)
        print(
            f"[Collect Soil Sample] Received Response:"
            f"\n{response}"
        )

    def analyze_request(self):
        request = sensor_pb2.AnalyzeRequest()
        request.detail = sensor_pb2.AnalyzeRequest.HIGH
        response = self.stub.AnalyzeSoilSample(request)
        print(
            f"[Analyze Request] Received Response:"
            f"\nmineral ratio: {response.minerals_ratio}"
            f"\nmoisture content: {response.moisture_content}"
            f"\norganic matter ratio: {response.organic_matter_ratio}\n"
        )

if __name__ == '__main__':
    with grpc.insecure_channel(f'{HOST}:{PORT}') as channel:
      stub = sensor_pb2_grpc.SoilSensorStub(channel)
      controller = PrimaryController(stub=stub)
      # send requests to the sensor
      controller.activate_module()
      controller.collect_soil_sample()
      controller.analyze_request()

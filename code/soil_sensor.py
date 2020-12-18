import grpc

from concurrent import futures

from protos.builds import sensor_pb2
from protos.builds import sensor_pb2_grpc

from google.protobuf.json_format import MessageToDict


MAXIMUM_WORKERS = 10
HOST = 'localhost'
PORT = '50051'


class SoilSensor(sensor_pb2_grpc.SoilSensorServicer):

    def ActivateModule(self, request, context):
        activate_request = MessageToDict(
            message=request,
            preserving_proto_field_name=True,
        )
        print(f"\n[Activate Module] Server Received:\n{activate_request}\n")
        return sensor_pb2.ActivateResponse(
            status_code=200,
            message="activated"
        )

    def CollectSoilSample(self, request, context):
        collect_request = MessageToDict(
            message=request,
            preserving_proto_field_name=True,
        )
        print(f"[Collect Soil Sample] Server Received:\n{collect_request}\n")
        return sensor_pb2.CollectResponse(
            success=True
        )

    def AnalyzeSoilSample(self, request, context):
        analyze_request = MessageToDict(
            message=request,
            preserving_proto_field_name=True,
        )
        print(f"[Analyze Soil Sample] Server Received:\n{analyze_request}\n")
        return sensor_pb2.AnalyzeResponse(
            minerals_ratio=0.7,
            moisture_content=0.55,
            organic_matter_ratio=0.2
        )

def launch_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=MAXIMUM_WORKERS))
    sensor_pb2_grpc.add_SoilSensorServicer_to_server(SoilSensor(), server)
    server.add_insecure_port(f'{HOST}:{PORT}')
    server.start()
    # to prevent early completion
    server.wait_for_termination()

if __name__ == '__main__':
    launch_server()

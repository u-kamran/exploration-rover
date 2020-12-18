## Exploration Rover

This repository contains sample code from an educational session that I taught on the topic of Protocol Buffers and gRPC.

The sample code simulates communication between a primary controller and a soil sensor module on an exploration rover.

## Example Output

The requests received by the soil sensor:

```
[Activate Module] Server Received:
{'module_uuid': 'dca63b5c-a935-4b43-936e-0a469c844121'}

[Collect Soil Sample] Server Received:
{'soil_sample_location': {'x_coordinate': 10.1, 'y_coordinate': 20.2, 'z_coordinate': 30.3}}

[Analyze Soil Sample] Server Received:
{'detail': 'HIGH'}
```

The responses received by the primary controller:

```
[Activate Module] Received Response:
status code: 200
message: activated

[Collect Soil Sample] Received Response:
success: true

[Analyze Request] Received Response:
mineral ratio: 0.7
moisture content: 0.55
organic matter ratio: 0.2
```

## Local Development

Note: the approach below uses `conda`, but it is not required. A virtual environment is recommended though.

1. Create a new virtual environment using conda:

```
conda create -n grpc python=3.7
```

2. Activate the virtual environment:

```
conda activate grpc
```

3. Install `grpcio` using conda or pip:

```
pip install grpcio
```

4. Install `grpcio-tools` using conda or pip:

```
pip install grpcio-tools
```

## Generating Artifacts

Navigate to the following folder:

```
cd protos
```

Run the following script:

```
./generate.sh
```

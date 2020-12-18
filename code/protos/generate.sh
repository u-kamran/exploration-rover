#!/bin/sh

echo "Generating gRPC Artifacts"

python -m grpc.tools.protoc \
    -I./source \
    --python_out=./builds \
    --grpc_python_out=./builds \
    ./source/*.proto

python -m lib2to3 ./builds/ -w -n
#!/bin/sh

protoc --proto_path ../protobufs --swift_out=proto-client-console ../protobufs/messages.proto
protoc --proto_path ../protobufs --grpc-swift_out=Client=true,Server=false:proto-client-console ../protobufs/messages.proto

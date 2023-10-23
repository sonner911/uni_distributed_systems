from concurrent import futures

import grpc

from messages_pb2 import (
    GetMessagesResponse,
    Message,
)
import messages_pb2_grpc


class MessagesService(messages_pb2_grpc.MessagesServicer):
    def GetMessages(self, request, context):
        return GetMessagesResponse(messages=[
            Message(id=1, body='First message'),
            Message(id=2, body='Second message'),
        ])


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    messages_pb2_grpc.add_MessagesServicer_to_server(
        MessagesService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()

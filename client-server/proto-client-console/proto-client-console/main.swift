import Foundation
import GRPC
import NIO

let eventLoopGroup = PlatformSupport.makeEventLoopGroup(loopCount: 1)
defer {
  try? eventLoopGroup.syncShutdownGracefully()
}

let channel = ClientConnection
    .insecure(group: eventLoopGroup)
    .connect(host: "localhost", port: 50051)
let client = MessagesAsyncClient(channel: channel)

let messagesResponse = try await client.getMessages(GetMessagesRequest())

print("Received messages:")
for message in messagesResponse.messages {
    print("#\(message.id): \(message.body)")
}

def Initialize(bitrate, messageHandler):
    global handler
    handler = messageHandler
    print("CAN - Emulator Initialization")
    print("CAN - Bitrate:", bitrate)

def Close():
    print("CAN - Thread Closed")

def Update():
    return

def Send(messageId, messageData, channel):
    global handler
    print("CAN - Sending Message:", hex(messageId), "On Channel", channel, "Data:", messageData)
    handler(messageId, messageData)
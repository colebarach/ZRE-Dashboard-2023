# Title: CANLib Library Interface
# Author: Cole Barach
# Date Created: 22.11.29
# Date Updated: 22.11.29
# Function: Frontend interface for the KVaser CANLib Python Library. Provides a generic interface for the library interchangeable with
#   interfaces to similar CAN libraries.

# Libraries
import canlib
from canlib import canlib
from canlib import Frame
from canlib.canlib import ChannelData

ChannelBitrate = {
    10000 : canlib.canBITRATE_10K,
    50000 : canlib.canBITRATE_50K,
    62000 : canlib.canBITRATE_62K,
    83000 : canlib.canBITRATE_83K,
    100000 : canlib.canBITRATE_100K,
    125000 : canlib.canBITRATE_125K,
    250000 : canlib.canBITRATE_250K,
    1000000 : canlib.canBITRATE_1M
}

def Initialize(bitrateIn, messageHandler):
    global can0
    global can1
    global handler
    handler = messageHandler
    bitrate = ChannelBitrate[bitrateIn]
    print("CAN - OS: Windows")
    print("CAN - Using Kvaser Canlib Library")
    print("CAN - Canlib Version:", canlib.dllversion())
    can0 = OpenChannel(0, bitrate=bitrate)
    print("CAN - Opened Channel 0. Bitrate:", bitrateIn)
    can1 = OpenChannel(1, bitrate=bitrate)
    print("CAN - Opened Channel 1. Bitrate:", bitrateIn)

def Update():
    global can0
    global can1
    global handler
    # Read Channel 0
    try:
        frame = can0.read()
        handler(frame.id, frame.data)
    except (canlib.canNoMsg) as ex:
        pass # No Message
    except (canlib.canError) as ex:
         # Error Frame
        print("CAN - Error:", ex)
    
    # Read Channel 1
    try:
        frame = can0.read()
        handler(frame.id, frame.data)
    except (canlib.canNoMsg) as ex:
        pass # No Message
    except (canlib.canError) as ex:
        # Error Frame
        print("CAN - Error:", ex)

def Close():
    global can0
    global can1
    CloseChannel(can0)
    CloseChannel(can1)

def OpenChannel(channelId, openFlags=canlib.canOPEN_ACCEPT_VIRTUAL, bitrate=canlib.canBITRATE_500K, bitrateFlags=canlib.canDRIVER_NORMAL):
    channel = canlib.openChannel(channelId, openFlags)
    print("CAN - Device:", ChannelData(channelId).channel_name, "- ID:", ChannelData(channelId).card_upc_no)
    channel.setBusOutputControl(bitrateFlags)
    channel.setBusParams(bitrate)
    channel.busOn()
    return channel

def CloseChannel(channel):
    print("CAN - Device Closed:", ChannelData(channel.index).channel_name)
    channel.busOff()
    channel.close()

def Send(messageId, messageData, channel):
    global can0
    global can1
    print("CAN - Sending Message:", hex(messageId), " Data:", messageData)
    messageFrame = Frame(messageId, messageData, len(messageData), canlib.MessageFlag.STD)
    if(channel == 0): can0.write(messageFrame)
    if(channel == 1): can1.write(messageFrame)
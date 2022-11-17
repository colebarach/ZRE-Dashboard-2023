# Libraries
from canlib import canlib
from canlib import Frame
from canlib.canlib import ChannelData

# Include
import can
import config

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

def Initialize():
    global canMainRx
    global canMainTx
    bitrate = ChannelBitrate[config.CAN_BITRATE]
    print("CAN - OS: Windows")
    print("CAN - Using Kvaser Canlib Library")
    print("CAN - Canlib Version:", canlib.dllversion())
    print("CAN - Channel bitrate:", config.CAN_BITRATE)
    canMainRx = OpenChannel(0, bitrate=bitrate)
    canMainTx = OpenChannel(1, bitrate=bitrate)

def Update():
    global canMainRx
    global canMainTx
    try:
        frame = canMainRx.read()
        if(frame.id == config.CAN_ID_INPUT_PEDALS): can.HandleInputPedals(frame.data)
        if(frame.id == config.CAN_ID_DATA_MOTOR):   can.HandleDataMotor(frame.data)
        if(frame.id == config.CAN_ID_DATA_PEDALS):  can.HandleDataPedals(frame.data)
        if(frame.id == config.CAN_ID_STATUS_ECU):   can.HandleStatusEcu(frame.data)
    except (canlib.canNoMsg) as ex:
        pass
    except (canlib.canError) as ex:
        print("CAN - Error:", ex)

def Close():
    global canMainRx
    global canMainTx
    CloseChannel(canMainRx)
    CloseChannel(canMainTx)

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

def Send(messageId, messageData, main=True):
    global canMainRx
    global canMainTx
    print("CAN - Sending Message:", hex(messageId), " Data:", messageData)
    if(main):
        messageFrame = Frame(messageId, messageData, len(messageData), canlib.MessageFlag.STD)
        canMainTx.write(messageFrame)
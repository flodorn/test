#!/usr/bin/env python3
import asyncio
import logging
import os
import struct

from examples.helper import get_commandline
from pymodbus.datastore import (
    ModbusSequentialDataBlock,
    ModbusServerContext,
    ModbusSlaveContext,
    ModbusSparseDataBlock,
)
from pymodbus.device import ModbusDeviceIdentification

# --------------------------------------------------------------------------- #
# import the various client implementations
# --------------------------------------------------------------------------- #
from pymodbus.server import (
    StartAsyncSerialServer,
    StartAsyncTcpServer,
    StartAsyncTlsServer,
    StartAsyncUdpServer,
)
from pymodbus.version import version
import codecs

hex = codecs.encode(b"S", "hex")

_logger = logging.getLogger()




#result = "S".encode()

dataExport = struct.pack(">ss", hex)

#dataExport = struct.pack(">c", result)

#b = bytes(data, 'utf-8')

#hex(ord("c"))

#print(type(dataExport))
#print(result)
print(dataExport)
print(hex)


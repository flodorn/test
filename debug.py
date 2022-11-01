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


_logger = logging.getLogger()


data="S"

result = data.encode()
dataExport = struct.pack(">s", result)

#dataExport = struct.pack(">c", result)

#b = bytes(data, 'utf-8')

print(type(dataExport))
print(dataExport)

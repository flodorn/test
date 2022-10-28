from pymodbus.client import AsyncModbusSerialClient

async def run():
    client = AsyncModbusSerialClient("/dev/ttyUSB0")

    await client.connect()
    ...
    await client.close()

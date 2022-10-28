from pymodbus.client import AsyncModbusSerialClient

async def run():
    client = AsyncModbusSerialClient("dev/serial0")

    await client.connect()
    ...
    await client.close()

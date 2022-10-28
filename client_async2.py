from pymodbus.client import AsyncModbusSerialClient

async def run():
    client = AsyncModbusSerialClient("/dev/ttyUSB0")

    await client.connect()
    rr = await async_client.read_coils(0x01)
    await async_client.write_coil(0x01, values)
    print(values)
    await client.close()

    

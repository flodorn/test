from pymodbus.client import AsyncModbusSerialClient

async def run():
    client = AsyncModbusSerialClient("/dev/ttyUSB0", baudrate: int = 19200)
    
    
	
    await client.connect()
    rr = await async_client.read_coils(0x03)
    await async_client.write_coil(0x03, rr)
    print(values)
    await client.close()

    

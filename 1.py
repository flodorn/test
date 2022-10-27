#!/usr/bin/env python3
import minimalmodbus
import serial

ser = serial.Serial('/dev/ttyUSB0')  # open serial port
print(ser.name)         # check which port was really used




instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1)  # port name, slave address (in decimal)

## Read temperature (PV = ProcessValue) ##
temperature = instrument.read_register(289, 1)  # Registernumber, number of decimals
print(temperature)

## Change temperature setpoint (SP) ##
NEW_TEMPERATURE = 95
instrument.write_register(24, NEW_TEMPERATURE, 1)  # Registernumber, value, number of decimals for storage



ser.close()             # close port

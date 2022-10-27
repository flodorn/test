import serial



with serial.Serial('/dev/ttyUSB0', 9600, timeout=10) as ser:
	print(ser.name)         # check which port was really used
	x = ser.read()          # read one byte
	s = ser.read(10)        # read up to ten bytes (timeout)
	line = ser.readline()   # read a '\n' terminated line
	print(x)
	print(s)
	print(line)

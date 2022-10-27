import serial



with serial.Serial('/dev/ttyUSB0', 9600, timeout=1) as ser:
	print(ser.name)         # check which port was really used
	x = ser.read()          # read one byte
	s = ser.read(5)        # read up to ten bytes (timeout)
	line = ser.readline()   # read a '\n' terminated line
	lines = ser.readlines(5)   # read multiple '\n' terminated lines (timeout)
	print(x)
	print(s)
	print(line)
	print(lines)

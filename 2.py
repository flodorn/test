import serial

with serial.Serial('/dev/ttyUSB0', 9600, timeout=1) as ser:
	f = open("log.txt", "a")
	
	print(ser.name)         # check which port was really used
	x = ser.read()          # read one byte
	s = ser.read(5)        # read up to ten bytes (timeout)
	line = ser.readline(5)   # read a '\n' terminated line (timneout)
	lines = ser.readlines(5)   # read multiple '\n' terminated lines (timeout)
	
	print(x)
	f.write(x)
	print(s)
	f.write(s)
	print(line)
	f.write(line)
	print(lines)
	f.write(lines)
	f.close()

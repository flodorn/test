import serial

with serial.Serial(port='/dev/ttyUSB0', baudrate=9600, bytesize=serial.EIGHTBITS, timeout=5) as ser:
	
	f = open("log.txt", "a")
	
	print(ser.name)         # check which port was really used
	x = ser.read()          # read one byte
	s = ser.read(5)        # read up to ten bytes (timeout)
	line = ser.readline(10)   # read a '\n' terminated line (timneout)
	#lines = ser.readlines(5)   # read multiple '\n' terminated lines (timeout)
	
	print(x)
	f.write(str(x))
	print(s)
	f.write(str(s))
	print(line)
	f.write(str(line))
	#print(lines)
	#f.write(str(lines))
	
	f.close()
	serial.close()

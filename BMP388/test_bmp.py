import bmp388library

bmp = bmp388library.DFRobot_BMP388_I2C(0x77)

while True:
	temperature = bmp.readTemperature()
	pressure = bmp.readPressure()

	print(f"T: {temperature}")
	print(f"P: {pressure}")


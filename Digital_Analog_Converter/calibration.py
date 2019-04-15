import Adafruit_MCP4725

dac = Adafruit_MCP4725.MCP4725()

zero = 4095;
zero = int(zero)
dac.set_voltage(zero)

print("calibration")

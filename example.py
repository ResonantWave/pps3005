from pps3005 import PPS3005

power_supply = PPS3005('COM14', 25, 2) # initialize PSU on COM1, 25V max and 2A max.

print('Is power supply output on? {}'.format(power_supply.is_on()))
print('Turn power supply output on')
power_supply.turn_on()
print('Is power supply output on? {}'.format(power_supply.is_on()))
print('Set power supply voltage to 20V')
power_supply.set_voltage(20)
print('Close power supply port')
del power_supply

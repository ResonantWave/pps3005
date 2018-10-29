from serial import Serial

class PPS3005:
    volt_frame_set = 'VSET1:{}'
    volt_frame_get = 'VOUT1?'

    amp_frame_set = 'ISET1:{}'
    amp_frame_get = 'IOUT1?'

    on_frame = 'OUT1'
    off_frame = 'OUT0'
    
    def set_voltage(self, volts):
        self.ser.write(self.volt_frame_set.format(volts))

    def get_voltage(self):
        self.ser.write(self.volt_frame_get)
        return self.ser.read(5)

    def set_amps(self, amps):
        self.ser.write(self.amp_frame_set.format(amps))

    def get_amps(self):
        self.ser.write(self.amp_frame_get)
        return self.ser.read(5)

    def turn_on(self):
        self.ser.write(self.on_frame)
        self.on = True

    def turn_off(self):
        self.ser.write(self.off_frame)
        self.on = False

    def is_on(self):
        return self.on

    def __init__(self, com_port, max_v = 30, max_a = 5):      
        self.max_volts = max_v if max_v < 30 else 30
        self.max_amps = max_a if max_a < 5 else 5
        self.on = False
        self.ser = Serial(com_port, 9600)
        print('PPS3005 successfully initialised on ' + com_port)
        print('Max voltage: {}V'.format(self.max_volts))
        print('Max amps: {}A'.format(self.max_amps))

    def __del__(self):
        self.ser.close()
        print('Successfully closed PSU port')

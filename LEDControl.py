import time


class LEDControl:
    
    MODEMAX = 3
    DIMMAX = 9
    SPEEDMAX = 2
    COLORMAX = 6
    
    RED = 0
    GRN = 1
    BLU = 2

    def __init__(self):
        self.mode = 0
        self.speed = 0
        self.color = 0
        self.dim = 5
        self.led = [0, 0, 0]
        self.switchflag = 0

    def fadeup(self):
        for i in range(len(self.led)):
            self.led[i] += 1
            if self.led[i] > 100:
                self.led[i] = 0
        time.sleep(0.01)


    ########### CONTROL FUNCTIONS ###########
    def changemode(dir):
        if dir == 1:
            self.mode += 1
            if self.mode > LEDControl.MODEMAX:
                self.mode = 0
        else:
            self.mode -= 1
            if self.mode < 0:
                self.mode = LEDControl.MODEMAX
    
    def changespeed(dir):
        if dir == 1:
            self.speed += 1
            if self.speed > LEDControl.SPEEDMAX:
                self.speed = 0
        else:
            self.speed -= 1
            if self.speed < 0:
                self.speed = LEDControl.SPEEDMAX
    
    def changedim(dir):
        if dir == 1:
            self.dim += 1
            if self.dim > LEDControl.DIMMAX:
                self.dim = 0
        else:
            self.dim -= 1
            if self.dim < 0:
                self.dim = LEDControl.DIMMAX
                
    def changecolor(dir):
        if dir == 1:
            self.color += 1
            if self.color > LEDControl.COLORMAX:
                self.color = 0
        else:
            self.color -= 1
            if self.color < 0:
                self.color = LEDControl.COLORMAX
            
                
        
    ########### HELPER FUNCTIONS ###########
    
    # Function that converts 0-100 to 0-65536 for use from PWM
    def pwmconvert(self, x):
        return int(x * 65536 * self.dim / 4000)

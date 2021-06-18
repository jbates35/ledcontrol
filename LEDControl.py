import time


class LEDControl:
    
    PATTERN_MAX = 3
    DIM_MAX = 9
    SPEEDMAX = 2
    COLORMAX = 6
    
    RED = 0
    GRN = 1
    BLU = 2

    def __init__(self):
        self.pattern = 0
        self.speed = 0
        self.color = 0
        self.dim = 5
        self.led = [0, 0, 0]
        self.switch_flag = 0

    def fadeup(self):
        for i in range(len(self.led)):
            self.led[i] += 1
            if self.led[i] > 100:
                self.led[i] = 0
        time.sleep(0.01)


    ########### CONTROL FUNCTIONS ###########
    def changeval(self, x, max, dir):
    if dir == 1:
        return x+1 if x < max else 0
    else:
        return x-1 if x > 0 else max
    
    
    def changemode(self, dir):
        self.changeval(self.mode, LEDControl.MODEMAX, dir)
    
    def changespeed(self, dir):
        self.changeval(self.speed, LEDControl.SPEEDMAX, dir)
    
    def changedim(self, dir):
        self.changeval(self.dim, LEDControl.DIMMAX, dir)
                
    def changecolor(self, dir):
        self.changeval(self.color, LEDControl.COLORMAX, dir)
            
                
        
    ########### HELPER FUNCTIONS ###########
    
    # Function that converts 0-100 to 0-65536 for use from PWM
    def pwmconvert(self, x):
        return int(x * 65536 * self.dim / 4000)

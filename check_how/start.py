import numpy as np
import matplotlib.pyplot as plt
import time


class Robot:
    def __init__(self,acc,width,height):
        self.V=0
        self.th=0
        self.acc=acc
        self.time=time.time()

    def move(self,th):
        x=self.V*np.cos(th)
        y=self.V*np.sin(th)
        return x,y

    def change_v(self):
        self.V=self*self.acc*(time.time()-self.time)
        
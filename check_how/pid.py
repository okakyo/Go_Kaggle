import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


class PID:
    def __init__(self,ideal=0.5,kp=0.3,ki=0.1,kd=0.02,setTime=1.0):
        
        self.kp=kp
        self.ki=ki
        self.kd=kd
        self.ideal=ideal
        self.setTime=setTime

        self._diff=0
        self.sum=0
    
    def different(self,x):
        self._diff=x-self.ideal
    
    def Proportial(self):
        response=self.kp*self._diff
        return response

    def Integral(self):
        self.sum+=self._diff*self.setTime
        return self.ki*self.sum

    def Diffentional(self):
        data=self._diff/self.setTime
        return self.kd*data

    def PID(self,data):
        response=[]
        for x in data:
            self.different(x)
            response.append(self.Proportial()+self.Integral()+self.Diffentional())
        return response

    def __call__(self,data):
        return self.PID(data)


if __name__=="__main__":
    data=[1.0,3.2,5.0,7.4,6.5,7.4,3.5,4.3,2.5]
    pid=PID()
    for ideal in pid(data):
        print("実測値：{}".format(ideal))


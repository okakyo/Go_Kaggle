import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


class PID:
    def __init__(self,ideal=1,kp=0.3,ki=0.1,kd=0.02,setTime=1.0):
        
        self.kp=kp
        self.ki=ki
        self.kd=kd
        self.ideal=ideal
        self.setTime=setTime

        self._diff=0
        self.sum=0
    
    def different(self,x):
        self._diff=self.ideal-x
    
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
        self.different(data)
        return self.Proportial()+self.Integral()+self.Diffentional()
        

    def __call__(self,firstInput):
        return self.PID(firstInput)


if __name__=="__main__":
    countChallnge=[]
    outputData=[]
    x=np.random.rand()
    pid=PID()
    for i in range(100):
        y=pid(x)
        countChallnge.append(i)
        outputData.append(pid(x))
        print(y)
        x=y
    plt.plot(countChallnge,outputData)
    plt.show()

    
       
 


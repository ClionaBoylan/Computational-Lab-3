import numpy as np
import matplotlib.pyplot as plt
import time as tittymilk

starttime=tittymilk.time()
D=10**-(3.5)
m=(2*10**3)*(4.0/3.0)*np.pi*((D)/2)**3
length=3000
g=9.8
B=1.6*(10**-4)
C=0.25
c=C*(D**2)
b=B*D
dt=0.001
vy=[1.0]
vyquad=[vy[0]]
vx=[1.0]
vxquad=[vx[0]]
sy=[0.0]
syquad=[sy[0]]
sx=[0.0]
sxquad=[sx[0]]

number=10
powers=np.linspace(-5.0,1.5,number)
i=0
diameters=[]
while i<number:
    diameters.append(10**powers[i])
    i+=1

i=0
masses=[]
while i<number:
    masses.append((2*10**3)*(4.0/3.0)*np.pi*((diameters[i])/2)**3)
    i+=1


runno=1000
length=30000000
thetaarray=np.linspace(0,np.pi/2,runno)
v=1
dt=0.0001
ranges=[]
angles=[]
k=0
while k<number:
    R=[]
    D=diameters[k]
    m=(2*10**3)*(4.0/3.0)*np.pi*((D)/2)**3
    b=B*D
    def dvy(v1,v2):
        return -g*dt-(c/m)*np.sqrt(v1**2+v2**2)*dt*v2
    def dvx(v1,v2):
        return -(c/m)*np.sqrt(v1**2+v2**2)*dt*v1
    j=0
    while j<runno:
        vx=[np.cos(thetaarray[j])*v]
        vy=[np.sin(thetaarray[j])*v]
        sx=[0.0]
        sy=[0.0]
        i=0
        while i<length-1:
            vy.append(vy[i]+dvy(vx[i],vy[i]))
            vx.append(vx[i]+dvx(vx[i],vy[i]))
            sy.append(sy[i]+vy[i]*dt)
            sx.append(sx[i]+vx[i]*dt)
            if sy[i]<0:
                time=i
                break
            i+=1
        R.append(sx[time])
        if R[j]<R[j-1] and j!=0:
            ranges.append(R[j-1])
            angles.append(thetaarray[j-1])
            break
        j+=1
    print('Overall:',((k+1)/number)*100)
    k+=1

endtime=tittymilk.time()-starttime
print(endtime/60,'mins')


plt.scatter(masses,angles,c=angles,s=0.5,cmap='rainbow')
plt.xscale('log')
plt.xlabel('Masses (kg)')
plt.ylabel('Optimum Angle (rad)')
plt.savefig('BigGay.pdf')

plt.scatter(masses[1:],angles)
plt.xscale('log')
import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

diameters=[0.09847450218426967,9.847450218426972e-05,0.000984745021842697,0.009847450218426968]
masses=[1.0,1e-9,1e-6,1e-3]
D1=0.09847450218426967
D2=9.847450218426972e-05
D3=0.000984745021842697
D4=0.009847450218426968
m1=1.0
m2=1e-9
m3=1e-6
m4=1e-3
dt=0.0001


D=0.04570781497340833
m=(2*10**3)*(4.0/3.0)*np.pi*((D)/2)**3
length=1000000
g=9.8
B=1.6*(10**-4)
C=0.25
b=B*D
c=C*D**2
dt=0.0001
v0=10
thetas=[np.pi/4, np.pi/8, 3*np.pi/8]

n=0
while n<len(thetas):
    k=0
    while k<len(diameters):
        v0=5
        theta=np.pi/4
        vy=[v0*np.sin(thetas[n])]
        vyquad=[vy[0]]
        vy2=[vy[0]]
        vx=[v0*np.cos(thetas[n])]
        vxquad=[vx[0]]
        vx2=[vx[0]]
        sy=[0.0]
        syquad=[sy[0]]
        sy2=[sy[0]]
        sx=[0.0]
        sxquad=[sx[0]]
        sx2=[sx[0]]
        D=diameters[k]
        m=(2*10**3)*(4.0/3.0)*np.pi*((D)/2)**3
        b=B*D
        c=C*D**2
        def dvy(v):
            return -g*dt-(b/m)*v*dt
        
        def dvy2(vx,vy):
            return (-g-(c/m)*np.sqrt(vx**2+vy**2)*vy)*dt
        
        def dvx2(vx,vy):
            return -(c/m)*np.sqrt(vx**2+vy**2)*vx*dt
        
        def dvx(v):
            return -(b/m)*v*dt
        i=0
        while i<length-1:
            vy.append(vy[i]+dvy(vy[i]))
            vx.append(vx[i]+dvx(vx[i]))
            vyquad.append(vyquad[i]-g*dt)
            vxquad.append(vxquad[0])
            vy2.append(vy2[i]+dvy2(vx2[i],vy2[i]))
            vx2.append(vx2[i]+dvx2(vx2[i],vy2[i]))
            sy.append(sy[i]+vy[i]*dt)
            sx.append(sx[i]+vx[i]*dt)
            syquad.append(syquad[i]+vyquad[i]*dt)
            sxquad.append(sxquad[i]+vxquad[i]*dt)
            sy2.append(sy2[i]+vy2[i]*dt)
            sx2.append(sx2[i]+vx2[i]*dt)
            if syquad[i]<0:
                break
            i+=1
        
        plt.scatter(0,0,label='Vacuum',c='blue',s=1e-9)
        plt.scatter(0,0,label='Quadratic Air Resistance',c='red',s=1e-9)
        plt.scatter(0,0,label='Linear Air Resistance',c='green',s=1e-9)
        plt.scatter(sx,sy, c=sy,cmap='Greens',s=0.5)
        plt.scatter(sx2,sy2,c=sy2,cmap='Reds',s=0.5)
        plt.scatter(sxquad,syquad, c=syquad,cmap='Blues',s=0.5)
        plt.legend(markerscale=200000.0)
        plt.ylim(0,1.1*max(syquad))
        plt.title(r'm=%skg, $v_0$=%sm/s, $\theta$=%s$\pi$' %(masses[k],v0,Fraction(thetas[n]/np.pi)))
        plt.savefig('%s %s.pdf' %(n,k))
        plt.show()
        k+=1
    n+=1
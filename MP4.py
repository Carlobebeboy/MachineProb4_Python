import matplotlib.pyplot as plot
import numpy as np
import math as mt

def MP4(height, velocity, angle, Ax, Ay):
    
    if height < 0:
        raise NameError('Error! Input Height')
    elif Ay == 0:
        raise NameError('Error! There would be no Free Fall')
        
    
    deg = mt.radians(angle)
    sind = mt.sin(deg)
    cosd = mt.cos(deg)
                   
           
    T = (mt.sqrt(abs((velocity*sind)**2-2*Ay*height)) - velocity*sind)/Ay
    
    if T <= 0:
        
        T = (-mt.sqrt(abs((velocity*sind)**2-2*Ay*height)) - velocity*sind)/Ay
        
    t =  np.arange(0,T,0.1)
    
    y = height + velocity*sind*t+(1/2)*Ay*t**2
    x = velocity*cosd*t+(1/2)*Ax*t**2
    
        
    plot.plot(x,y,'-r')
    plot.grid()
    plot.title('Projectile Trajectory')
    plot.xlabel('Horizontal Distance')
    plot.ylabel('Vertical Distance')
    plot.show()
    
           
    
        
        
    
    
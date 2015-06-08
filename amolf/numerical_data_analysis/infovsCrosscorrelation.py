#compute information vs cross correlation

from numpy import*
from scipy import *
from matplotlib import pyplot as plt











T=24.
w=2*pi/T
phi=pi/2.
r=200.
A=50.
dt=0.05

def infoCross(a):
		
	fi=arange(0,pi,0.1)
	t=arange(0,T,dt)
	XM=arange(150,320)
	YM=arange(150,320)


	c=a


	infotot=[]
	cor=arange(-0.99,1,0.05)
	for b in cor:
		
		infoA=[]
		for phi in fi:
			integ=[]
			XYind=0
			pxy=[]
			for x in XM:
				pxy.append([])
				for y in YM:
					
					
					C=a*c-b**2
					Z=1/(sqrt((2*pi)**2*C)*T)
					
					pxy[XYind].append(dt*sum(Z*exp(-0.5*(1/C)*(a*(x-A*sin(w*t)-r)**2+c*(y-A*sin(w*t+phi)-r)**2+2*b*((x-A*sin(w*t)-r)*(y-A*sin(w*t+phi)-r))))))
					
					integ.append(sum(Z*(exp(-0.5*(1/C)*(a*(x-A*sin(w*t)-r)**2+c*(y-A*sin(w*t+phi)-r)**2+2*b*((x-A*sin(w*t)-r)*(y-A*sin(w*t+phi)-r))))) * (-0.5*(1/C)*(a*(x-A*sin(w*t)-r)**2+c*(y-A*sin(w*t+phi)-r)**2+2*b*((x-A*sin(w*t)-r)*(y-A*sin(w*t+phi)-r)))+0.5*	log((2*pi)**2*C))))
					
					

				XYind=XYind+1 
				
			f_pxy=array(pxy)
			fl_pxy=log(f_pxy)
			ent=-f_pxy*fl_pxy
			ent[isnan(ent)]=0
			infoA.append(ent.sum()-(sum(integ)*dt))          
			
			
			
		infotot.append(infoA)
		

		
	return infotot




























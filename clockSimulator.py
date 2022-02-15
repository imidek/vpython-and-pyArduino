from vpython import *
import numpy as np

clockR = 2
clockT = clockR/10
majorTickL = clockR/7
majorTickT = 2*np.pi*clockR/400
majorTickW = clockT*1.2

minorTickL = clockR/12
minorTickT = 2*np.pi*clockR/600
minorTickW = clockT*1.2

arLenM = clockR
arLenH = arLenM*.75
arShaftM = arLenM/20
arShaftH = arShaftM*1.2

hour = arrow(axis=vector(0,1,0), color=color.orange, length=arLenH, shaftwidth=arShaftH*2,
pos=vector(0,0,clockT) )

minute = arrow(axis=vector(0,1,0), color=color.red, length=arLenM, shaftwidth=arShaftM,
pos=vector(0,0,clockT) )

for angle in np.linspace(0,2*np.pi,13):
    majorTick=box(axis=vector(clockR*np.cos(angle),clockR*np.sin(angle),0),
    color=color.black,length=majorTickL,width=majorTickW,height=majorTickT,
    pos=vector((clockR-majorTickL/2)*np.cos(angle),(clockR-majorTickL/2)*np.sin(angle),0))

for angle in np.linspace(0,2*np.pi,61):
    minorTick=box(axis=vector(clockR*np.cos(angle),clockR*np.sin(angle),0),
    color=color.black,length=minorTickL,width=minorTickW,height=minorTickT,
    pos=vector((clockR-minorTickL/2)*np.cos(angle),(clockR-minorTickL/2)*np.sin(angle),0))


clockFace = cylinder(axis=vector(0,0,1),radius=clockR,length=clockT,
 color=vector(0,1,.8),pos=vector(0,0,-clockT/2))

minuteD=(np.pi*2)/360
hourD=minuteD/12
thetaH = np.pi/2
thetaM = np.pi/2

while True: 
    rate(50)
    thetaM = thetaM - minuteD 
    thetaH = thetaH - hourD
    minute.axis=vector(np.cos(thetaM)*arLenM,np.sin(thetaM)*arLenM,0)
    minute.length=arLenM
    hour.axis=vector(np.cos(thetaH)*arLenH,np.sin(thetaH)*arLenH,0)
    hour.length=arLenH


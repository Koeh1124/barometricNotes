import math
from operator import truediv

#Sources
#https://www.mide.com/air-pressure-at-altitude-calculator
#https://www.engineeringtoolbox.com/standard-atmosphere-d_604.html

#Standards

#Prusure and temp are using ISA standards
#static prusre at sea level [Pa]
Pb = 1013200
#standard temp at sea level [K]
Tb = 288

#Standard temp. lapse rate [K/m]
Lb = -0.0065

#universal gas constant [N*m/mol*K]
R = 8.31432

#gravitational accelration constant [m/s^2]
go = 9.80665

#molar Mass of Earth's air [kg/mol]
M = 0.0289644

#height at the bottom of our atmospheric layer
hb = 0

#give a prusure in Pa we can calculate a height
def calcHeight(P):
    global Pb,Tb,Lb,R,go,M,hb
    h = hb + ((Tb/Lb)*((pow((P/Pb),((-R*Lb)/(go*M))))-1))
    print(h)

run = True
while(run):
    ui = input("Input a prusure in Pa or type q to quit")
    if ui == "q":
        run = False
    elif(not(ui.isalpha())):
        calcHeight(float(ui))

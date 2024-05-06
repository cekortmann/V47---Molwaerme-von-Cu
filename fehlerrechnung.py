import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import csv
from numpy import sqrt
import scipy.constants as const
from scipy.optimize import curve_fit                        # Funktionsfit:     popt, pcov = curve_fit(func, xdata, ydata) 
from uncertainties import ufloat                            # Fehler:           fehlerwert =  ulfaot(x, err)
from uncertainties import unumpy as unp 
from uncertainties.unumpy import uarray                     # Array von Fehler: fehlerarray =  uarray(array, errarray)
from uncertainties.unumpy import (nominal_values as noms,   # Wert:             noms(fehlerwert) = x
                                  std_devs as stds)  

m = 0.342
M = 0.0634
Mm= M/m
kappa=140*10**9
V_m=7.11*10**(-6)

def T(R):
    return (0.00134*R**2+2.296*R-243.02+273.15)

Acu= unp.uarray([158.1,153.4,153.6,151.9,153.0,153.6,153.8,154.0,154.3,154.4,154.5,154.7,154.7,154.8,154.8,154.6,155.0,155.0,155.1,155.1,155.2,155.2,155.3,155.3,155.4,155.3,155.3],[0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1])*10**(-3)                    #Spannung Heizspirale cu
Vcu= unp.uarray([16.56,16.09,16.11,15.92,16.07,16.16,16.19,16.22,16.27,16.29,16.30,16.31,16.33,16.34,16.34,16.36,16.37,16.37,16.38,16.38,16.39,16.39,16.39,16.39,16.39,16.38,16.38],[0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01])


R1  = unp.uarray([24.9,27.3,28.6,29.2,33.3,37.8,40.4,42.7,47.5,50.0,52.3,55.1,57.6,59.6,61.0,64.1,67.2,69.9,73.8,77.0,80.0,83.6,87.4,91.5,96.0,100.0,104.0],[0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1])
t1 = unp.uarray([0,180,309,360,730,1160,1425,1674,2190,2454,2697,2996,3288,3606,3708,4042,4369,4712,5225,5612,5980,6429,7008,7440,8034,8541,9032],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
n_spalten = 27
nullen = np.zeros(n_spalten)
T1 = unp.uarray(nullen,nullen)

i=0

while i<27:
    T1[i]=T(R1[i])
    i=i+1

print(T(R1[2]))
#print(len(Vcu))
#print(len(t1))
print(T(R1[len(R1)-1]))
print(T(111))
dt= unp.uarray([0,180,309,360,730,1160,1425,1674,2190,2454,2697,2996,3288,3606,3708,4042,4369,4712,5225,5612,5980,6429,7008,7440,8034,8541,9032],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
j=1
while j<27:
    dt[j]=t1[j]-t1[j-1]
    j=j+1

#print(T1)



dT= unp.uarray(nullen,nullen)
k=1

while k<27:
    dT[k]=T1[k]-T1[k-1]
    k=k+1
dT[0]=1

i=0
def E(U,I,dt):
        return U*I*dt
        
E = E(Vcu,Acu,dt)

def C_p(Mm,E,dT):
    return E/dT
uC_p=C_p(Mm,E,dT)*Mm

def alpha1(T):
   return ((T-70)*0.15+7)*10**(-6)

alpha =unp.uarray(nullen,nullen)
uC_v=unp.uarray(nullen,nullen)

q=0
while q<26:
    alpha[q]=((T1[q]-70)*0.15+7)*10**(-6)
    q+=1

while i<26:
    uC_v[i]= uC_p[i+1]-9*alpha[i]**2*kappa*V_m*T1[i]
    i+=1

#print(dt)
#print(dT)
#print(uC_p)
#print(E)
print(uC_v)
#print(alpha)
print(len(uC_v))

n_spalten=11
nullen = np.zeros(n_spalten)
thetadT= unp.uarray([2.4,3.1,2.9,2.6,2.3,2.0,2.1,2.2,2.2,2.1,1.7],[0,0,0,0,0,0,0,0,0,0,0])
theta = unp.uarray(nullen,nullen)
i=0

while i<11:
    theta[i]=thetadT[i]*T1[i]
    i+=1

    
print(theta)
print(np.mean(theta))

with open('table1.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    # Schreiben Sie die Kopfzeile in die CSV-Datei, wenn gewünscht
    writer.writerow(['R1', 'T1', 'ARez', 'Vrez', 'R1', 't1'])

    # Schreiben Sie die Inhalte der Arrays in die CSV-Datei
    for R1, T1, Acu, Vcu, R1, t1 in zip(R1, T1, Acu, Vcu, R1, t1):
        writer.writerow([R1, T1, Acu, Vcu, R1, t1])
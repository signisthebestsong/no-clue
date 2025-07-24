import numpy as np
import matplotlib.pyplot as plt

def line(x, A, b):
    return A*x+b

v300    = pd.read_csv('300.csv')
v350    = pd.read_csv('350.csv')
v400    = pd.read_csv('400.csv')
v500    = pd.read_csv('500.csv')
v600    = pd.read_csv('600.csv')

rho_vzd = 1.25  # hustota vzduchu
rho_ol  = 1030  # hustota oleje
eta     = 18.24e-6
g       = 9.81
d       = 2.5e-3
U       = np.array([300, 350, 400, 500, 600])
E       = U/d
roz     = 0.001483*30e-3

v300['sum'] = (np.abs(v300['v1'])+np.abs(v300['v2']))*roz
v350['sum'] = (np.abs(v350['v1'])+np.abs(v350['v2']))*roz
v400['sum'] = (np.abs(v400['v1'])+np.abs(v400['v2']))*roz
v500['sum'] = (np.abs(v500['v1'])+np.abs(v500['v2']))*roz
v600['sum'] = (np.abs(v600['v1'])+np.abs(v600['v2']))*roz

v300['r']   = np.sqrt(9*eta*np.abs(v300['delta'])*roz/(4*g*(rho_ol-rho_vzd)))
v350['r']   = np.sqrt(9*eta*np.abs(v350['delta'])*roz/(4*g*(rho_ol-rho_vzd)))
v400['r']   = np.sqrt(9*eta*np.abs(v400['delta'])*roz/(4*g*(rho_ol-rho_vzd)))
v500['r']   = np.sqrt(9*eta*np.abs(v500['delta'])*roz/(4*g*(rho_ol-rho_vzd)))
v600['r']   = np.sqrt(9*eta*np.abs(v600['delta'])*roz/(4*g*(rho_ol-rho_vzd)))

v300['q']   = 3*np.pi*eta*v300['r']*v300['sum']/E[0]
v350['q']   = 3*np.pi*eta*v350['r']*v350['sum']/E[1]
v400['q']   = 3*np.pi*eta*v400['r']*v400['sum']/E[2]
v500['q']   = 3*np.pi*eta*v500['r']*v500['sum']/E[3]
v600['q']   = 3*np.pi*eta*v600['r']*v600['sum']/E[4]

Q           = []
for i in range(len(v300['q'])):
    Q.append(np.sort(v300['q'])[i])
for i in range(len(v350['q'])):
    Q.append(np.sort(v350['q'])[i])
for i in range(len(v400['q'])):
    Q.append(np.sort(v400['q'])[i])
for i in range(len(v500['q'])):
    Q.append(np.sort(v500['q'])[i])
for i in range(len(v600['q'])):
    Q.append(np.sort(v600['q'])[i])

Q           = np.sort(np.array(Q))

# NOBODY WILL FIND THIS
# https://youtu.be/xvFZjo5PgG0?si=rPNrVgbkxhdWwQi3
print(Q)

q1          = Q[0:6]
q2          = Q[6:9]
q3          = Q[9:15]
q4          = Q[15:22]
q5          = Q[22:44]
q6          = Q[44:51]
q7          = Q[51:53]
q8          = Q[53:59]

xfit        = []

for i in range(len(q1)):
    xfit.append(1)

for i in range(len(q2)):
    xfit.append(2)

for i in range(len(q3)):
    xfit.append(3)

for i in range(len(q4)):
    xfit.append(4)

for i in range(len(q5)):
    xfit.append(5)

for i in range(len(q6)):
    xfit.append(6)

for i in range(len(q7)):
    xfit.append(7)

for i in range(len(q8)):
    xfit.append(8)

fitq        = curve_fit(line, xfit, Q[0:59])


q_fit       = fitq[0][0]
B_fit       = fitq[0][1]
dq_fit      = np.sqrt(np.diag(fitq[1]))[0]


hran = []

hran.append((np.min(q2)+np.max(q1))/2)
hran.append((np.min(q3)+np.max(q2))/2)
hran.append((np.min(q4)+np.max(q3))/2)
hran.append((np.min(q5)+np.max(q4))/2)
hran.append((np.min(q6)+np.max(q5))/2)
hran.append((np.min(q7)+np.max(q6))/2)
hran.append((np.min(q8)+np.max(q7))/2)


# For real this time (KEKW)
# ayaya123


vypQ        = [q1,q2,q3,q4,q5,q6,q7,q8]
el_nab      = []
for i in range(7):
    for j in range(i):
        el_nab.append((np.average(vypQ[i+1])-np.average(vypQ[j]))/(i-j+1))
e           = np.average(el_nab)
de          = np.std(el_nab, ddof=1)
print(f'{e} +- {de}')

ion300      = round(v300['q']/np.average(el_nab))
ion350      = round(v350['q']/np.average(el_nab))
ion400      = round(v400['q']/np.average(el_nab))
ion500      = round(v500['q']/np.average(el_nab))
ion600      = round(v600['q']/np.average(el_nab))
print(len(Q))

x_plt       = np.linspace(0,9,100)

plt.scatter(np.linspace(1,1,len(q1)), q1, label='1')
#plt.plot(np.linspace(0,9,100), np.linspace(e,e,100), color='black', linewidth='0.5')
plt.scatter(np.linspace(2,2,len(q2)), q2, label='2')
#plt.plot(np.linspace(0,9,100), np.linspace(2*e,2*e,100), color='black', linewidth='0.5')
plt.scatter(np.linspace(3,3,len(q3)), q3, label='3')
#plt.plot(np.linspace(0,9,100), np.linspace(3*e,3*e,100), color='black', linewidth='0.5')
plt.scatter(np.linspace(4,4,len(q4)), q4, label='4')
#plt.plot(np.linspace(0,9,100), np.linspace(4*e,4*e,100), color='black', linewidth='0.5')
plt.scatter(np.linspace(5,5,len(q5)), q5, label='5')
#plt.plot(np.linspace(0,9,100), np.linspace(5*e,5*e,100), color='black', linewidth='0.5')
plt.scatter(np.linspace(6,6,len(q6)), q6, label='6')
#plt.plot(np.linspace(0,9,100), np.linspace(6*e,6*e,100), color='black', linewidth='0.5')
plt.scatter(np.linspace(7,7,len(q7)), q7, label='7')
#plt.plot(np.linspace(0,9,100), np.linspace(7*e,7*e,100), color='black', linewidth='0.5')
plt.scatter(np.linspace(8,8,len(q8)), q8, label='8')
#plt.plot(np.linspace(0,9,100), np.linspace(8*e,8*e,100), color='black', linewidth='0.5')
plt.plot(x_plt, q_fit*x_plt+B_fit, color='red', label=f'$q=(1,52\pm0.04)~$C')
plt.ylabel('$q~$[C]')
plt.xlabel('Ionizace')
plt.legend()
plt.show()


plt.scatter(np.linspace(1,len(v300['q']), len(v300['q'])), v300['q'], label='300 V')
plt.scatter(np.linspace(1,len(v350['q']), len(v350['q'])), v350['q'], label='350 V')
plt.scatter(np.linspace(1,len(v400['q']), len(v400['q'])), v400['q'], label='400 V')
plt.scatter(np.linspace(1,len(v500['q']), len(v500['q'])), v500['q'], label='500 V')
plt.scatter(np.linspace(1,len(v600['q']), len(v600['q'])), v600['q'], label='600 V')
plt.plot([0,30], [hran[0], hran[0]], color='black', linewidth='0.5')
plt.plot([0,30], [hran[1], hran[1]], color='black', linewidth='0.5')
plt.plot([0,30], [hran[2], hran[2]], color='black', linewidth='0.5')
plt.plot([0,30], [hran[3], hran[3]], color='black', linewidth='0.5')
plt.plot([0,30], [hran[4], hran[4]], color='black', linewidth='0.5')
plt.plot([0,30], [hran[5], hran[5]], color='black', linewidth='0.5')
plt.plot([0,30], [hran[6], hran[6]], color='black', linewidth='0.5')
ax  = plt.gca()
ax.set_ylim([1e-19,1e-18])
plt.xlabel('Číslo naměřené kapky')
plt.ylabel('$q~$[C]')
plt.legend()
plt.show()

v300['v1']    = np.abs(v300['v1']*roz)
v350['v1']    = np.abs(v350['v1']*roz)
v400['v1']    = np.abs(v400['v1']*roz)
v500['v1']    = np.abs(v500['v1']*roz)
v600['v1']    = np.abs(v600['v1']*roz)

v300['v2']    = np.abs(v300['v2']*roz)
v350['v2']    = np.abs(v350['v2']*roz)
v400['v2']    = np.abs(v400['v2']*roz)
v500['v2']    = np.abs(v500['v2']*roz)
v600['v2']    = np.abs(v600['v2']*roz)

v300['delta'] = v300['delta']*roz
v350['delta'] = v350['delta']*roz
v400['delta'] = v400['delta']*roz
v500['delta'] = v500['delta']*roz
v600['delta'] = v600['delta']*roz

v300['ion']   = ion300
v350['ion']   = ion350
v400['ion']   = ion400
v500['ion']   = ion500
v600['ion']   = ion600

v300.to_excel('hodn_300.xlsx')
v350.to_excel('hodn_350.xlsx')
v400.to_excel('hodn_400.xlsx')
v500.to_excel('hodn_500.xlsx')
v600.to_excel('hodn_600.xlsx')

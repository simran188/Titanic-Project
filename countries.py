import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
mpl.style.use('classic')

plt.rcParams['xtick.major.size'] = 5
plt.rcParams['xtick.major.width'] = 1
plt.rcParams['xtick.minor.size'] = 2.5
plt.rcParams['xtick.minor.width'] = 1
plt.rcParams['ytick.major.size'] = 5
plt.rcParams['ytick.major.width'] = 1
plt.rcParams['ytick.minor.size'] = 2.5
plt.rcParams['ytick.minor.width'] = 1

A=20
font = {'family' : 'serif', 'weight' : 'normal', 'size' : A}
plt.rc('font', **font)
B = 19
linearColor = [132/255,30/255,255/255]
rootColor = [0/255,204/255,102/255]


def plotCountries():
    India()
    USA()
    SKorea()
    plt.show()




def India():
    fig, axes = plt.subplots(figsize=(7, 5.4))
    print("\n----------------INDIA----------------------")
    data = np.loadtxt("allCasesIndia.txt", comments='#')
    t = data[:,0]
    it = data[:,1]
    itdot = np.gradient(it)
    no_of_days = t[-1]
    print(no_of_days)
    
    #axes.text(2, 1e4, "India")
    axes.set_title("India", fontsize=A)
    axes.plot(t, it, color = 'red', lw=2)
    axes.plot(t, itdot, color = 'blue', lw=3)
    axes.set_yscale('log')
    
    exp1Start = 3 
    exp1Stop = 26
    pwr1Start = 28
    pwr1Stop = 36
    pwr2Start = 38
    pwr2Stop = 45
    
    tExp1 = t[exp1Start:exp1Stop]
    itExp1 = it[exp1Start:exp1Stop]
    constExp1 = np.polyfit(tExp1,np.log(itExp1),1)
    yfitExp1 = np.exp(constExp1[1])*np.exp(tExp1*constExp1[0])
    print(np.exp(constExp1[1]),"e^",constExp1[0])
    
    tPwr1 = t[pwr1Start:pwr1Stop]
    itPwr1 = it[pwr1Start:pwr1Stop]
    constPwr1 = np.polyfit(tPwr1, itPwr1, 1)
    yfitPwr1 = constPwr1[0]*tPwr1 + constPwr1[1]
    print(constPwr1[0], "t + ", constPwr1[1])
    
    tPwr2 = t[pwr2Start:pwr2Stop]
    itPwr2 = it[pwr2Start:pwr2Stop]
    constPwr2 = np.polyfit(tPwr2, itPwr2, 1)
    yfitPwr2 = constPwr2[0]*tPwr2 + constPwr2[1]
    print(constPwr2[0], "t + ", constPwr2[1])        
        
    errorExp1 = np.mean(np.abs(yfitExp1-itExp1)*100/itExp1)
    print("% error Exp1 =", errorExp1)
    errorPwr1 = np.mean(np.abs(yfitPwr1-itPwr1)*100/itPwr1)
    print("% error Pwr1 =", errorPwr1)
    errorPwr2 = np.mean(np.abs(yfitPwr2-itPwr2)*100/itPwr2)
    print("% error Pwr2 =", errorPwr2)
    
    axes.plot(tExp1, yfitExp1, color= 'k', lw=3, linestyle='dashed')
    axes.plot(tPwr1, yfitPwr1, color= linearColor, lw=3, linestyle='dashed')
    axes.plot(tPwr2, yfitPwr2, color= linearColor, lw=3, linestyle='dashed')
    axes.set_xlabel("$t$ $\mathrm{(days)}$")
    axes.set_ylabel("$I(t)$, $I'(t)$")
    
    axes.set_xlim(1, no_of_days)
    fig.tight_layout()


def USA():
    fig, axes = plt.subplots(figsize=(7, 5.4))
    print("\n----------------USA----------------------")
    data = np.loadtxt("allCasesUSA.txt", comments='#')
    t = data[:,0]
    it = data[:,1]
    itdot = np.gradient(it,t)
    
    no_of_days = t.size
    print (no_of_days)
    
    #axes.text(2, 1e4, "USA")
    axes.set_title("USA", fontsize=A)
    axes.plot(t, it, color = 'red', lw=2)
    axes.plot(t, itdot, color = 'blue', lw=3)
    axes.set_yscale('log')
    
    exp1Start = 9
    exp1Stop = 27
    exp2Start = 28
    exp2Stop = 36
    pwr1Start = 40
    pwr1Stop = 51
    pwr2Start = 53
    pwr2Stop = 58
    pwr3Start = 0
    pwr3Stop = 0
    
    tExp1 = t[exp1Start:exp1Stop]
    itExp1 = it[exp1Start:exp1Stop]
    constExp1 = np.polyfit(tExp1,np.log(itExp1),1)
    yfitExp1 = np.exp(constExp1[1])*np.exp(tExp1*constExp1[0])
    print(np.exp(constExp1[1]),"e^",constExp1[0])
    
    tExp2 = t[exp2Start:exp2Stop]
    itExp2 = it[exp2Start:exp2Stop]
    constExp2 = np.polyfit(tExp2,np.log(itExp2),1)
    yfitExp2 = np.exp(constExp2[1])*np.exp(tExp2*constExp2[0])
    print(np.exp(constExp2[1]),"e^",constExp2[0])
    
    tPwr1 = t[pwr1Start:pwr1Stop]
    itPwr1 = it[pwr1Start:pwr1Stop]
    constPwr1 = np.polyfit(tPwr1, itPwr1, 3)
    yfitPwr1 = constPwr1[0]*tPwr1**3 + constPwr1[1]*tPwr1**2 + constPwr1[2]*tPwr1 + constPwr1[3]
    print(constPwr1[0], "t3 + ", constPwr1[1], "t2 + ", constPwr1[2], "t + ",constPwr1[3])
    
    tPwr2 = t[pwr2Start:pwr2Stop]
    itPwr2 = it[pwr2Start:pwr2Stop]
    constPwr2 = np.polyfit(tPwr2, itPwr2, 1)
    yfitPwr2 = constPwr2[0]*tPwr2 + constPwr2[1]
    print(constPwr2[0], "t + ", constPwr2[1])
    
    errorExp1 = np.mean(np.abs(yfitExp1-itExp1)*100/itExp1)
    print("% error Exp1 =", errorExp1)
    errorExp2 = np.mean(np.abs(yfitExp2-itExp2)*100/itExp2)
    print("% error Exp2 =", errorExp2)
    errorPwr1 = np.mean(np.abs(yfitPwr1-itPwr1)*100/itPwr1)
    print("% error Pwr1 =", errorPwr1)
    errorPwr2 = np.mean(np.abs(yfitPwr2-itPwr2)*100/itPwr2)
    print("% error Pwr2 =", errorPwr2)
    
    axes.plot(tExp1, yfitExp1, color= 'k', lw=3, linestyle='dashed')
    axes.plot(tExp2, yfitExp2, color= 'k', lw=3, linestyle='dashed')
    axes.plot(tPwr1, yfitPwr1, color= 'k', lw=3, linestyle='dashed')
    axes.plot(tPwr2, yfitPwr2, color= linearColor, lw=3, linestyle='dashed')
    axes.set_xlabel("$t$ $\mathrm{(days)}$")
    axes.set_ylabel("$I(t)$, $I'(t)$")
    
    axes.set_xlim(1, no_of_days)
    fig.tight_layout()






def SKorea():
    fig, axes = plt.subplots(figsize=(7, 5.4))
    print("\n----------------SOUTH KOREA----------------------")
    data = np.loadtxt("allCasesSouthKorea.txt", comments='#')
    t = data[:,0]
    it = data[:,1]
    itdot = np.gradient(it,t)
    
    no_of_days = t.size
    print (no_of_days)
    
    #axes.text(2, 1e4, "South Korea")
    axes.set_title("South Korea", fontsize=A)
    axes.plot(t, it, color = 'red', lw=2)
    axes.plot(t, itdot, color = 'blue', lw=3)
    axes.set_yscale('log')
    
    exp1Start = 1
    exp1Stop = 5
    pwr1Start = 9
    pwr1Stop = 15
    pwr2Start = 18
    pwr2Stop = 23
    pwr3Start = 24
    pwr3Stop = 30
    
    tExp1 = t[exp1Start:exp1Stop]
    itExp1 = it[exp1Start:exp1Stop]
    constExp1 = np.polyfit(tExp1,np.log(itExp1),1)
    yfitExp1 = np.exp(constExp1[1])*np.exp(tExp1*constExp1[0])
    print(np.exp(constExp1[1]),"e^",constExp1[0])
    
    tPwr1 = t[pwr1Start:pwr1Stop]
    itPwr1 = it[pwr1Start:pwr1Stop]
    constPwr1 = np.polyfit(tPwr1, itPwr1, 2)
    yfitPwr1 = constPwr1[0]*tPwr1**2 + constPwr1[1]*tPwr1 + constPwr1[2]
    print(constPwr1[0], "t2 + ", constPwr1[1], "t + ", constPwr1[2])
    
    tPwr2 = t[pwr2Start:pwr2Stop]
    itPwr2 = it[pwr2Start:pwr2Stop]
    constPwr2 = np.polyfit(tPwr2, itPwr2, 1)
    yfitPwr2 = constPwr2[0]*tPwr2 + constPwr2[1]
    print(constPwr2[0], "t + ", constPwr2[1])
    
    tPwr3 = t[pwr3Start:pwr3Stop]
    itPwr3 = it[pwr3Start:pwr3Stop]
    constPwr3 = np.polyfit(tPwr3**0.5, itPwr3, 1)
    yfitPwr3 = constPwr3[0]*tPwr3**0.5 + constPwr3[1]
    print(constPwr3[0], "t^(0.5) + ", constPwr3[1])
    
    errorExp1 = np.mean(np.abs(yfitExp1-itExp1)*100/itExp1)
    print("% error Exp1 =", errorExp1)
    errorPwr1 = np.mean(np.abs(yfitPwr1-itPwr1)*100/itPwr1)
    print("% error Pwr1 =", errorPwr1)
    errorPwr2 = np.mean(np.abs(yfitPwr2-itPwr2)*100/itPwr2)
    print("% error Pwr2 =", errorPwr2)
    errorPwr3 = np.mean(np.abs(yfitPwr3-itPwr3)*100/itPwr3)
    print("% error Pwr3 =", errorPwr3)
    
    axes.plot(tExp1, yfitExp1, color= 'k', lw=3, linestyle='dashed')
    axes.plot(tPwr1, yfitPwr1, color= 'k', lw=3, linestyle='dashed')
    axes.plot(tPwr2, yfitPwr2, color= linearColor, lw=3, linestyle='dashed')
    axes.plot(tPwr3, yfitPwr3, color= rootColor, lw=3, linestyle='dashed')
    axes.set_xlabel("$t$ $\mathrm{(days)}$")
    axes.set_ylabel("$I(t)$, $I'(t)$")
    
    axes.set_xlim(1, no_of_days)
    fig.tight_layout()




    

    





plotCountries()


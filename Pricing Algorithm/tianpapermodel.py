import numpy as np
import matplotlib.pyplot as plt


def v(x, t, a=8):
    """
    This is the v() function as indicated in the paper
    x: input status of current serving periods
    t: t time units ahead
    """
    
    res = 0
    if x <= 0 or t == 0:
        return 0
    
    fac_i = 1
    for i in range(x):
        res += (a*t/np.e)**i / fac_i
        fac_i *= i+1  # update
    
    return np.log(res)


def p(x, t, a=8):
    """
    This is the price function as indicated in the paper
    x : input status of current service period
    t : t time units ahead
    """
    
    res = 1 + v(x, t, a) - v(x-1, t, a)
    return res


def r(T=24, S=24, P=25, a=8):
    """
    This is the function computing total revenues
    T: total number of hours
    S: number of service periods
    P: number of parking spots
    a: coefficient as in the paper, default as 8
    """
    
    XT = np.zeros([S,T]).astype(np.int)
    XT[:, :] = P
    ps = np.zeros(XT.shape)

    for i in range(10):
        for t in range(T):
            for x in range(S): # service periods
                ps[x, t] = 1 + v(XT[x,t], t, a) - v(XT[x,t]-1, t, a)
                d = a * np.exp(-ps[x,t])
                if d > XT[x, t]:
                    XT[x, t] = 0
                else:
                    XT[x, t] = P - np.ceil(d)   
        #print("iter={}, max_price={:.2f}, min_price={:.2f}, max_spots={}, min_spots={}, revenue={:.2f}".format(
        #    i, np.max(ps), np.min(ps), np.max(XT), np.min(XT), np.sum(ps * (P - XT))))
    
    res = np.sum(ps * (P - XT))
    return res


def f(T=24, S=24, P=25, a=8, pr=1):
    """
    This is the fix price revenue function
    T: total number of hours
    S: number of service periods
    P: number of parking spots
    a: coefficient as in the paper, default as 8
    pr: current price given
    """
    
    XT = np.zeros([S,T]).astype(np.int)
    XT[:, :] = P
    ps = np.zeros(XT.shape)
    ps[:, :] = pr 

    for t in range(T):
        for x in range(S): # service periods
            d = a * np.exp(- ps[x,t])
            XT[x, t] = XT[x, t] - np.ceil(d)

    XT = P - XT
    return np.sum(ps * XT)


if __name__ == "__main__":
    
    TS = range(2, 36, 2)
    RS = []
    FS = []
    
    for T in TS:
        RS.append(r(T=T))
        FS.append(f(T=T))
    
    plt.plot(TS,RS,TS,FS)
    plt.gca().legend(('dynamic pricing','fixed pricing'))
    plt.xlabel('# of hours ahead')
    plt.ylabel('revenue in total')
    plt.figure(figsize=(30,30))
    plt.show()

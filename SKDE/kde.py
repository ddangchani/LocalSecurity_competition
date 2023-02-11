import sett

def densityF(x, y, xi, yi):
    
    u = (x-xi) / sett.p1 
    v = (y-yi) / sett.p1 

    Ks = sett.ct1 * (1 - u**2 - v**2)
    spaceKDE = 0.75 * sett.ct2 * Ks
    return spaceKDE
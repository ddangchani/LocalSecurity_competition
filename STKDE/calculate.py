def densityF(x, y, t, xi, yi, ti):
    import sett
    u = (x-xi) / sett.p1 
    v = (y-yi) / sett.p1 
    w = (t-ti) / sett.p2 
    Ks = sett.ct1 * (1 - pow(u, 2) - pow(v, 2))
    Kt = 0.75 * (1 - pow(w, 2))
    spaceTimeKDE = sett.ct2 * Ks * Kt
    return spaceTimeKDE

def calc(i,j,xyGrid,tGrid,sList,tList,inXY,inT):
    import sett
    xC, yC, tC = xyGrid[i][0], xyGrid[i][1], tGrid[j][0] # current grid (X,Y : Centroid)

    # nList > points that are neighbors both spatially and temporally
    nList = [val for val in sList[i] if val in tList[j]]
    density = 0.0 # estimated density
    
    # calculate density
    if nList: # neighbor 존재하면 density 추가
        for k in nList:
            nindex = int(k)
            density += densityF(
                inXY[nindex][0], inXY[nindex][1], 
                inT[nindex][0], xC, yC, tC)
        
    # return density
    return([xC, yC, tC, density])
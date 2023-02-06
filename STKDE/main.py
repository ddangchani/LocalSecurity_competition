if __name__ =='__main__':
        
    import math, os, sys
    import numpy as np
    import pandas as pd
    import geopandas as gpd
    from scipy import spatial
    import kde, dataset, calculate
    from tqdm import tqdm
    import multiprocessing
    import calculate as calc
    import sett

    # Initialize
    sett.init()

    # read parameters
    parameters = {'p1' : 10000.0, 'p2' : 72.0, 'p3' : 1000.0, 'p4' : 2}

    sett.p1 = float(parameters['p1'])	# p1 = spatial bandwidth(meter)
    sett.p2 = float(parameters['p2'])	# p2 = temporal bandwidth(hour)
    sett.p3 = float(parameters['p3'])	# p3 = spatial resolution(meter)
    sett.p4 = int(parameters['p4'])	    # p4 = temporal resolution(hour)

    # Load data
    inXY, inT, xyGrid, tGrid = dataset.load_dataset()

    # 전역변수 설정(global variables)
    sett.npts = len(inXY)
    sett.ct1 = 0.5 * math.pi
    sett.ct2 = pow(10.0, 5) / (sett.npts * pow(sett.p1, 2) * sett.p2)

    #build trees

    stree = spatial.cKDTree(inXY)
    ttree = spatial.cKDTree(inT)

    sList = stree.query_ball_point(xyGrid, r=sett.p1)[:100]
    tList = ttree.query_ball_point(tGrid, r=sett.p2)[:100]

    print('Built cKDTree!')



    # Using Multiprocessing Pool
    from itertools import product
    import parmap
    from itertools import product
    ls = [item for item in product(range(len(sList)),range(len(tList)))]

    stList = parmap.starmap(calc.calc, ls, xyGrid, tGrid, sList, tList, inXY, inT, pm_pbar=True)

    stList = pd.DataFrame(stList, columns=['X', 'Y', 'T', 'density'])
    stList.to_csv(f'data/stKDE_{sett.p1}_{sett.p2}.csv', index=False)
    print('STKDE completed!')
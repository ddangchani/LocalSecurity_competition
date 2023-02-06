import numpy as np
import pandas as pd
import geopandas as gpd


def load_dataset():
    import sett
    
    # Load Data
    df = gpd.read_file('data/gdf_crime_full.gpkg')
    df = df.to_crs(epsg=5181) # 좌표계 m단위로 변경
    df = df[['RECV_CPLT_DM', 'geometry']]
    df.RECV_CPLT_DM = df.RECV_CPLT_DM.dt.to_period('H')
    df.RECV_CPLT_DM = df.RECV_CPLT_DM.dt.to_timestamp()

    # data에 time index 찾아 넣기(기준시점으로부터 시간)

    df['T'] = 0.0
    for i in range(len(df)):
        # 2021년 1월 1일 0시 기준
        delta = df.RECV_CPLT_DM[i] - pd.Timestamp(2020, 1, 1, 0) 
        df.iat[i, 2] = delta / pd.Timedelta(hours=1)

    # X, Y 좌표 추출
    df['X'] = df.geometry.x
    df['Y'] = df.geometry.y

    # 각 벡터 분리
    inX = df['X']
    inY = df['Y']
    inT = df['T'].to_numpy().reshape(-1,1)

    inXY = list(zip(inX, inY))

    # 격자데이터 로드, 격자화
    grid = gpd.read_file('data/CENSUS/grid.gpkg') # epsg:5181
    xyGrid = list(zip(grid.geometry.centroid.x, grid.geometry.centroid.y))
    tmin, tmax = 0.0, max(inT)

    tminDiff = tmin%sett.p4
    tmaxDiff = tmax%sett.p4

    tminP = tmin - tminDiff + sett.p4
    tmaxP = tmax - tmaxDiff + sett.p4

    tGrid = []
    for k in range(int(tminP),int(tmaxP),sett.p4):
        tGrid.append([k])

    print('Data Load complete!')

    return inXY, inT, xyGrid, tGrid

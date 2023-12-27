# LocalSecurity_competition
제1회 지역 치안 안전 데이터 분석 경진대회를 위한 repository 입니다

## Topic : Development of a prediction model for risk areas for voice fraud(voice phishing) using kernel density analysis and spatial models

## 최종 보고서 : [Link](https://github.com/ddangchani/LocalSecurity_competition/blob/main/%E1%84%87%E1%85%A9%E1%84%80%E1%85%A9%E1%84%89%E1%85%A5_github.pdf)

## 분석 데이터
- 플랫폼 측에서 제공받은 112 사건신고 접수 데이터(접수일시, 사건코드, 사건좌표)
  - 2020-2022년 데이터
  - 공간분석 computational cost 절감을 위해 대전광역시, 세종특별자치시 데이터만 사용
  - 분석대상범죄 : **보이스피싱**

- 외부데이터
> - SGIS(통계지리정보시스템) : 격자별(1000m) 인구정보(연령, 성별)
> - 지역 내 ATM, CD 등 현금출금가능 시설 위치정보(크롤러 이용)
>   - `Crawler_atm.ipynb` : `Selenium` 이용
> - 국토교통부_전국 버스정류장 위치정보
> - 상권정보(소상공인시장진흥공단)

## 분석 방법
- SpatioTemporal/Spatial Kernel Density Estimation(STKDE/SKDE) : 
  > - 시공간(3D) or 공간(2D) 커널밀도분석으로 분석 대상 지역 내 보이스피싱 범죄 핫스팟(Hotspot) 추출
  > - 사용 커널 : Epanechnikov kernel
  > - code modified [from Here](https://github.com/alexandster/densitySpaceTime)

- Spatial Regression : `pysal` 이용
- Machine Learning(GBM) : with `pycaret`
  > Hyperparameter tuning : Bayesian Optimization

## 분석 결과
제공 데이터셋과 외부데이터를 활용하여 대전 및 세종 지역의 보이스피싱 범죄위험지역을 100m 격자 단위로 분석한 결과</br>

한 지역 내에서 보이스피싱 범죄가 발생하는 것을 **랜덤한 확률변수로** 가정하면
- 공간커널밀도분석으로 oversmoothing bandwidth를 이용하여 지역 내 확률밀도함수를 추정할 수 있고
- 외생변수공간시차모형(혹은 GBM모델)을 활용하여 25%의 Hotspot으로 90% 이상의 범죄 발생지점을 예측하는 모델을 생성할 수 있음

## 대회 결과 : 최우수상(2위)🏆
- 대회 후기 및 간략한 리뷰 : https://velog.io/@ddangchani/제1회-지역치안데이터분석경진대회-공모전-후기

# LocalSecurity_competition
제1회 지역 치안 안전 데이터 분석 경진대회를 위한 repository 입니다

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

## 분석 방법
- SpatioTemporal Kernel Density Estimation(STKDE)
  - code modified [from Here](https://github.com/alexandster/densitySpaceTime)
  > 시공간 커널밀도분석으로 분석 대상 지역 내 보이스피싱 범죄 핫스팟(Hotspot) 추출
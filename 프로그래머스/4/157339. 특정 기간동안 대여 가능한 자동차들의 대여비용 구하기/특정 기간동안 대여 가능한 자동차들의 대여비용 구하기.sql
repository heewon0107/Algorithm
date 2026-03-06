-- 코드를 입력하세요
#1. 세단 or suv 차
#2. CAR_ID 조인 하는데 START_DATE END_DATE 가 11월 1일 ~ 11월 30일
#3. DAILY_FEE * 30 


SELECT  CAR_ID, C.CAR_TYPE, ROUND(C.DAILY_FEE * 30 * (100 - D.DISCOUNT_RATE) / 100) AS FEE
        
        # C 테이블의 세 개 속성
  FROM  (SELECT  B.CAR_ID, A.CAR_TYPE, A.DAILY_FEE
          # SUV, 세단인 자동차들 A
          FROM  (SELECT  CAR_ID, CAR_TYPE, DAILY_FEE 
                   FROM  CAR_RENTAL_COMPANY_CAR
                  WHERE  CAR_TYPE IN ('SUV', '세단')) A
                    # 렌트 히스토리 B
                     JOIN  CAR_RENTAL_COMPANY_RENTAL_HISTORY B
                     ON A.CAR_ID = B.CAR_ID
          # 차 종별  
           GROUP
              BY  B.CAR_ID
          # 가장 마지막 렌트반납일이 2022-11-01 이전인 C
          HAVING  MAX(END_DATE) < '2022-11-01') C 
          
          # 
          JOIN  CAR_RENTAL_COMPANY_DISCOUNT_PLAN D
          ON C.CAR_TYPE = D.CAR_TYPE
          
 WHERE  D.DURATION_TYPE LIKE '30%' AND (C.DAILY_FEE * 30 * (100 - D.DISCOUNT_RATE) / 100) BETWEEN 500000 AND 2000000
 
 ORDER
    BY  FEE DESC,
        C.CAR_TYPE, 
        C.CAR_ID DESC
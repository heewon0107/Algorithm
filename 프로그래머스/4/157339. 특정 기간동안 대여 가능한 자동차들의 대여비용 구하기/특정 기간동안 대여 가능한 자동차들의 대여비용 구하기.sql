SELECT  CAR_ID, C.CAR_TYPE, ROUND(C.DAILY_FEE * 30 * (100 - D.DISCOUNT_RATE) / 100) AS FEE
        
        # C 테이블의 세 개 속성
  FROM  (SELECT  B.CAR_ID, A.CAR_TYPE, A.DAILY_FEE
          #1. SUV, 세단인 자동차들 A JOIN 히스토리 B
          FROM  (SELECT  CAR_ID, CAR_TYPE, DAILY_FEE 
                   FROM  CAR_RENTAL_COMPANY_CAR
                  WHERE  CAR_TYPE IN ('SUV', '세단')) A
                    # 렌트 히스토리 B
                     JOIN  CAR_RENTAL_COMPANY_RENTAL_HISTORY B
                     ON A.CAR_ID = B.CAR_ID
         
          #2. 차 종별 가장 마지막 렌트반납일이 2022-11-01 이전인 C
          GROUP
             BY  B.CAR_ID
         
          HAVING  MAX(END_DATE) < '2022-11-01') C 
          
          #3. 렌트 가능한 차 C와 할인율 D 조인
          JOIN  CAR_RENTAL_COMPANY_DISCOUNT_PLAN D ON C.CAR_TYPE = D.CAR_TYPE
        
        #4. 30일 이상 할인율이 범위 안에 들어있는 인스턴스 찾기
 WHERE  D.DURATION_TYPE LIKE '30%' AND (C.DAILY_FEE * 30 * (100 - D.DISCOUNT_RATE) / 100) BETWEEN 500000 AND 2000000
 
 ORDER
    BY  FEE DESC,
        C.CAR_TYPE, 
        C.CAR_ID DESC

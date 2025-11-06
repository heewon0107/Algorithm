# 1. 대장균 개체의 크기 DESC
# 2. 비율 별 라벨링
# 2-1. 한 컬럼이 어느 비율에 속하는지 알아야 함

# 총 데이터는 4배수

SELECT  ID,
        CASE
        WHEN    A.P <= 0.25 THEN 'CRITICAL'
        WHEN    A.P <= 0.5  THEN 'HIGH'
        WHEN    A.P <= 0.75 THEN 'MEDIUM'
        ELSE    'LOW'
        END AS  COLONY_NAME
        
  FROM  (SELECT ID,
                PERCENT_RANK() OVER(ORDER BY SIZE_OF_COLONY DESC) AS P
           FROM ECOLI_DATA) AS A
  
 ORDER  
    BY  A.ID
  
 
        
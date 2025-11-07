# 3세대 대장균은 내 부모가 부모를 가져야함
# A 조부모, B 부모, C 자식
# 1. B,C 조인 
# 2. B의 PARENT의 PARENT가 NULL이여야함

SELECT  C.ID

  FROM  ECOLI_DATA B
        JOIN
        ECOLI_DATA C
        ON B.ID = C.PARENT_ID

 WHERE  B.PARENT_ID IS NOT NULL
        AND 
        (SELECT A.PARENT_ID
           FROM ECOLI_DATA A
          WHERE A.ID = B.PARENT_ID) IS NULL
 
 ORDER
    BY  C.ID
  


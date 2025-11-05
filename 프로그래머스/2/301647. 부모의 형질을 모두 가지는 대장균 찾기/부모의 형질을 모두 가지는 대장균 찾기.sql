# 1. 부모와의 AND 비교
# 2. 부모의 형질 SELECT


# A = 부모, B = 자식

SELECT  B.ID,
        B.GENOTYPE,
        A.GENOTYPE AS PARENT_GENOTYPE

  FROM  ECOLI_DATA A
        JOIN
        ECOLI_DATA B
        ON A.ID = B.PARENT_ID
        
  
 WHERE  (A.GENOTYPE & B.GENOTYPE) = A.GENOTYPE
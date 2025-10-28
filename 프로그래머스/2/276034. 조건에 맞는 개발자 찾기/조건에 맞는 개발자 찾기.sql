SELECT  DISTINCT
        B.ID,
        B.EMAIL,
        B.FIRST_NAME,
        B.LAST_NAME

  FROM  SKILLCODES AS A
        JOIN
        DEVELOPERS AS B
        ON
        A.CODE & B.SKILL_CODE > 0
 
 WHERE  A.NAME IN ('Python','C#')
 
 ORDER
    BY  ID
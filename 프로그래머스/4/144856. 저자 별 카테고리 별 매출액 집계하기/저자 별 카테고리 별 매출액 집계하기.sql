# 1. SALES DATE 2022년 1월 도서 분리

# 2. 카테고리별 매출액 ID마다의 SUM(SALES)

# 3. 저자의 카테고리별 매출액
SELECT  A.AUTHOR_ID,
        A.AUTHOR_NAME,
        B.CATEGORY,
        SUM(S.SALES * B.PRICE) AS TOTAL_SALES

  FROM  (BOOK B 
        JOIN 
        AUTHOR A 
        ON  B.AUTHOR_ID = A.AUTHOR_ID) 
        JOIN
        BOOK_SALES S
        ON B.BOOK_ID = S.BOOK_ID
        
 WHERE  SUBSTR(S.SALES_DATE,1,7) = '2022-01'
 
 GROUP
    BY  B.CATEGORY, A.AUTHOR_NAME
  
 ORDER
    BY  A.AUTHOR_ID,
        B.CATEGORY DESC
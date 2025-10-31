# 식품분류별 제일 비싼 식품 찾기

# 1. 식품 분류별로 제일 비싼 아이템 찾기
SELECT  CATEGORY,
        PRICE AS MAX_PRICE,
        PRODUCT_NAME
        
  FROM  FOOD_PRODUCT
  
 WHERE  PRICE
        IN (SELECT  MAX(PRICE)
              FROM  FOOD_PRODUCT
             WHERE  CATEGORY IN ('과자', '국', '김치', '식용유')
             GROUP
                BY  CATEGORY)
        AND
        CATEGORY IN ('과자', '국', '김치', '식용유')
 ORDER
    BY  PRICE DESC
-- 코드를 입력하세요
SELECT *
FROM food_product
WHERE price = (SELECT MAX(PRICE) FROM FOOD_PRODUCT);
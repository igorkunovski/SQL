-- 2 Выведите только четные числа от 1 до 10 включительно. (Через функцию / процедуру)
-- Пример: 2,4,6,8,10 (можно сделать через шаг +  2: х = 2, х+=2)

DROP PROCEDURE IF EXISTS numbers;

DELIMITER //
CREATE PROCEDURE numbers  (IN input_number INT)
BEGIN
DECLARE n INT;
DECLARE x INT;
DECLARE result VARCHAR(45) DEFAULT "";
SET n = input_number;
SET x = 2;

    REPEAT
    	SET result = CONCAT(result, x, ",");
        SET x = x + 2;
        UNTIL x > input_number
	END REPEAT;
    
    SELECT result; 
END //

CALL numbers(10);

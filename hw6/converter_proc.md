-- 1.	Создайте функцию, которая принимает кол-во сек и форматирует их в кол-во дней, часов, минут и секунд.
-- Пример: 123456 ->'1 days 10 hours 17 minutes 36 seconds '


DROP PROCEDURE IF EXISTS timing;

DELIMITER //
CREATE PROCEDURE timing  (IN input_seconds INT)
BEGIN
DECLARE n INT;
DECLARE x INT;
DECLARE seconds INT;
DECLARE minutes INT;
DECLARE hours INT;
DECLARE days INT;
DECLARE result VARCHAR(255) DEFAULT "";
SET n = input_seconds;
SET x = 60;


    IF n > x THEN 
		SET seconds = n % x;
        SET n = (n - seconds) / x;
        SET result = CONCAT(result, seconds, " seconds.");
	ELSE 		
		SET result = CONCAT(result, n, " seconds.");
        SET n = 0;
    END IF;
    
	IF n > x THEN
		SET minutes = n % x;
        SET n = (n - minutes) / x;
        SET x = 24;
        SET result = CONCAT( minutes, " minutes, ", result);
	ELSEIF n > 0 THEN 		
		SET result = CONCAT(n, " minutes, ", result);
        SET x = 24;
        SET n = 0;
     END IF;
     
	IF n > x THEN
		SET hours = n % x;
        SET n = (n - hours) / x;        
        SET result = CONCAT( hours, " hours, ", result);
    ELSEIF n > 0 THEN 		
		SET result = CONCAT(n, " hours, ", result);
        SET n = 0;
	END IF;
    
    IF n > 0 THEN
        SET result = CONCAT( n, " days, ", result);	     
END IF;

    SELECT result; 
END //

CALL timing(123456);
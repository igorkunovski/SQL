/* HW1
1. Создайте таблицу с мобильными телефонами, используя графический интерфейс.
2. Заполните БД данными Выведите название, производителя и цену для товаров, количество которых превышает 2.
3. Выведите весь ассортимент товаров марки “Samsung”
*/


CREATE TABLE `hw1`.`phone` (
`id` INT NOT NULL AUTO_INCREMENT,
`producer` VARCHAR(45) NOT NULL,
`model` VARCHAR(45) NOT NULL,
`color` VARCHAR(45) NOT NULL,
`memory` INT NOT NULL,
`price` DOUBLE NOT NULL,
`qty` INT NOT NULL,
PRIMARY KEY (`id`));

INSERT INTO `hw1`.`phone` (`producer`, `model`, `color`, `memory`, `price`, `qty`) 
VALUES ('Apple', 'iPHONE 11', 'black', '64', '600', '10');
INSERT INTO `hw1`.`phone` (`producer`, `model`, `color`, `memory`, `price`, `qty`) 
VALUES ('Apple', 'iPHONE 13', 'white', '128', '650', '5');
INSERT INTO `hw1`.`phone` (`producer`, `model`, `color`, `memory`, `price`, `qty`) 
VALUES ('Samsung', 'Galaxy S22', 'black', '256', '680', '2');
INSERT INTO `hw1`.`phone` (`producer`, `model`, `color`, `memory`, `price`, `qty`) 
VALUES ('Samsung', 'Galaxy A53', 'white', '256', '330', '6');
INSERT INTO `hw1`.`phone` (`producer`, `model`, `color`, `memory`, `price`, `qty`) 
VALUES ('Xiaomi', 'Redmi 9C', 'green', '64', '150', '10');
INSERT INTO `hw1`.`phone` (`producer`, `model`, `color`, `memory`, `price`, `qty`) 
VALUES ('Sony', 'Xperia 10', 'green', '128', '400', '1');

SELECT model, producer, price
FROM hw1.phone
WHERE qty > 2;

SELECT * FROM hw1.phone
WHERE producer = "samsung";

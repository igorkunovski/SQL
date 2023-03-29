-- 1.	Создайте представление, в которое попадут автомобили стоимостью  до 25 000 долларов

CREATE OR REPLACE VIEW up_to_25000 AS
SELECT id, name, cost
FROM cars
WHERE cost < 25000
ORDER BY name;

SELECT * FROM up_to_25000;

-- 2.	Изменить в существующем представлении порог для стоимости: пусть цена будет до 30 000 долларов (используя оператор ALTER VIEW)


ALTER VIEW up_to_25000 AS
SELECT id, name, cost
FROM cars
WHERE cost < 30000
ORDER BY name;

SELECT * FROM up_to_25000;

-- 3. 	Создайте представление, в котором будут только автомобили марки “Шкода” и “Ауди”

CREATE OR REPLACE VIEW audi_skoda AS
SELECT id, name, cost
FROM cars
WHERE name = 'Audi' OR name = 'Skoda'
ORDER BY cost;
SELECT * FROM audi_skoda;

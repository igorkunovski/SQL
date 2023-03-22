-- 1. Отсортируйте данные по полю заработная плата (salary) в порядке: убывания; возрастания

SELECT * FROM staff
ORDER BY salary;

SELECT * FROM staff
ORDER BY salary DESC;

-- 2. Выведите 5 максимальных заработных плат (saraly)

SELECT * FROM staff
ORDER BY salary DESC
LIMIT 5;

-- 3. Посчитайте суммарную зарплату (salary) по каждой специальности (роst)

SELECT post AS "Должность",
SUM(salary) AS "Суммарная ЗП по специальности"
FROM staff
GROUP BY post;

-- 4 Найдите кол-во сотрудников с специальностью (post) «Рабочий» в возрасте от 24 до 49 лет 
включительно.

SELECT count(post) AS "Рабочее от 24 до 49 лет"
FROM staff
WHERE post = "Рабочий" AND age >= 24 AND age <= 49;

-- 5 Найдите количество специальностей

SELECT 
count(DISTINCT (post))  AS "Кол-во рабочих специальностей"
FROM staff;

-- Выведите специальности, у которых средний возраст сотрудников меньше 30 лет (в нашем примере 
таблица результатов будет пуста)

SELECT post AS "Должность", AVG(age) AS "Средний возраст"
FROM staff
GROUP BY post
HAVING AVG(age) < 30;

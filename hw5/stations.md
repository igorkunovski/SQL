/*
Добавьте новый столбец под названием «время до следующей станции». Чтобы получить это значение, мы вычитаем время станций для пар смежных станций.
Мы можем вычислить это значение без использования оконной функции SQL, но это может быть очень сложно. Проще это сделать с помощью оконной функции LEAD .
Эта функция сравнивает значения из одной строки со следующей строкой, чтобы получить результат.
В этом случае функция сравнивает значения в столбце «время» для станции со станцией сразу после нее.
*/

SELECT train_id,
station,
station_time as 'Departure',
LEAD(station_time, 1, 0) OVER (PARTITION BY train_id ORDER BY station_time) AS 'Arrive',
timediff(LEAD(station_time) OVER (PARTITION BY train_id ORDER BY station_time), station_time) AS 'Duration'
FROM stations;


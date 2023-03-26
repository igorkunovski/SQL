-- 1. Вывести на экран сколько машин каждого цвета для машин марок BMW и LADA

SELECT MARK, COLOR, COUNT(*) AS "QTY"
FROM auto
WHERE MARK = "BMW" OR MARK = "LADA"
GROUP BY MARK, COLOR
ORDER BY MARK;

-- 2. Вывести на экран марку авто и количество AUTO не этой марки

SELECT MARK, (SELECT COUNT(*) from auto) - COUNT(*) AS "QTY of other auto marks"
from auto
GROUP BY MARK
ORDER BY MARK;
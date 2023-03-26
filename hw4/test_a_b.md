-- Напишите запрос, который вернет строки из таблицы test_a, id которых нет в таблице test_b, НЕ используя ключевого слова NOT.

SELECT a.id, a.data
FROM test_a AS a
LEFT JOIN test_b AS b ON a.id = b.id
WHERE b.id IS NULL;


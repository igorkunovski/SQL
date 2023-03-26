-- Вывести название и цену для всех анализов, которые продавались 5 февраля 2020 и всю следующую неделю.

SELECT analysis.an_name, analysis.an_price, orders.ord_datetime
FROM analysis
JOIN orders ON analysis.an_id = orders.ord_an
WHERE orders.ord_datetime BETWEEN "2020-02-05" AND "2020-02-13";

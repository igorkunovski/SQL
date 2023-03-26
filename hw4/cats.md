-- Вывести всех котиков по магазинам по id (условие соединения shops.id = cats.shops_id)

SELECT
cats.shops_id, 	cats.name, 	shops.id, shops.shopname
FROM cats
JOIN shops ON shops.id = cats.shops_id;

-- Вывести магазин, в котором продается кот “Мурзик” (попробуйте выполнить 2 способами)


SELECT shopname AS "Магазин с Мурзиком"
FROM shops
JOIN cats ON shops.id = cats.shops_id
WHERE cats.name = "Murzik";

SELECT shopname AS "Магазин с Мурзиком"
FROM cats, shops
WHERE shops.id = cats.shops_id AND cats.name = "Murzik";


-- Вывести магазины, в котором НЕ продаются коты “Мурзик” и “Zuza”

SELECT shopname AS "Магазин без Мурзика и Зузы"
FROM shops
JOIN cats ON shops.id = cats.shops_id
WHERE cats.name != "Murzik" AND cats.name != "Zuza";
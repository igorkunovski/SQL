-- выбрать всех пользователей, указав их id, имя и фамилию, город и аватарку
-- (используя вложенные запросы)
-- (используя JOIN)

SELECT id, firstname, lastname, hometown, photo_id
FROM users, profiles
WHERE users.id = profiles.user_id;

SELECT id, firstname, lastname, hometown, photo_id
FROM users
LEFT JOIN profiles ON
users.id = profiles.user_id;


-- выбрать фотографии (filename) пользователя с email: arlo50@example.org . ID типа медиа, соответствующий фотографиям неизвестен.
-- (используя вложенные запросы)

SELECT filename, users.id
FROM media
RIGHT JOIN users ON users.id = media.user_id
WHERE users.email = "arlo50@example.org" AND media.filename REGEXP '.jpg$|.bmp$|.jpeg$|.png$';

SELECT filename, users.id
FROM media, users
WHERE users.id = media.user_id AND users.email = "arlo50@example.org" AND media.filename REGEXP '.jpg$|.bmp$|.jpeg$|.png$';

SELECT filename, users.id
FROM media
RIGHT JOIN users ON
users.id = media.user_id
WHERE users.email = "arlo50@example.org" AND media.media_type_id = 1;

-- выбрать id друзей пользователя с id = 1
-- (используя UNION)

SELECT friend_requests.target_user_id AS "Approved friends of user with id 1"
FROM friend_requests
WHERE friend_requests.initiator_user_id = 1 AND friend_requests.status = 'approved'
UNION
SELECT friend_requests.initiator_user_id
FROM friend_requests
WHERE friend_requests.target_user_id = 1 AND friend_requests.status = 'approved';

-- Список медиафайлов пользователей, указав название типа медиа (id, filename, name_type)
-- (используя JOIN)

SELECT media.user_id, media.filename, media_types.name_type
FROM media
LEFT JOIN media_types ON media.media_type_id = media_types.id
ORDER BY media.user_id;

-- Создайте представление, в котором будут выводится все сообщения, в которых принимал участие пользователь с id = 1.

SELECT messages.from_user_id, messages.to_user_id, messages.body
FROM messages
WHERE messages.from_user_id = 1
UNION
SELECT messages.from_user_id, messages.to_user_id, messages.body
FROM messages
WHERE messages.to_user_id = 1;


-- список публикаций пользователя id=1

SELECT media.user_id, media.filename, media_types.name_type
FROM media
LEFT JOIN media_types ON media.media_type_id = media_types.id
WHERE media.user_id = 1 AND media_types.name_type = 'Post'
ORDER BY media.user_id;

-- тексты публикаций пользователя id=1

SELECT user_id, body AS Post
FROM media
WHERE user_id = 1 AND media_type_id = 4;
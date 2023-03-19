№1. Используя оператор ALTER TABLE, установите внешний ключ в одной из таблиц.
№2. Без оператора JOIN, верните заголовок публикации, текст с описанием, идентификатор клиента, опубликовавшего публикацию и логин данного клиента.
№3. Выполните поиск по публикациям, автором котоырх является клиент "Mikle".

**1.** 

ALTER TABLE clients
ADD COLUMN posts_id INT REFERENCES posts(id);

SELECT * FROM clients;

**2.**

SELECT title, full_text, user_id, login
    FROM posts, users
WHERE users.id = posts.user_id;

**3.**

SELECT title, login
    FROM posts, users
WHERE posts.user_id = users.id
    AND users.login = "Mikle";


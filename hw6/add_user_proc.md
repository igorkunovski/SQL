-- Создать процедуру для добавления нового пользователя с профилем

DROP PROCEDURE IF EXISTS add_user;

DELIMITER //
CREATE PROCEDURE add_user
(
IN id INT,
IN firstname VARCHAR(50),
IN lastname VARCHAR(50),
IN email VARCHAR(120),
IN gender VARCHAR(1),
IN birthday VARCHAR(15),
IN photo_id INT,
IN hometown VARCHAR(15)
)
BEGIN

	INSERT INTO users (id, firstname, lastname, email) VALUES
    (id, firstname, lastname, email);
    
    INSERT INTO profiles (user_id, gender, birthday, photo_id, hometown) VALUES
    (id, gender, birthday, photo_id, hometown);
    
    SELECT * FROM hw4.users;
    SELECT * FROM hw4.profiles;

END //

CALL add_user(11, 'Igor', 'Kunovski', 'igor@mail.ru', 'm', '1980-03-23', NULL, 'New York');
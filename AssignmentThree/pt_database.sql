CREATE DATABASE pt_database;

USE pt_database;

CREATE TABLE users (
	userID INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(200) not null unique,
    fullname VARCHAR(200),
    age INT,
    gender ENUM ('male', 'female'),
    height DECIMAL (5,2), -- in cms
    weight DECIMAL (5,2), -- in kg
    email VARCHAR (200),
    PRIMARY KEY (UserID)
);

CREATE TABLE activity (
	activityID INT,
    userID INT,
    type VARCHAR (200),
    duration INT,
    distance DECIMAL (8,2),
    cal_burned DECIMAL (8,2),
    date DATE,
    PRIMARY KEY (activityID),
    FOREIGN KEY (userID) REFERENCES users(userID)
);

CREATE TABLE nutrition (
	nutritionID INT,
    userID INT,
    mealtype VARCHAR (200),
    fooditem VARCHAR (200),
    quantity DECIMAL (8,2),
	calories DECIMAL (8,2),
    date DATE,
    PRIMARY KEY (nutritionID),
    FOREIGN KEY (userID) REFERENCES users(userID)
);

CREATE TABLE goal (
	goalID INT,
    userID INT,
    goaltype VARCHAR (200),
    targetvalue DECIMAL (8,2),
    progress DECIMAL (8,2),
    deadline DATE,
    PRIMARY KEY (goalID),
    FOREIGN KEY (userID) REFERENCES users(userID)
);

-- added CHECK to ensure users are over 18 as calories etc would be very different for younger users.
ALTER TABLE users
MODIFY COLUMN age INT CHECK (age >= 18);

-- data for 8 different users.

INSERT INTO users (username, fullname, age, gender, height, weight, email)
VALUES
	('zed', 'Milo Manheim', 23, 'male', 190.2, 70.2, 'milomanheim@gmail.com'),
    ('addison', 'Meg Donnelly', 24, 'female', 160.2, 48.3, 'megdonnelly@gmail.com'),
    ('bucky', 'Trevor Tordjman', 28, 'male', 185.3, 82.6, 'trevortordjman@gmail.com'),
    ('eliza', 'Kylee Russell', 27, 'female', 160.4, 52.4, 'kyleerussell@gmail.com'),
    ('bonzo', 'James Godfrey', 27, 'male', 190.0, 79.3, 'jamesgodfrey@gmail.com'),
    ('bree', 'Carla Jeffrey', 31, 'female', 160.3, 55.3, 'carlajeffrey@gmail.com'),
    ('lacey', 'Emilia McCarthy', 27, 'female', 170.2, 51.2, 'emiliamccarthy@gmail.com'),
    ('mslee', 'Naomi Sneickus', 50, 'female', 170.4, 58.3, 'naomisneickus@gmail.com');

-- Check all data has been entered correctly.
SELECT * FROM users;

-- alter activtyID, goalID and nutritionID to become auto_incrememnt
ALTER TABLE activity
MODIFY COLUMN activityID INT NOT NULL AUTO_INCREMENT;

ALTER TABLE goal
MODIFY COLUMN goalID INT NOT NULL AUTO_INCREMENT;

ALTER TABLE nutrition
MODIFY COLUMN nutritionID INT NOT NULL AUTO_INCREMENT;

-- activities entered for each user of the database
INSERT INTO activity (userID, type, duration, distance, cal_burned, date)
	VALUES
    (1, 'running', 30, 3.1, 250.3, '2024-01-23'),
    (2, 'walking', 25, 2.5, 128.6, '2024-01-23'),
    (3, 'weights', 45, 0, 380.4, '2024-01-23'),
    (4, 'running', 20, 3.8, 230.7, '2024-01-23'),
    (5, 'running', 45, 8.3, 570.5, '2024-01-23'),
    (6, 'weights', 45, 0, 480.6, '2024-01-23'),
    (7, 'weights', 61, 0, 470.6, '2024-01-23'),
    (8, 'cycling', 45, 15.7, 480.7, '2024-01-23');

SELECT * FROM activity;

-- error made in inserting data twice so deleting duplicate entries from table.
DELETE FROM activity
WHERE activityID IN (8, 9, 10, 11, 12, 13, 14);

-- goal entered for each user of the database
INSERT INTO goal (userID, goaltype, targetvalue, progress, deadline)
	VALUES
		(1, 'marathon', 42.19, 10.2, '2025-03-25'),
        (2, 'race', 5.0, 1.5, '2024-12-13'),
        (3, 'weight loss', 5.0, 1.2, '2024-11-01'),
        (4, 'weight loss', 10.0, 3.5, '2025-01-01'),
        (5, 'race', 5.0, 3.5, '2024-11-03'),
        (6, 'half-marathon', 21.1, 16.0, '2025-02-14'),
        (7, 'weight loss', 7.0, 2.1, '2024-12-01'),
        (8, 'weight loss', 8.5, 4.7, '2025-01-01');

-- looking at all users goals and activites
SELECT *
FROM users u
JOIN goal g ON u.userID = g.userID
JOIN activity a ON u.userID = a.userID
ORDER BY goaltype;

INSERT INTO nutrition (userID, mealtype, fooditem, quantity, calories, date)
	VALUES
		(1, 'lunch', 'bagel', 80.1, 212, '2024-09-23'),
        (2, 'breakfast', 'pancakes', 350.0, 430.0, '2024-09-13'),
        (3, 'dinner', 'pasta', 150.4, 280, '2024-08-13'),
        (4, 'breakfast', 'cheerios', 75.0, 320.2, '2024-09-13'),
        (1, 'breakfast', 'eggs', 75.5, 158.4, '2024-09-24'),
        (5, 'dinner', 'fries', 200, 265.5, '2024-08-13'),
        (3, 'breakfast', 'eggs', 68.0, 158.5, '2024-09-10'),
        (7, 'lunch', 'rice', 125.4, 230.5, '2024-08-17');

INSERT INTO nutrition (userID, mealtype, fooditem, quantity, calories, date)
	VALUES
		(1, 'lunch', 'bagel', 85, 230, '2024-09-24'),
        (1, 'dinner', 'chicken pasta pesto', 410, 670, '2024-09-24'),
        (1, 'snack', 'mars bar', 51.0, 228, '2024-09-24');

-- user wants to add total calories for each day
SELECT SUM(calories), fullname, n.date
FROM nutrition n
JOIN users u
ON n.userID = u.userID
WHERE n.userID = 1
GROUP BY date;

-- user wants to add total calories for one specific day
SELECT SUM(calories) AS daily_calories, fullname, n.date
FROM nutrition n
JOIN users u
ON n.userID = u.userID
WHERE n.userID = 1 AND date = '2024-09-24';

-- user can quickly add an activity they have done
DELIMITER //
CREATE PROCEDURE add_activity(
    IN a_userID INT,
    IN a_type VARCHAR(200),
    IN a_duration INT,
    IN a_distance DECIMAL(8,2),
    IN a_cal_burned DECIMAL(8,2),
    IN a_date DATE
)
BEGIN
    INSERT INTO activity (userID, type, duration, distance, cal_burned, date)
    VALUES (a_userID, a_type, a_duration, a_distance, a_cal_burned, a_date);
END //
DELIMITER ;

-- error made with creating procedure
-- DROP PROCEDURE add_activity;

CALL add_activity (1, 'weights', 45, 0, 380, '2024-09-25');

-- INSERT INTO activity (userID, type, duration, distance, cal_burned, date)
-- 	VALUES
-- 		(6, 'running', 33.5, 5.1, 320, '2024-09-16'),
--         (6, 'running', 45, 7.0, 540, '2024-09-18'),
--         (6, 'running', 90.0, 13.5, 780, '2024-09-21');

-- user wants to know their average km run in a week
SELECT AVG(distance) AS weekly_distance, u.fullname
FROM activity a
JOIN users u
	ON a.userID = u.userID
WHERE a.userID = 6;

-- user adding in nutrition for the day
DELIMITER //
CREATE PROCEDURE add_nutrition(
    IN u_userID INT,
    IN u_mealtype VARCHAR(200),
    IN u_fooditem VARCHAR(200),
    IN u_quantity DECIMAL(8,2),
    IN u_calories DECIMAL(8,2),
    IN u_date DATE
)
BEGIN
    INSERT INTO nutrition (userID, mealtype, fooditem, quantity, calories, date)
    VALUES (u_userID, u_mealtype, u_fooditem, u_quantity, u_calories, u_date);
END //
DELIMITER ;

CALL add_nutrition (2, 'lunch', 'tomato soup', 150, 230, '2024-09-20');
CALL add_nutrition (6, 'breakfast', 'eggs on toast', 200, 380, '2024-09-17');

-- user wants to see a snapshot of their week
SELECT u.fullname, a.type, a.duration, n.calories, a.cal_burned, a.date
FROM activity a
LEFT JOIN users u
	ON a.userID = u.userID
LEFT JOIN nutrition n
	ON a.userID = n.userID
WHERE a.date BETWEEN '2024-09-16' AND '2024-09-22' AND u.userID = 6
ORDER BY 1, 2, 3, 4, 5, 6;


-- user wants to see all activity types they have completed
SELECT userID, type AS activities, CAST(AVG(duration) AS DECIMAL(5,1)) AS avg_duration
FROM activity
GROUP BY 1, 2
HAVING userID = 6;

-- user wants to view the types of food they are eating
SELECT DISTINCT fooditem
FROM nutrition
WHERE userID = 1;


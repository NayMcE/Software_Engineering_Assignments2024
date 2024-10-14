CREATE DATABASE nutrition;
USE nutrition;

CREATE TABLE recipes (
	recipe_id INT NOT NULL AUTO_INCREMENT,
    recipe_name VARCHAR (200),
    calories INT,
    protein INT,
    carbs INT,
    fat INT,
    meal_type VARCHAR (200),
    instructions VARCHAR (200),
    ingredients VARCHAR(200),
    PRIMARY KEY (recipe_id, meal_type)
);

DELIMITER //
CREATE PROCEDURE add_meal(
    IN m_recipe_name VARCHAR(200),
    IN m_calories INT,
    IN m_protein INT,
    IN m_carbs INT,
    IN m_fat INT,
    IN m_meal_type VARCHAR(200),
    IN m_instructions VARCHAR(200),
    IN m_ingredients VARCHAR(200)
)
BEGIN
    INSERT INTO recipes (recipe_name, calories, protein, carbs, fat, meal_type, instructions, ingredients)
    VALUES (m_recipe_name, m_calories, m_protein, m_carbs, m_fat, m_meal_type, m_instructions, m_ingredients);
END //
DELIMITER ;


CALL add_meal ('chocolate protein overnight oats', 346, 22, 36, 15, 'breakfast', 'In an airtight glass jar combine ingredients and mix well. Place in the fridge overnight.', '35g oats, 2tbsp chia seeds, 1tsp vanilla extract, 1/2 scoop of chocolate protein powder, 1/2 cup of milk');

SELECT * FROM recipes;

CALL add_meal('Pumpkin Chia protein pudding', 306, 24, 26, 12, 'breakfast', 'In an airtight container combine ingredients and mix well. Place in the fridge overnight.', '1 scoop vanilla protein powder, 1/3 cup pumpkin puree, 2 1/2 tbsp chia seeds, 1 cup of milk, 1 tsp vanilla, 1/2 tsp cinnamon');
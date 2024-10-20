CREATE DATABASE nutrition;
USE nutrition;

CREATE TABLE recipes (
	recipe_id INT NOT NULL AUTO_INCREMENT,
    recipe_name VARCHAR (200),
    meal_type VARCHAR (200),
    instructions VARCHAR (200),
    ingredients VARCHAR(200),
    PRIMARY KEY (recipe_id)
);

CREATE TABLE nutri_info (
	recipe_id INT NOT NULL,
    calories INT,
    protein INT,
    carbs INT,
    fat INT,
    FOREIGN KEY (recipe_id) REFERENCES recipes (recipe_id)
);

DELIMITER //
CREATE PROCEDURE add_meal(
    IN m_recipe_name VARCHAR(200),
    IN m_meal_type VARCHAR(200),
    IN m_instructions VARCHAR(600),
    IN m_ingredients VARCHAR(600)
)
BEGIN
    INSERT INTO recipes (recipe_name, meal_type, instructions, ingredients)
    VALUES (m_recipe_name, m_meal_type, m_instructions, m_ingredients);
END //
DELIMITER ;

DROP PROCEDURE add_meal;

ALTER TABLE recipes
MODIFY COLUMN instructions VARCHAR(600);

ALTER TABLE recipes
MODIFY COLUMN ingredients VARCHAR(600);


CALL add_meal ('chocolate protein overnight oats', 'breakfast', 'In an airtight glass jar combine ingredients and mix well. Place in the fridge overnight.', '35g oats, 2tbsp chia seeds, 1tsp vanilla extract, 1/2 scoop of chocolate protein powder, 1/2 cup of milk');

CALL add_meal('Pumpkin Chia protein pudding', 'breakfast', 'In an airtight container combine ingredients and mix well. Place in the fridge overnight.', '1 scoop vanilla protein powder, 1/3 cup pumpkin puree, 2 1/2 tbsp chia seeds, 1 cup of milk, 1 tsp vanilla, 1/2 tsp cinnamon');
CALL add_meal('Veggie Stir-Fry', 'dinner', 'Heat oil in a pan over medium heat. Add minced garlic and ginger, sauté for 1 minute. Add chopped vegetables and stir-fry for 5-7 minutes. Stir in soy sauce and cook for another 2 minutes. Sprinkle with sesame seeds before serving.', 'Broccoli (1 cup), Bell pepper (1), Carrot (1), Soy sauce (2 tbsp), Garlic (2 cloves, minced), Ginger (1 tsp, minced), Olive oil (1 tbsp), Sesame seeds (1 tsp)');
CALL add_meal ('Grilled Chicken Salad', 'lunch', 'Season the chicken breast with salt and pepper, grill the chicken for 6-7 minutes on each side. In a bowl, toss mixed greens, halved cherry tomatoes, and sliced cucumber. Drizzle with olive oil and lemon juice, and add the sliced chicken on top.', 'Chicken breast (200g), Mixed greens (2 cups), Cherry tomatoes (10), Cucumber (1/2), Olive oil (1 tbsp), Lemon juice (1 tbsp), Salt (to taste), Pepper (to taste)');

SELECT *
FROM recipes;





# Assignment Four - API's

## Nutrition Database

### The concept of this application

This is my nutrition database that compliments my Personal Trainer database.
The idea is that a Personal Trainer can send recipe ideas to the client for them to
choose from. Whilst there are more ways to utilise the database with nutritional 
information, this demonstrates how a client can view their recipe choices and delete
ones they would prefer not to have as a set meal.

### How to run this application

* First copy the "nutrition_db.sql" script to create the database
* Enter your username and password into the config file. 
* Run the "db_utils" file to check the database connection is running correctly. You will need to import mysql.connector from this file.
* Then run the "app" file to connect to Flask, you will need to import Flask from this file.
* Navigate to the "main" file where you will need to import requests before running the file.
* Finally run the "main" file and follow the instructions. You will have a choice as to viewing all your recipes or viewing them by meal type. From there you can delete any recipe by id if you don't like the look of it. It will then return to you your new recipe collection with the deleted recipe removed.

Hope you enjoy.
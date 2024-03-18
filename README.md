# COMP3005_A3
Assignment 3, Question 1 for Carleton Universities COMP3005 

# Setting up the DB
  - Right click databases, hover over create > databases
  - name the database A3Q1 (or something of your choosing, just update the database info in python)
  - open the query tool, click open file, and import the a3q1 sql file.
  - run the file to create and populate the table with sample data in pgadmin4

# running the application
  - in a command line interface, ensure you have python installed and run pip install psycopg2
  - then open the 3005a3.py folder and modify the initial conn statement to connect the database (ln 4 to ln 8)
  - run the file using your preferred python interpreter
  - to see changes made, use SELECT * FROM students; in pgAdmin

# demo video

https://youtu.be/ZAwQzQuD4AQ

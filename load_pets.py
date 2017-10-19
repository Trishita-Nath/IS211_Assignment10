import sqlite3 as sql
import sys

con = None

try:
    con = sql.connect('pets.db')
    cur = con.cursor()    
    cur.executescript(""" 
    	Drop table  if exists person;
    	Drop table  if exists pet;
    	Drop table  if exists person_pet;
    	CREATE TABLE person( id INTEGER PRIMARYKEY, first_name TEXT, last_name TEXT, age INTEGER);
    	CREATE TABLE pet( id INTEGER PRIMARYKEY, name TEXT, breed TEXT, age INTEGER, dead INTEGER);
    	CREATE TABLE person_pet( person_id INTEGER, pet_id INTEGER);
    	INSERT INTO person VALUES(1, 'James', 'Smith', 41);
        INSERT INTO person VALUES(2, 'Diana', 'Greene', 23);
        INSERT INTO person VALUES(3, 'Sara', 'White', 27);
        INSERT INTO person VALUES(4, 'William', 'Gibson', 23);
        INSERT INTO pet VALUES(1, 'Rusty', 'Dalmation', 4, 1);
        INSERT INTO pet VALUES(2, 'Bella', 'Alaskan Malamute', 3, 0);
        INSERT INTO pet VALUES(3, 'Max', 'Cocker Spaniel', 1, 0);
        INSERT INTO pet VALUES(4, 'Rocky', 'Beagle', 7, 0);
        INSERT INTO pet VALUES(5, 'Rufus', 'Cocker Spaniel', 1, 0);
        INSERT INTO pet VALUES(6, 'Spot', 'Bloodhound', 2, 1);
        INSERT INTO person_pet VALUES(1, 1);
        INSERT INTO person_pet VALUES(1, 2);
        INSERT INTO person_pet VALUES(2, 3);
        INSERT INTO person_pet VALUES(2, 4);
        INSERT INTO person_pet VALUES(3, 5);
        INSERT INTO person_pet VALUES(4, 6);
     """)
    con.commit()
                  
    
except sql.Error, e:
    
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    
    if con:
		con.close()
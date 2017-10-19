import sqlite3 as sql
import sys

con = None

try:
    con = sql.connect('pets.db')
    con.row_factory = sql.Row
    while True:
        personID = raw_input('Please enter an ID number: ')
        if personID == '-1':
            sys.exit()
        else:
            try:
                personID = int(personID)
            except:
                print "Error, please input a number"
                continue

        cur = con.cursor()
        cur.execute("SELECT * FROM person WHERE id =?", [(personID)])
        row = cur.fetchone()

        if row == None:
            print 'Not a valid ID number. Try Entering another ID.'
            continue

        print row['first_name'] + ' ' + row['last_name'] + ' is ' + str(row['age']) + ' years old.'


        for row in con.execute(
            "SELECT * FROM person_pet WHERE person_id =?", [(personID)]):

            for name in con.execute(
                "SELECT * FROM person WHERE id =?", [(personID)]): owner = name['first_name'] + ' ' + name['last_name']

            for eachrow in con.execute(
                "SELECT * FROM pet WHERE id =?", [(row['pet_id'])]):

                if eachrow['dead'] == 0:
                    print ('- ' + owner + ' owns ' + eachrow['name'] + ', a ' + eachrow['breed'] + ' who is ' + str(eachrow['age']) + ' years old.')
                else:
                    print ('- ' + owner + ' owned ' + eachrow['name'] + ', a ' + eachrow['breed'] + ' who was ' + str(eachrow['age']) + ' years old.')


except sql.Error as e:
    print "Closing."
    print "Error: %s " % e.args[0]
    sys.exit(1)

finally:
    if con:
        con.close()

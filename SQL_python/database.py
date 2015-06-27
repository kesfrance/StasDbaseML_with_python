#!/usr/bin/python3
#
#  
# Author: Francis Kessie
#
"""
A program that demos how to store and retrieve data from a RDMS.

The programs stores and retrieves the weather and climate data of some 
cities in the USA. At start up the user is prompted to select from the options 
the kind of record he would like to view. 
"""

import sqlite3 as lite
import pandas as pd
import sys

#creates a new database if it doesnt already exists
with lite.connect('usa_weather_climate.db') as con:
   
    #create a cursor object to execute SQL commands
    cur = con.cursor()


    #Create cities and weather tables
    cur.executescript("""DROP TABLE IF EXISTS cities;
                  CREATE TABLE cities (name text, state text);""")

    cur.executescript("""DROP TABLE IF EXISTS weather;
                  CREATE TABLE weather(city text, year integer, 
                   warm_month text, cold_month text, average_high integer);""")
       
 
    #insert values into tables
    cities = (('New York City', 'NY'),
         ('Boston', 'MA'),
         ('Chicago', 'IL'),
         ('Miami', 'FL'),
         ('Dallas', 'TX'),
         ('Seattle', 'WA'),
         ('Portland', 'OR'),
         ('San Francisco', 'CA'),
         ('Los Angeles', 'CA'),
         ('Washington', 'DC'),
         ('Houston', 'TX'),
         ('Las Vegas', 'NV'),
         ('Atlanta', 'GA'))
         
    weather = (('New York City', 2013, 'July', 'January', 62),
          ('Boston', '2013', 'July', 'January', 59),
          ('Chicago', '2013', 'July', 'January', 59),
          ('Miami', '2013', 'August', 'January', 84),
          ('Dallas', '2013', 'July', 'January', 77),
          ('Seattle', '2013', 'July', 'January', 61),
          ('Portland', '2013', 'July', 'December', 63),
          ('San Francisco', '2013', 'September', 'December', 64),
          ('Los Angeles', '2013', 'September', 'December', 75),
          ('Washington', 2013, 'July', 'January', 87),
          ('Houston', 2013, 'July', 'January', 96),
          ('Las Vegas', 2013, 'July', 'December', 106), 
          ('Atlanta', 2013, 'July', 'January', 90))

    cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
    cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather)
    
    
    def get_data(months):
        """
        Join tables and retieves warmest cities according to month selected
        """
        cur.execute("SELECT city, average_high, state, warm_month \
        FROM cities INNER JOIN weather ON city = name WHERE warm_month =="+"'"+months+"'"+"")
        rows = cur.fetchall()    
        header = [name[0] for name in cur.description]
        df = pd.DataFrame(rows, columns=header)
        preamble = "The cities that are warmest in "+ months + " are:"
    
        #return statement showing warmest cities and corresponding states
        statement = ''
        for i in range(0, len(df.index)):
            cities_states = df.iloc[i][0] +", "+ df.iloc[i][2]
            statement = statement + ' '
            statement = statement + cities_states + ","              
        return ("{2}{0}{1}".format(statement.rstrip(","), ".", preamble))

    
    message1 = "Hi. You can view cities in the USA by their warmest months with this program!."
    options = ["July", "August", "September"]  
    prompt = ", ".join(options)
    greetings = "Bye for now, see yaa!!"
    print(" ")
    print(message1)
    print(" ")
        
    while True:
          inp = input('I have records for ' + prompt +"(Select one month or press Enter to quit): ")
          if not inp:
             print(" ")
             print(greetings)
             break    
             
          else:
              try:
                  months = inp.capitalize()
                  print(" ")                             
                  print(get_data(months)) 
                  print("*"*60)                    
                  print(" ") 
                  
                  options.remove(months)
                  prompt = ", ".join(options)
              except ValueError:
                  print("Invalid selection!.")
                  print(" ")
                  continue
          
          while True:
              inp = input('Check out another month. I have ' + prompt +"(Select one or press Enter to quit): ")
              if not inp:
                  print(" ")
                  print(greetings)
                  sys.exit()
                          
              try:
                  months = inp.capitalize()
                  print(" ")
                  print(get_data(months)) 
                  print("*"*60)                    
                  print(" ")   
                  options.remove(months) 
              except ValueError:
                  print("Not a valid selection or have been viewed already!.")
                  print("*"*60)                    
                  print(" ") 
                  continue
                            
              prompt = ", ".join(options)
              while True:
                      inp = input('One more to go. Select and view ' + prompt +"(or press Enter to quit): ")
                      if not inp:
                          print(" ")
                          print(greetings)
                          sys.exit()
                      else:
                          
                          try:
                              months = inp.capitalize()
                              print(" ")
                              print(get_data(months))
                              print("*"*60)                    
                              print(" ") 
                              print("Thats all for now. Goodbye!!") 
                              sys.exit()
                          except ValueError:
                              print("Not a valid selection or have been viewed already")
                              print("*"*60)                    
                              print(" ") 
                              continue
          

#!/usr/bin/env python  
  
import os  
import time  
import datetime  
import glob  
import MySQLdb  
from time import strftime  
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()
  
  
#Valtozok megadasa MySQLnek 
db = MySQLdb.connect(host="localhost", user="root", passwd="mysql-jelszo", db="sensor") # replace password with your password  
cur = db.cursor()  
  
def dateTime(): # UNIX ido beallitasa  
        secs = float(time.time())  
        secs = secs*1000  
        return secs  
  
def tempRead(): #homerseklet kiolvasasa, float 3 decimalis  
        degrees = float('{0:.3f}'.format(sense.get_temperature()-10.5))
        return degrees  
  
def pressRead():#legnyomas kiolvasasa, float 3 decimalis   
        pascals = float('{0:.3f}'.format(sense.get_pressure()))  
        return pascals  
  
def humidityRead(): #paratartalom kiolvasasa, float 3 decimalis   
        humidity = float('{0:.3f}'.format(sense.get_humidity()))  
        return humidity  
  
secs = dateTime()  
temperature = tempRead()  
pressure = pressRead()  
humidity = humidityRead()  
  
sql = ("""INSERT INTO bmesensor (datetime,temperature,pressure,humidity) VALUES (%s,%s,%s,%s)""", (secs, temperature, pressure, humidity))  
  
try:  
    print "Adatbazisba iras..."  
    cur.execute(*sql)  
    db.commit()  
    print "Iras kesz"  
  
except:  
    db.rollback()  
    print "Nem sikerult"  
  
cur.close()  
db.close()  
  
print secs  
print temperature  
print pressure  
print humidity  

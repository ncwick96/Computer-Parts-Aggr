# This script pulls computer part info from multiple sites and compares them
# CNA 330
# Group Project with PSwift
# Nathan Wick, ncwick@student.rtc.edu/ncwick96@gmail.com
#
# Code referenced from: https://github.com/RTCedu/CNA330/JobHunter/JobHunter.py
#                       https://github.com/RTCedu/CNA336/Spring2018/Sql.py
#
import mysql.connector
import sys
import json
import urllib.request
import os
import time

conn = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='Computer_Parts')
c = conn.cursor()
c.execute("CREATE TABLE FIXTEST(id INTEGER PRIMARY KEY, Date TEXT, Class TEXT, Name TEXT, Model INTEGER, "
          "Manufacturer TEXT, Quantity INTEGER, Price INTEGER, Site TEXT)")

# Creates test entry to ensure things are going as they should be.
c.execute("INSERT INTO Computer_Parts VALUES(0, '11/9/18', 'RAM',"
          " 'Corsair 64gb RAM 3200', '224873', 'Corsair', '64','550.98', 'Amazon')")
c.close()


# {                 Planning on using these in boolean ops later, may delete if better method found
# Classes for db table, and var assignment for later processing
a = "RAM"; b = "Heat_Sink"; c = "CPU"; d = "PSU"; e = "Mother_Board"

# Sites for db table, and var assignment for later processing
am = "Amazon"; bb = "Best_Buy"; f = "Frys"; ne = "New_Egg"
# }

# Runs with exit code 0, no errors, but does not create DB, PSwift, compare with your JH script please.
# Work in progress below

counter = 0
query = "#INSERT URL(S) HERE#"
jsonpage = 0
try:
    contents = urllib.request.urlopen(query)
    response = contents.read()
    jsonpage = json.loads(response)
except:
    pass
    time.sleep(1)
data = json.dumps(jsonpage['data'])
for i in data:
    conn.c(
        "INSERT INTO Computer_Parts(#VAR STUFF HERE#+#TABLE VALUES/DATA#)"
    )

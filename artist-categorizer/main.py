import os
import sqlite3 as sql
import requests

# Set Working Dir (binding to config planned, for now it just goes up a directory.)
os.chdir("../")

# Connect to DB
con = sql.connect('artistinfo.db')

# More Planned :3

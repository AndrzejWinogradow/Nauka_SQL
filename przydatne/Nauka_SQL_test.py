#! /usr/bin/env python3
# -*- coding: utf-8 -*-


# import sqlite3

from sqlitedict import SqliteDict
mydict = SqliteDict('./my_db.sqlite', autocommit=True)
mydict['some_key'] = any_picklable_object
print(mydict['some_key'])  # prints the new value
for key, value in mydict.iteritems():
    print(key, value)
print(len(mydict)) # etc... all dict functions work
mydict.close()
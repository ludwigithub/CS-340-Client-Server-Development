#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 22:37:46 2023

@author: deonneludwig_snhu
"""

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        # USER = 'aacuser'
        # PASS = 'snhu1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32112
        DB = 'aac'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        print ("Connection Successful") # confirm connection to database
        
# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary            
            return True # confirm insert of data successful
        else:
            return False # confirm insert of data not successful
            raise Exception("Nothing to save, because data parameter is empty")
        
# Create method to implement the R in CRUD.
    def read(self, data=None):
        if data is not None: #if data exits
            readList = self.database.animals.find(data)  # read data in file/data should be dictionary            
        else:
           readList = self.database.animals.find() # if none return an empty list
        return readList 
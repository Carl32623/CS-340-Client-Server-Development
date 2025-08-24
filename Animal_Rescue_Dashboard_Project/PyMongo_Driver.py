#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 26 13:13:28 2025
Updated on Sat Aug 02 16:58:22 2025

@author: carllalonde_snhu
"""

from pymongo import MongoClient
from bson.objectid import ObjectId
from pprint import pprint


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Initializing the MongoClient. This helps to access the MongoDB
        # databases and collections. This is hard-wired to use the aac database,
        # the animals collection, and the aac user. Definitions of the connection
        # string variables are unique to the individual Apporto environment.

        # Connection Variables
        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32989
        DB = 'AAC'
        COL = 'animals'

        # Initialize Collections
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client['%s' % DB]
        self.collection = self.database['%s' % COL]

        # Insert a document into the MongoDB collection

    def create(self, data):
        if data is not None and isinstance(data, dict):
            try:
                insert_result = self.collection.insert_one(data)
                if insert_result.acknowledged:
                    print(f"Document inserted with _id: {insert_result.inserted_id}")
                    return True
                else:
                    print("Insert was not acknowledged by MongoDB.")
                    return False
            except Exception as e:
                print(f"Error inserting data: {e}")
                return False
        else:
            print("Invalid data.")
            return False

    # Find and Read a document
    def read(self, query):
        if query is not None and isinstance(query, dict):
            try:
                results = list(self.collection.find(query))
                if results:
                    print(f"{len(results)} document(s) found:")
                    for doc in results:
                        pprint(doc)
                else:
                    print("No documents found matching query.")

                return results

            except Exception as e:
                print(f"Error reading data: {e}")
                return []
        else:
            print("Invalid query.")
            return []

    # Update a document
    def update(self, query, updatedValues):
        if query is not None and updatedValues is not None:
            if isinstance(query, dict) and isinstance(updatedValues, dict):
                try:
                    results = self.collection.update_many(query, {'$set': updatedValues})
                    print(f"Found {results.matched_count} document(s).")
                    print(f"Updated {results.modified_count} document(s).")
                    return results.modified_count
                except Exception as e:
                    print(f"An error occurred during update: {e}")
                    return 0
            else:
                print("Both query and updatedValues must be dictionaries.")
                return 0
        else:
            print("Query and updated values cannot be empty.")
            return 0

    # Delete a document from the collection
    def delete(self, query):
        if query is not None:
            if isinstance(query, dict):
                try:
                    results = self.collection.delete_many(query)
                    print(f"Deleted {results.deleted_count} document(s).")
                    return results.deleted_count
                except Exception as e:
                    print(f"An error occurred during delete: {e}")
                    return 0
            else:
                print("Query must be a dictionary.")
                return 0
        else:
            print("Query cannot be empty.")
            return 0

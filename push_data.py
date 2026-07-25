import os
import sys
import json

from dotenv import load_dotenv

load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URL")

import certifi
ca=certifi.where()


import pandas as pd
import pymongo 
import numpy as np

from  networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class Networkdataextract():
    def __init__(self) -> None:
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
        
    def cv_to_json_converter(self,file_path):
        try:
            data=pd.read_csv(file_path)
        
            data.reset_index(drop=True,inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            
            return records     
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
        
    def insert_data_to_mongo(self,records,database,collection):
        try:
            self.database=database
            self.records=records
            self.collection=collection
            
            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
            self.database=self.mongo_client[self.database]
            
            self.collection=self.database[self.collection]
            
            self.collection.insert_many(self.records)
            return len(self.records)
            
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        


if __name__=='__main__':
    FILE_PATH="/Users/shreyashpawade/Documents/Network security/Network_Data/phisingData.csv"
    DATABASE="SHREYASH"
    COLLECTION="Networkdata"
    network_obj=Networkdataextract()
    records=network_obj.cv_to_json_converter(file_path=FILE_PATH)
    print(records)
    
    no_of_records=network_obj.insert_data_to_mongo(records,DATABASE,COLLECTION)
    print(no_of_records)
    
    
        
        
             
        
        
    


# -*- coding: utf-8 -*-
"""
Created on Tue May 19 22:45:16 2020

@author: S
"""

import json
import sqlite3

DB_Name = "IoT_DataBase.db"


class DatabaseManager():
    def __init__(self):
        self.conn = sqlite3.connect(DB_Name, isolation_level=None)
        self.conn.execute('pragma foreign_keys = on')
        self.cur = self.conn.cursor()

    def add_del_update_db_record(self, sql_query, args=()):
        self.cur.execute(sql_query, args)
        return

    def select_db_record(self, sql_query, args=()):
        self.cur.execute(sql_query, args)
        return self.cur.fetchall();

    def __del__(self):
        self.cur.close()
        self.conn.close()

    @staticmethod
    def getdataSet(sqlText):
        dbObj = DatabaseManager()
        rows = dbObj.select_db_record(sqlText)
        del dbObj
        return rows


def read_temperature_data():
    db = DatabaseManager()
    return db.select_db_record("select * from Temperature_Data")


def read_humidity_data():
    db = DatabaseManager()
    return db.select_db_record("select * from Humidity_Data")


def Temperature_Data_Handler(jsonData):
    json_Dict = json.loads(jsonData)
    SensorID = json_Dict['Sensor_ID']
    Date_Time = json_Dict['Date']
    Temperature = float(json_Dict['Temperature'])
    TemperatureLevel = json_Dict['TemperatureLevel']

    dbObj = DatabaseManager()
    dbObj.add_del_update_db_record(
        "insert into Temperature_Data(SensorID,Date_Time,Temperature,TemperatureLevel) values(?,?,?,?) ",
        [SensorID, Date_Time, Temperature, TemperatureLevel])
    del dbObj
    print("Inserted Temperature Data into Database")
    print("")


def Humidity_Data_Handler(jsonData):
    json_Dict = json.loads(jsonData)
    SensorID = json_Dict['Sensor_ID']
    Date_Time = json_Dict['Date']
    Humidity = float(json_Dict['Humidity'])
    HumidityLevel = json_Dict['HumidityLevel']

    dbObj = DatabaseManager()
    dbObj.add_del_update_db_record(
        "insert into Humidity_Data(SensorID,Date_Time,Humidity,HumidityLevel) values(?,?,?,?) ",
        [SensorID, Date_Time, Humidity, HumidityLevel])
    del dbObj
    print("inserted Humidity Data into Database")
    print("")


def Acceleration_Data_Handler(jsonData):
    json_Dict = json.loads(jsonData)
    SensorID = json_Dict['Sensor_ID']
    Date_Time = json_Dict['Date']
    print('************', Date_Time)
    accX = float(jsonData['accX'])
    accY = float(jsonData['accY'])
    accZ = float(jsonData['accZ'])

    dbObj = DatabaseManager()
    dbObj.add_del_update_db_record("insert into Acceleration_Data(SensorID,Date_Time,accX,accY,accZ)values(?,?,?,?,?) ",
                                   [SensorID, Date_Time, accX, accY, accZ])
    print("inserted Acceleration Data into Database")
    print("")


def sensor_Data_Handler(Topic, jsonData):
    if Topic == "Home/BedRoom/DHT1/Temperature":
        Temperature_Data_Handler(jsonData)
    elif Topic == "Home/BedRoom/DHT1/Humidity":
        Humidity_Data_Handler(jsonData)
    elif Topic == "Home/BedRoom/DHT1/Acceleration":
        Acceleration_Data_Handler(jsonData)

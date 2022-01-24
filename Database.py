# The use of this class is to initiate my database
# Keeping database initiator separate


import sqlite3

conn = sqlite3.connect('quizDB.db')
cursor = conn.cursor()


#  CREATE TABLES

#   MODULES TABLE
module_table = """CREATE TABLE IF NOT EXISTS modules (
                    module_ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                    moduleName TEXT, 
                    moduleDesc TEXT)"""

#   QUESTIONS TABLE
question_table = """CREATE TABLE IF NOT EXISTS questions (
                    question_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    module INTEGER,
                    qType INTEGER,
                    question TEXT,
                    answer TEXT,
                    options TEXT,
                    feedback TEXT,
                    FOREIGN KEY(module) REFERENCES modules (moduleName))"""

#   RESULTS TABLE
results_table = """CREATE TABLE IF NOT EXISTS reuslts (
                    result_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    module_ID INTEGER,
                    score INTEGER,
                    date BlOB,
                    FOREIGN KEY(module_ID) REFERENCES modules (module_ID))"""

cursor.execute(module_table)
cursor.execute(question_table)
cursor.execute(results_table)

#  GET MODULE ID AND NAMES
cursor.execute('SELECT module_ID,moduleName FROM modules')
moduleList = cursor.fetchall()


#  JUST MODULE NAMES
cursor.execute('SELECT moduleName FROM modules')
moduleNamesList = cursor.fetchall()

#  JUST MODULE NAMES
cursor.execute('SELECT moduleDesc FROM modules')
moduleDescList = cursor.fetchall()

conn.commit()
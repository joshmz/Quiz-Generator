import sqlite3

conn = sqlite3.connect('quizDB.db')
cursor = conn.cursor()


#  CREATE TABLES
module_table = """CREATE TABLE IF NOT EXISTS modules (
                    module_ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                    moduleName TEXT, 
                    moduleDesc TEXT)"""

question_table = """CREATE TABLE IF NOT EXISTS questions (
                    question_ID INTEGER PRIMARY KEY,
                    module INTEGER,
                    question TEXT,
                    answer TEXT,
                    options BLOB,
                    FOREIGN KEY(module) REFERENCES modules (moduleName))"""

cursor.execute(module_table)
cursor.execute(question_table)

#  GET MODULE ID AND NAMES
cursor.execute('SELECT module_ID,moduleName FROM modules')
moduleList = cursor.fetchall()


#  JUST MODULE NAMES
cursor.execute('SELECT moduleName FROM modules')
moduleNamesList = cursor.fetchall()

conn.commit()
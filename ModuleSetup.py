import Database as db

class MakeModule:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def insert_data(self):
        module = [
            self.name,
            self.description
        ]
        db.cursor.execute('INSERT INTO modules (moduleName, moduleDesc) VALUES (?,?)', module)
        db.conn.commit()


def create_module():
    name = input("What is the name of the module: ")
    description = input("Enter a short description: ")
    ModuleInstance = MakeModule(name, description)
    ModuleInstance.insert_data()
    print("Module Inserted")
    
import Database as db

def choose_module():
    module_check = True
    while module_check:
        for i in db.moduleList:
            print(*i)
        module_input = int(input(f"Enter module number: [1-{len(db.moduleList)}]: "))
        module_check = False
    makeQuiz(module_input)

def makeQuiz(module):
    moduleID = module-1
    moduleName = (''.join(db.moduleNamesList[moduleID]))
    print("Chosen module:", moduleName)
    #Get questions in that module
    db.cursor.execute(f"SELECT * FROM questions WHERE module = '{moduleName}'")
    questionsList = db.cursor.fetchall()

    db.conn.commit()
    print(questionsList)

choose_module()
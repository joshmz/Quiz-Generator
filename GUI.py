from tkinter import *
from tkinter import ttk
import Database as db
import ModuleSetup as ms
import QuestionSetup as qs

def exitWin():
    exit()

#   Window metadata
win = Tk()
win.title("QUIZ GENERATOR")

#   FRAMES
mainMenu = Frame(win)
takeQuiz = Frame(win)
adminTools = Frame(win)
moduleSetup = Frame(win)
QuestionSetup = Frame(win)

def addToDatabase(*args):
    #   Do this for module Insert
    if (len(args) == 2):
        ms.create_module(*args)
    #   Do this for Question insert
    #   Multiple Choice
    elif (len(args) != 2) and clicked.get() == qs.questionTypes[0]:
        qs.multiple_choice(args[0],args[1],args[2],args[3])
    #   True False
    elif (len(args) != 2) and clicked.get() == qs.questionTypes[1]:
        qs.true_false(args[0],args[1],args[2],args[3])
    #   Best Match
    else:
        qs.best_match(args[0],args[1],args[2])

def differenciateQuestion(type,module,ques,ans):
    print(type)
    answerList = [ans]
    if type == qs.questionTypes[0]:
        def addAnswer():
            if len(answerList) < 4:
                answerList.append(falseAnswer.get())
                Label(possibleAns,text=falseAnswer.get()).pack()
            else:
                ansListStr = '/'.join(answerList)
                print(ansListStr)
                addToDatabase(module,ques,ans,str(ansListStr))
                possibleAns.destroy()

        falseAnswerCount = 1

        possibleAns = Tk()
        possibleAns.title("MULTIPLE CHOICE")

        Label(possibleAns,text=f"Enter A False Answer: ({falseAnswerCount})").pack()
        falseAnswer = Entry(possibleAns, width=50,borderwidth=5)
        falseAnswer.pack()

        nextButton = Button(possibleAns,text='Next',command= addAnswer).pack()

        
        Label(possibleAns,text=answerList[0]).pack()


        possibleAns.mainloop()

    elif type == qs.questionTypes[1]:
        confirm = Tk()
        confirm.title("TRUE/FALSE")
        confirm.geometry("300x100")
        
        def addAnswer():
            if (ans == "True"):
                answerList.append("False")
                ansListStr = '/'.join(answerList)
                addToDatabase(module,ques,ans,str(ansListStr))
                confirm.destroy()
            elif (ans == "False"):
                answerList.append("True")
                answerList.append("False")
                ansListStr = '/'.join(answerList)
                addToDatabase(module,ques,ans,str(ansListStr))
                confirm.destroy()
            else:
                Label(confirm, text=f"{ans} is not True/False").pack()
                Button(confirm,text='Back',command= lambda: confirm.destroy()).pack()

        Label(confirm, text=f"The statement is {ans}?").pack()
        nextButton = Button(confirm,text='Next',command= addAnswer).pack()
        
        confirm.mainloop()
    else:
        termList = []
        defList = []
        makeTerms = Tk()
        makeTerms.title("BEST MATCH")

        Label(makeTerms, text=f"Term: ").pack()
        termInput = Entry(makeTerms, width=50, borderwidth=5)
        termInput.pack()
        Label(makeTerms, text=f"Definition: ").pack()
        defInput = Entry(makeTerms, width=50, borderwidth=5)
        defInput.pack()

        def addAnswer():
            if len(termList) < 4:
                termList.append(termInput.get())
                defList.append(defInput.get())
                Label(makeTerms,text=f'{termInput.get()} -> {defInput.get()}')
            else:
                termListStr = '/'.join(termList)
                defListStr = '/'.join(defList)
                addToDatabase(module,termListStr,defListStr)
                makeTerms.destroy()

        nextButton = Button(makeTerms,text='Next',command= addAnswer).pack()

        makeTerms.mainloop()


def swap(frame):
    frame.tkraise()

for frame in (mainMenu, 
            takeQuiz, 
            adminTools,
            moduleSetup,
            QuestionSetup):
    frame.grid(row=0,column=0, sticky='news')

#----------------------------------------------------
#   MAIN MENU
Button(mainMenu, text="Take Quiz", command= lambda: swap(takeQuiz)).pack()
Button(mainMenu, text="Administration Tools", command= lambda: swap(adminTools)).pack()
exitButton = Button(mainMenu, text="Exit", command=exitWin)
#----------------------------------------------------
#   QUIZ WINDOW

#----------------------------------------------------
#   ADMIN WINDOW
modButton = Button(adminTools, text="Make Module", command= lambda: swap(moduleSetup))
modButton.pack()
quesButton = Button(adminTools, text="Make Question", command= lambda: swap(QuestionSetup))
quesButton.pack()
backButton = Button(adminTools,text="Back", command= lambda: swap(mainMenu)).pack()
#----------------------------------------------------
#   MODULE SETUP PAGE
modLabal = Label(moduleSetup,text="Module Name").pack()
modName = Entry(moduleSetup, width=50,borderwidth=5)
modName.pack()
descLabel = Label(moduleSetup, text="Module Description").pack()
modDesc = Entry(moduleSetup,width=50,borderwidth=5)
modDesc.pack()

Button(moduleSetup,text="Register Module",command= lambda: addToDatabase(modName.get(), modDesc.get())).pack()
Button(moduleSetup, text="Back", command= lambda:swap(adminTools)).pack()

#----------------------------------------------------
#   QUESTION SETUP PAGE
clicked = StringVar()
clicked.set(qs.questionTypes[0])
chosenModule = StringVar()
chosenModule.set("Choose Module")

qTypeLabel = Label(QuestionSetup,text="Choose Question Type").pack()
qTypeOptions = OptionMenu(QuestionSetup, clicked, *qs.questionTypes)
qTypeOptions.pack()
swap(moduleSetup)
qModuleLabel = Label(QuestionSetup,text="What Module Is This Question For?").pack()
qModule = OptionMenu(QuestionSetup, chosenModule, *db.moduleNamesList)
qModule.pack()
quesLabel = Label(QuestionSetup,text="Enter Question").pack()
ques = Entry(QuestionSetup, width=50,borderwidth=5)
ques.pack()
ansLabel = Label(QuestionSetup, text="Answer").pack()
ans = Entry(QuestionSetup, width=50,borderwidth=5)
ans.pack()

Button(QuestionSetup,text="Next",command= lambda: differenciateQuestion(clicked.get(),
                                                                    chosenModule.get(),
                                                                    ques.get(),
                                                                    ans.get())).pack()
Button(QuestionSetup,text="Back",command= lambda: swap(mainMenu)).pack()


exitButton.pack()

mainMenu.tkraise()
win.mainloop()
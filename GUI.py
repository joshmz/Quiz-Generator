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
multipleChoiceSetup = Frame(win)

def addToDatabase(*args):
    #   Do this for module Insert
    if (len(args) == 2):
        ms.create_module(*args)
    #   Do this for Question insert
    #   Multiple Choice
    elif (len(args) != 2) and clicked.get() == qs.questionTypes[0]:
        print(getValues[1,4])
        qs.multiple_choice((getValues[1]),getValues[2],getValues[3],getValues[4])
    #   True False
    elif (len(args) != 2) and clicked.get() == qs.questionTypes[1]:
        pass
    #   Best Match
    else:
        pass

def differenciateQuestion(type,ans):
    if type == qs.questionTypes[0]:


        def addAnswer():
            if len(answerList) < 5:
                answerList.append(falseAnswer.get())
                Label(possibleAns,text=falseAnswer.get()).pack()
            else:
                getValues.append(answerList)
                addToDatabase(getValues,answerList,None)

        answerList = [ans]
        falseAnswerCount = 1

        possibleAns = Tk()
        possibleAns.title("MULTIPLE CHOICE")

        Label(possibleAns,text=f"Enter A False Answer: ({falseAnswerCount})").pack()
        falseAnswer = Entry(possibleAns, width=50,borderwidth=5)
        falseAnswer.pack()

        nextButton = Button(possibleAns,text='Next',command= addAnswer).pack()

        
        Label(possibleAns,text=answerList[0]).pack()


        possibleAns.mainloop()

        swap(multipleChoiceSetup)

def swap(frame):
    frame.tkraise()

for frame in (mainMenu, takeQuiz, adminTools,moduleSetup,QuestionSetup,multipleChoiceSetup):
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
chosenModule.set(db.moduleNamesList[0])

qTypeLabel = Label(QuestionSetup,text="Choose Question Type").pack()
qTypeOptions = OptionMenu(QuestionSetup, clicked, *qs.questionTypes)
qTypeOptions.pack()

qModuleLabel = Label(QuestionSetup,text="What Module Is This Question For?").pack()
qModule = OptionMenu(QuestionSetup, chosenModule, *db.moduleNamesList)
qModule.pack()
quesLabel = Label(QuestionSetup,text="Enter Question").pack()
ques = Entry(QuestionSetup, width=50,borderwidth=5)
ques.pack()
ansLabel = Label(QuestionSetup, text="Answer").pack()
ans = Entry(QuestionSetup, width=50,borderwidth=5)
ans.pack()

getValues =[
    clicked.get(),
    chosenModule.get(),
    ques.get(),
    ans.get()
]

Button(QuestionSetup,text="Next",command= lambda: differenciateQuestion(clicked.get(),ans.get())).pack()
Button(QuestionSetup,text="Back",command= lambda: swap(mainMenu)).pack()

#----------------------------------------------------
#   MCQ SETUP QAGE
multiChoiceLabel = Label(multipleChoiceSetup,text='MULTIPLE CHOICE').pack()




exitButton.pack()

mainMenu.tkraise()
win.mainloop()
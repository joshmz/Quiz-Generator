import ModuleSetup
import QuestionSetup
import Database as db


def admin_features():
    i = True
    while i:
        choice = int(input("1. Create Module \n"
                           "2. Create Question\n"
                           "Choose an option: "))
        if choice == 1:
            ModuleSetup.create_module()
            i = False
        elif choice == 2:
            if len(db.moduleList) != 0:
                QuestionSetup.choose_question_type()
            else:
                print("No modules found")
                admin_features()
        else:
            print("Invalid choice")
    exit()


admin_features()

#  ADD CHOICE TO PICK MODULE FOR QUESTIONS

#  MAKE BEST MATCH

#  MAKE GUI
import Database as db

# Array of all types of questions
questionTypes = ["Multiple Choice", "True/False", "Best Match"]


# Main parent class
class MakeQuestion:
    def __init__(self, module, type, question, answer, options, feedback, wrong_count):
        self.module = module
        self.type = type
        self.question = question
        self.answer = answer
        self.options = options
        self.feedback = feedback
        self.wrong_count = 0

    # Inserting data into database
    def insert_data(self,qType):
        question = [
            self.module,
            qType,
            self.question,
            self.answer,
            self.options,
            self.feedback
        ]
        db.cursor.execute('INSERT INTO questions (module, qType, question, answer, options, feedback) VALUES (?,?,?,?,?,?)', question)
        db.conn.commit()


# Multiple Choice Question Subclass -> MakeQuestion
class MakeMCQ(MakeQuestion):
    def __init__(self, module, type, question, answer, options, maxAnswers, feedback, wrong_count):
        #  inherit parent attributes
        super(MakeMCQ, self).__init__(module, type, question, answer, options, feedback, wrong_count)
        self.maxAnswers = maxAnswers

    # # Allow user to input fake answers FUNCTION OVERWRITTEN IN GUI
    # def make_dummy_answer(self):
    #     self.maxAnswers = int(input("How many answers would you like the MCQ to have? "))
    #     for i in range(self.maxAnswers - 1):
    #         dummy_answer = input("Enter dummy answer: ")
    #         self.options.append(dummy_answer)


# True False question subclass
class MakeTF(MakeQuestion):
    def __init__(self, module, type, question, answer, options, feedback, wrong_count):
        super(MakeTF, self).__init__(module, type, question, answer, options, feedback, wrong_count)

# Best Match question subclass
class MakeBM(MakeQuestion):
    def __init__(self, module, type, terms, definitions, feedback, wrong_count):
        super(MakeBM,self).__init__(module, None, None, None, None, feedback, wrong_count)
        self.type = type
        self.definitions = definitions
        self.terms = terms

    # def make_match(self):
    #     self.maxTerms = int(input("How many terms would you like to create? "))
    #     for i in range(self.maxTerms):
    #         term = input("Enter a term: ")
    #         definition = input("Enter its definition: ")
    #         self.terms.append(term)
    #         self.definitions.append(definition)
    #     self.matches = (list(zip(self.terms,self.definitions)))
    #     print (self.matches[0])
        
    def insert_data(self):
        question=[
            self.module,
            self.type,
            self.terms,
            self.definitions
        ]
        db.cursor.execute('INSERT INTO questions (module, qType, question, answer) VALUES (?,?,?,?)', question)
        db.conn.commit()


# Allow user to pick a question type OVERWRITTEN IN GUI
# def choose_question_type():
#     module_check = True
#     while module_check:
#         for i in db.moduleList:
#             print(*i)
#         module_input = int(input(f"Enter module number: [1-{len(db.moduleList)}]: "))
#         module_check = False
#     type_check2 = True
#     while type_check2:
#         type_input = int(input(f"Question Types: \n"
#                                f"1. {questionTypes[0]}\n"
#                                f"2. {questionTypes[1]}\n"
#                                f"3. {questionTypes[2]}\n"
#                                f"Please choose a question type [1-3]: "))
#         # Validation check
#         if (type_input > 3) or (type_input < 1):
#             print("Invalid selection")
#         else:
#             type_check2 = False
#     # Go to different functions based of question type
#     if type_input == 1:
#         question_input = input("Enter a question: ")
#         answer_input = input("Enter the correct answer: ")
#         multiple_choice(module_input, question_input, answer_input)
#     elif type_input == 2:
#         question_input = input("Enter a statement: ")
#         true_false(module_input, question_input)
#     elif type_input == 3:
#         best_match(module_input)


def multiple_choice(module, question, answer, options):
    module = module.strip("('),")
    question_instance = MakeMCQ(module, 1, question, answer, options, None, None, None)  # Instantiation
    question_instance.insert_data(1)

def true_false(module, question, answer, options):
    module = module.strip("('),")
    question_instance = MakeTF(module, 2, question, answer, options, None, None)  # Instantiation
    question_instance.insert_data(2)


def best_match(module,ques,ans):
    module = module.strip("('),")
    question_instance = MakeBM(module, 3, ques, ans, None, None)
    question_instance.insert_data()

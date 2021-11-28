import Database as db

# Array of all types of questions
questionTypes = ["Multiple Choice", "True/False", "Best Match"]


# Main parent class
class MakeQuestion:
    def __init__(self, module, type, question, answer, options):
        self.module = module
        self.type = type
        self.question = question
        self.answer = answer
        self.options = [answer]

    def insert_data(self):
        question = [
            str(db.moduleNamesList[self.module - 1]),
            self.question,
            self.answer
        ]
        db.cursor.execute('INSERT INTO questions (module, question, answer) VALUES (?,?,?)', question)
        db.conn.commit()


# Multiple Choice Question Subclass -> MakeQuestion
class MakeMCQ(MakeQuestion):
    def __init__(self, module, type, question, answer, options, maxAnswers):
        #  inherit parent attributes
        super(MakeMCQ, self).__init__(module, type, question, answer, options)
        self.maxAnswers = maxAnswers

    # Allow user to input fake answers
    def make_dummy_answer(self):
        self.maxAnswers = int(input("How many answers would you like the MCQ to have? "))
        for i in range(self.maxAnswers - 1):
            dummy_answer = input("Enter dummy answer: ")
            self.options.append(dummy_answer)


# True False question subclass
class MakeTF(MakeQuestion):
    def __init__(self, module, type, question, answer, options):
        super(MakeTF, self).__init__(module, type, question, answer, options)

    def true_or_false(self):
        self.answer = input("Is your statement True or False? ")
        # make GUI for choice
        if self.answer == "True":
            self.options.append("False")
        else:
            self.options.append("True")




class MakeBM:
    def __init__(self, type, terms, definitions, max_terms):
        self.type = type
        self.terms = []
        self.definitions = []
        self.maxTerms = max_terms

    def make_match(self):
        self.maxTerms = int(input("How many terms would you like to create? "))
        for i in range(self.maxTerms):
            term = input("Enter a term: ")
            definition = input("Enter its definition: ")
            self.terms.append(term)
            self.definitions.append(definition)


# Allow user to pick a question type
def choose_question_type():
    module_check = True
    while module_check:
        for i in db.moduleList:
            print(i)
        module_input = int(input(f"Enter module number: [1-{len(db.moduleList)}]: "))
        module_check = False
    type_check2 = True
    while type_check2:
        type_input = int(input(f"Question Types: \n"
                               f"1. {questionTypes[0]}\n"
                               f"2. {questionTypes[1]}\n"
                               f"3. {questionTypes[2]}\n"
                               f"Please choose a question type [1-3]: "))
        # Validation check
        if (type_input > 3) or (type_input < 1):
            print("Invalid selection")
        else:
            type_check2 = False
    # Go to different functions based of question type
    if type_input == 1:
        question_input = input("Enter a question: ")
        answer_input = input("Enter the correct answer: ")
        multiple_choice(module_input, question_input, answer_input)
    elif type_input == 2:
        question_input = input("Enter a statement: ")
        true_false(module_input, question_input)
    elif type_input == 3:
        best_match()


def multiple_choice(module, question, answer):
    question_instance = MakeMCQ(module, 1, question, answer, None, None)  # Instantiation
    question_instance.make_dummy_answer()
    print(f'this question is for {db.moduleNamesList[question_instance.module - 1]}')
    question_instance.insert_data()

def true_false(module, question):
    question_instance = MakeTF(module, 2, question, None, None)  # Instantiation
    question_instance.true_or_false()
    print(f'this question is for {db.moduleNamesList[question_instance.module - 1]}')
    question_instance.insert_data()


def best_match():
    question_instance = MakeBM(3, None, None, None)
    question_instance.make_match()

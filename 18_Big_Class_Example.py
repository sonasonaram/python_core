# School Management System Software
#
# Login for Teacher, Student
# Teacher can upload exam questions
# student will take the exam
# Teacher will check the answers, and put marks
# student can check how much mark he has got


class subject:
    def __init__(self, name):
        self.name = name
        self.full_marks = -1
        self.obtained_marks = -1
        self.no_of_questions = -1
        self.no_of_questions_answered = -1



class teacher:
    def __init__(self, name, email, password, subjects):
        self.name = name
        self.email = email
        self.password = password
        self.subjects = subjects
        self.logged_in = False

    def login(self, email, password):
        if email == self.email and password == self.password:
            self.logged_in = True
            print("login successful")
        else:
            self.logged_in = False
            print("login failure")

    def logout(self):
        self.logged_in = False

    def make_questions(self, sub):
        if (list)(self.subjects).count((sub)) != 0:
            sub.full_marks = 100
            sub.no_of_questions = 20
            print("Successfully set questions")
        else:
            print(sub.name, "is not assigned to", self.name)


    def check_answers(self, sub):
        answered_questions = sub.no_of_questions_answered
        if answered_questions != -1:
            marks = input("How much marks to give: ")
            sub.obtained_marks = marks
        else:
            print("Student has not yet answered the test")


class student:
    def __init__(self, name, email, password, subjects, roll, std):
        self.name = name
        self.email = email
        self.password = password
        self.subjects = subjects
        self.roll = roll
        self.std = std

    def login(self, email, password):
        if email == self.email and password == self.password:
            self.logged_in = True
            print("login successful")
        else:
            self.logged_in = False
            print("login failure")

    def logout(self):
        self.logged_in = False

    def answer_test(self, sub):
        if (list)(self.subjects).count(sub) != 0:
            q = sub.no_of_questions
            if q != -1:
                sub.no_of_questions_answered = input("Hi " + self.name + ", How many questions can you answer? ")
            else:
                print("The questions have not been set for", sub.name)
        else:
            print("You do not have access to", sub.name)

    def see_marks(self, sub):
        if (list)(self.subjects).count(sub) != 0:
            m = sub.obtained_marks
            if m == -1:
                print("Subject is not yet checked")
            else:
                print("You have got", m, "marks in", sub.name)



maths = subject("Mathematics")
science = subject("Science")

t = teacher("Ram", "ram@gmail.com", "12345", [maths, science])
s = student("hemanth", "hem@gmail.com", "6789", [maths], 1, 10)


# t.make_questions(maths)
#
# s.answer_test(maths)
#
# t.check_answers(maths)
#
# s.see_marks(maths)

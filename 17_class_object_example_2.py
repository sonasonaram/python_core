class Student:

    def __init__(self, Name, Place, Subject):
        self.Name = Name
        self.place = Place
        self.subject = Subject

    def Study(self):
        print(self.Name, "is Studying" )

    def AttendSession(self, meetingID):
        print(self.Name,"is attending meeting at" , meetingID)

    def Practice(self):
        print(self.Name ,"is practising",self.subject)

    def DoAssignment(self):
        pass

s1 = Student("Hemanth","Andhra", "maths")


s1.Study()
s1.AttendSession("123-456-789")
s1.Practice()
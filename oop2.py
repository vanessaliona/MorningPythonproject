class student:
    def __init__(self,firstname,course,language):
        self.firstname=firstname
        self.course=course
        self.language=language
        
        def sleep(self):
            print(self.firstname,"is sleeping")



student1=student(firstname:"Caleb",course:"MIT",language:"C++")
print(student1.firstname)
student1.sleep


student2=student(firstname:"Clarence")
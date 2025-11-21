class Student:
    def student_info(self,student_name,s_id,div,marks):
        setattr(self,"Student_name",student_name)
        setattr(self,"Student_ID",s_id)
        setattr(self,"Division",div)
        setattr(self,"Marks",marks)

    def class_m(self):
        print("Student_name",{getattr(self,"Student_name")})
        print("Student_ID",{getattr(self,"Student_ID")})
        print("Division",{getattr(self,"Division")})
        print("Marks",{getattr(self,"Marks")})
        print('-'*30)

student1=Student()
student2=Student()

student1.student_info("Aryan",1,'A',98)
student2.student_info('Amar',2,'A',96)

student1.class_m()
student2.class_m()        



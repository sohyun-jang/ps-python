class Student:
    def __init__(self, name, korean, math, english):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        
    def get_sum(self):
        return self.korean + self.math + self.english
    
    def get_average(self):
        return self.get_sum() / 3
    
    def __str__(self):
        return ("이름: {}, 총점: {}, 평균: {:.2f}".format(self.name, self.get_sum(), self.get_average()))
    
class GraduateStudent(Student):
    def __init__(self, name, korean, math, english, research_topic):
        super().__init__(name, korean, math, english)
        self.research_topic = research_topic
        
    def __str__(self):
        base = super().__str__()
        return (base + ", 연구 주제: {}".format(self.research_topic))
    

student1 = Student("홍길동", 88, 92, 85)
print(student1)

grad_student1 = GraduateStudent("김철수", 95, 90, 93, "인공지능")
print(grad_student1)
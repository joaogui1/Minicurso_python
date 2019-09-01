'''Class creation and Instanciation '''

class Student:

    def __init__(self, nome, sobrenome, Nusp):
        self.nome = nome
        self.sobrenome = sobrenome
        self.Nusp = Nusp
        self.email = f'{nome}.{sobrenome}@usp.br'

    def full_name(self):
        return f'{self.nome} {self.sobrenome}'


stu_1 = Student("Joao", "Araujo", "00000")
print(stu_1.email)
print(stu_1.full_name())
print(Student.full_name(stu_1))

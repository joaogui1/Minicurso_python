'''Class creation and Instanciation '''

class Student:

    valor_bolsa = 400
    def __init__(self, nome, sobrenome, Nusp):
        self.nome = nome
        self.sobrenome = sobrenome
        self.Nusp = Nusp
        self.email = f'{nome}.{sobrenome}@usp.br'
        self.contaBB = 0

    def full_name(self):
        return f'{self.nome} {self.sobrenome}'

    def recebe_bolsa(self):
        self.contaBB += self.valor_bolsa



stu_1 = Student("Joao", "Araujo", "00000")
print(stu_1.email)
print(stu_1.full_name())
print(Student.full_name(stu_1))

print(stu_1.contaBB)
stu_1.recebe_bolsa()
print(stu_1.contaBB)
print(stu_1.valor_bolsa)

stu_1.valor_bolsa = 300
print(stu_1.valor_bolsa)
print(Student.valor_bolsa)

'''Dunder Methods'''

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

    def set_bolsa(self, valor):
        self.valor_bolsa = valor

    def __repr__(self):
        return f"Student('{self.nome}', '{self.sobrenome}', {self.Nusp})"

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"

    #__add__, __len__, __mul__, __sub__, __call__

class Pos(Student):
    def __init__(self, nome, sobrenome, Nusp, orientador):
        super().__init__(nome, sobrenome, Nusp)
        self.orientador = orientador



stu_1 = Student("Joao", "Araujo", "00000")
print(stu_1.email)
print(stu_1.full_name())
print(Student.full_name(stu_1))
print(stu_1)

pos_1 = Pos("Leonardo", "Sampaio", "00001", "Moacir")

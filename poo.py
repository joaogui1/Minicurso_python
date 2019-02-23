import time
class AssocUSP():
    auxilio = 300
    def __init__(self, name, lastname, nusp):
        self.name = name
        self.lastname = lastname
        self.nusp = nusp
        self.banco = 0
    def receber(self):
        self.banco += self.auxilio
    def aumento(self):
        self.auxilio += 100
    def __repr__(self):
        return f'AlunoUSP("{self.name}", "{self.lastname}", {self.nusp})'
    def __str__(self):
        return f'{self.name} {self.lastname}'
    def __len__(self):
        return 1

class AlunoUSP(AssocUSP):
    auxilio = 400
    def __init__(self, name, lastname, nusp):
        AssocUSP.__init__(self, name, lastname, nusp)
        self.email = f'{name}.{lastname}@.usp.br'
        self.ponderada = None

class AlunoPOS(AlunoUSP):
    def __init__(self, name, lastname, nusp, professor, bolsa = None):
        AlunoUSP.__init__(self, name, lastname, nusp)
        self.professor = professor
        self.bolsa = bolsa

class Professor(AssocUSP):
    def __init__(self, name, lastname, nusp, orientandos = None):
        AssocUSP.__init__(self, name, lastname, nusp)
        self.email = f'{name}.{lastname}@.usp.br'
        if orientandos == None:
            orientandos = list()
        self.orientandos = orientandos
    def __len__(self):
        return len(self.orientandos)

def decide_bolsa(professor, bolsa, aluno):
    if((len(professor) < 30 and len(bolsa[0]) > 8000 and aluno.bolsa == None)):
        time.sleep(1000000000000000000000000000000)
        return True
    return False







joao = AlunoUSP("Joao", "Araujo", 9725165)
alex = AlunoUSP("Alex", "Andre", 10734706)
alex.receber()
print(joao.__dict__)
# print(joao.email)

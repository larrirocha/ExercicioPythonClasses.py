'''Utilizando o Python crie uma classe que recebe duas notas (Unidade I e 
Unidade II) e calcula a nota final do aluno, lembrando que a nota final é a soma das
notas da Unidade I e Unidade II'''


class aluno:
    def __init__(self, unidadeI, unidadeII):
        self.unidadeI = unidadeI
        self.unidadeII = unidadeII
        self.mediaAluno = (unidadeI + unidadeII)

    def calculoMedia(self, mediaAluno):
        self.mediaAluno = (self.unidadeI + self.unidadeII)
        if mediaAluno > 6:
            return 'Média %s (Aluno APROVADO!)' % mediaAluno
        else:
            return 'Média %s (Aluno REPROVADO!)' % mediaAluno


resultado = aluno("7", "8")
print(resultado.mediaAluno)




import os
from time import sleep
from prettytable import PrettyTable


class Alunos:

    Todos_os_alunos = []

    def Validar_notas(self, nota):
        if nota >= 0 and nota <= 10:
            return True

        else:
            return False

    def Inserir_aluno(self):
        nome = input("Digite o nome do aluno:")

        while True:
            inserir_outros_dados = input('Quer inserir as provas e trabalhos: [s/n]')

            if inserir_outros_dados.lower() == 's':
                self.Adicionar_as_notas_e_criar_aluno(True, nome)
                break

            elif inserir_outros_dados.lower() == 'n':
                self.Adicionar_as_notas_e_criar_aluno(False, nome)
                break

            else:
                print('Opção não existente, digite apenas "s" ou "n"')

    def Adicionar_as_notas_e_criar_aluno(self, adicionar_tudo, nome):
        def Adicionando_as_notas(qual_nota):
            while True:
                try:
                    nota = input(f'Digite a nota da {qual_nota} do aluno: [P- Pular]')

                    if nota.lower() == 'p':
                        nota = '-'
                        break

                    elif self.Validar_notas(float(nota)):
                        nota = float(nota)
                        # Se for valido então vamos retornar parar o loop e a nota sera a que ele digitou
                        break

                    else:
                        print('Nota invalida')

                except:
                    print('Nota invalida')

            return nota


        # nome, nota1, nota2, trabalho1, trabalho2, rec, media, status
        novo_aluno = []
        novo_aluno.append(nome)

        todas_opcoes = ['nota 1', 'nota 2', 'trabalho 1', 'trabalho 2']
        if adicionar_tudo:
            for item in todas_opcoes:
                novo_aluno.append(Adicionando_as_notas(item))

            # Esa sera a nota da recuperação
            novo_aluno.append('-')

            # Obs: a media e o status são adicionados quando for listar todos os alunos no metodo Listar_todos_os_alunos

        else:
            # Se o usuario nã quiser adicionar nenhuma nota
            novo_aluno += ['-', '-', '-', '-', '-', '-', '-']

        # Vamos adicionar na lista dos alunos
        self.Todos_os_alunos.append(novo_aluno)

    def Excluir_aluno(self, excluir_aluno):
        self.Listar_todos_os_alunos()
        while True:
            try:
                codigo = int(input('Digite o codigo do aluno: [0-sair]'))

                if codigo == 0:
                    break

                else:
                    aluno = self.Todos_os_alunos[codigo - 1]

                    # PAra saber se é para excluir o aluno
                    if excluir_aluno:
                        quer_excluir = input('Você quer mesmo excluir esse aluno? [s-sim]')

                        if quer_excluir.lower() == 's':
                            self.Todos_os_alunos.pop(codigo-1)
                            print('Excluindo aluno... Aguarde alguns segundos por favor!')
                            sleep(5)
                            print('\nAluno excuido com sucesso!')

                            input('Precione qualquer tecla para continuar')


                        else:
                            print('Cancelando...')
                            sleep(2)

                    else:
                        self.Mostrar_um_aluno(aluno, codigo)

                    # Como entrou nesse else então esta valido e vamos parar o loop
                    break

            except:
                print('Codigo não encontrado, digite um valido')

    def Listar_todos_os_alunos(self):

        os.system('cls')

        tabela = PrettyTable(['Id', 'Nome', 'Prova 1', 'Prova 2', 'trabalho 1', 'Trabalho 2', 'Recuperação',
                              'Nota final', 'Status'])
        cont = 1
        for aluno in self.Todos_os_alunos:
            media, status = self.Media(aluno)

            tabela.add_row([cont, aluno[0], aluno[1], aluno[2], aluno[3], aluno[4], aluno[5], media, status])

            cont += 1

        print(tabela)
        input('\nPara continuar, aperte qualquer tecla')

    def Media(self, aluno):
        def Avaliando_a_media_com_a_recuperacao(media):
            # Se ja fez a recuperação e se for maior que a media, então ele passou, se não ele não passou
            if aluno[5] > media:
                # Aqui vamos mudar tambem a media, isso porque se a nota de recuperação for maior que a media
                # então vamos mostrar ela
                media = aluno[5]

                if aluno[5] >= 6:
                    status = 'Aprovado'

                else:
                    status = 'Reprovado'

            else:
                if media >= 6:
                    status = 'Aprovado'

                else:
                    status = 'Reprovado'

            return media, status



        def Obtento_status(media):
            # Descobrindo se a nota é um numero
            if type(media) != str:
                status = 'Recuperação'
                if media >= 6:
                    status = 'Aprovado'

                elif media < 5:
                    status = 'Reprovado'

                # Vamos verificar se ele ja fez a prova de recuperação
                if type(aluno[5]) != str:
                   media, status = Avaliando_a_media_com_a_recuperacao(media)

            # Se a media nao for numero, então não tem nenhuma nota cadastrada ainda, ou seja, o status vai ser '-'
            else:
                status = '-'

            return media, status


        media_provas = 0
        media_trabalhos = 0
        cont = 0
        for item in aluno:
            try:
                nota = float(item)

                '''
                As posições estao assim...
                posições...      0       1        2         3           4            5
                Todos_alunos = [nome, prova 1, prova 2, trabalho 1, trabalho 2, recuperacao]
                '''
                if cont == 1 or cont == 2:
                    media_provas += nota / 2

                elif cont == 3 or cont == 4:
                    media_trabalhos += nota / 2

            except:
                pass

            cont += 1

        media = round(media_provas * 0.7 + media_trabalhos * 0.3, 2)

        # Esse if/else é para saber se tem uma media, se não tem então vamos retornar apenas um '-'
        if media == 0:
            media = '-'

        # Para saber se é numero ou teto para nao dar erro depois
        # if type(media) == int or type(media) == float:
        #     status = 'Recuperação'
        #     if media >= 6:
        #         status = 'Aprovado'
        #
        #     elif media < 5:
        #         status = 'Reprovado'
        #
        # else:
        #     status = '-'

        media, status = Obtento_status(media)

        return media, status

    def Lancar_nota(self, qual_nota):
        def Trocar_nota(nota_original, nova_nota):
            if nota_original == '-':
                return True

            else:
                if nota_original >= 5 and nota_original < 6:
                    print('O aluno não está em recuperação, então não pode ser adicionada uma nota de recuperação')
                    return False

                else:
                    sim_nao = input(f'Quer mesmo trocar a nota {nota_original} pela nota {nova_nota} [s-sim]:')
                    if sim_nao.lower() == 's':
                        return True

                    else:
                        print('\nA troca da nota está sendo cancelada...')
                        sleep(4)
                        return False

        def Adicionar_nota(aluno):
            while True:
                try:
                    nota = float(input(f'Digite uma nota para {qual_nota}:'))

                    if self.Validar_notas(nota):
                        break
                except:
                    print('Nota invalida')

            if qual_nota == 'Prova 1':
                if Trocar_nota(aluno[1], nota):
                    aluno[1] = nota

            elif qual_nota == 'Prova 2':
                if Trocar_nota(aluno[2], nota):
                    aluno[2] = nota

            elif qual_nota == 'Trabalho 1':
                if Trocar_nota(aluno[3], nota):
                    aluno[3] = nota

            elif qual_nota == 'Trabalho 2':
                if Trocar_nota(aluno[4], nota):
                    aluno[4] = nota

            elif qual_nota == 'Recuperação':
                if Trocar_nota(aluno[5], nota):
                    aluno[5] = nota


        self.Listar_todos_os_alunos()
        while True:
            try:
                codigo = int(input('Digite o codigo do aluno: [0-sair]'))
                aluno = self.Todos_os_alunos[codigo-1]

                if codigo == 0:
                    break

                else:
                    Adicionar_nota(aluno)
                    break

            except:
                print('Codigo invalido')

    def Mostrar_um_aluno(self, aluno, id):

        tabela = PrettyTable(['Id', 'Nome', 'Prova 1', 'Prova 2', 'trabalho 1', 'Trabalho 2', 'Recuperação',
                              'Nota final', 'Status'])

        media, status = self.Media(aluno)

        tabela.add_row([id, aluno[0], aluno[1], aluno[2], aluno[3], aluno[4], aluno[5], media, status])

        input('\nAperte qualquer tecla para continuar')

class Menu(Alunos):

    def __init__(self):
        self.Todos_os_alunos = []
        while True:
            print(f'{"=" * 30} MENU {"=" * 30}')
            print('1 - Inserir aluno \n2 - Excluir aluno por código \n3 - Exibir dados do aluno por código '
                  '\n4 - Listar todos os alunos \n5 - Lançar nota Prova 1 \n6 - Lançar nota Prova 2 \n7 - Lançar nota Trabalho 1'
                  ' \n8 - Lançar nota Trabalho 2 \n9 - Lançar nota Recuperação \n10 - Sair')
            try:
                escolha = int(input('\nDigite a opção desejada:'))

                if escolha == 10:
                    break

                elif escolha >= 1 and escolha <= 9:
                    self.Direcionando_opcao_escolhida(escolha)

                else:
                    print('Por favor, digite uma opção existente!')

            except:
                print('Por favor, digite uma opção existente!')

            os.system('cls')

    def Direcionando_opcao_escolhida(self, opcao):
        if opcao == 1:
            self.Inserir_aluno()

        elif opcao == 2:
            self.Excluir_aluno(True)

        elif opcao == 3:
            self.Excluir_aluno(False)

        elif opcao == 4:
            self.Listar_todos_os_alunos()

        elif opcao == 5:
            self.Lancar_nota('Prova 1')

        elif opcao == 6:
            self.Lancar_nota('Prova 2')

        elif opcao == 7:
            self.Lancar_nota('Trabalho 1')

        elif opcao == 8:
            self.Lancar_nota('Trabalho 2')

        elif opcao == 9:
            self.Lancar_nota('Recuperação')


Menu()

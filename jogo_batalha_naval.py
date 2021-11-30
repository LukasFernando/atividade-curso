
import os
import random


class Criando_algumas_variaveis:
    def __init__(self, tamanho):
        '''
        Nesse metodo vamos criar algumas variaveis para usar nessa clase e vamos criar as posições das colunas
        '''

        # O tamanho da tabela, para usar em outros metodos
        self.Tamanho_do_tabuleiro = tamanho

        # Essa variavel vai salvar as posiçoes da linha (linha 1, linha 2,...)
        self.contagem_das_linhas = '     '

        # Nesse for vamos salvar as linhas, do tamanho que foi recebido
        for posicao in range(self.Tamanho_do_tabuleiro):
            self.contagem_das_linhas += str(posicao) + '  '

        # essa variavel e´para formar um quadro em volta do Tabuleiro. Ex: +--------+
        self.Tracos_para_separar_a_posicao_do_tabuleiro = ('+' + ('-' * self.Tamanho_do_tabuleiro * 3 + '--') + '+')

        # Para saber se é o usuario quem esta jogando ou a maquina
        self.Achou_uma_jogada = False

        # Vamos escolher a posição dos navios da maquina
        self.Escolhendo_o_navio_da_maquina()

        # Vamos criar algumas listas para usar na classe Batalha_naval
        self.Listas()

    def Escolhendo_o_navio_da_maquina(self):
        # Essas duas variaveis são para saber quantos navios foram acertados, para saber se o jogo acabou ou não
        self.Contagem_de_acertos_no_navio_do_usuario = 0
        self.Contagem_de_acertos_no_navio_da_maquina = 0

        # Vamos escolher o´prmeiro navio da maquina
        self.Navio_linha_maquina = random.randrange(0, self.Tamanho_do_tabuleiro)
        self.Navio_coluna_maquina = random.randrange(0, self.Tamanho_do_tabuleiro)

        # Agora vamos escolher o segundo navio da maquina, porem não pode ser o mesmo que o primeiro
        while True:
            # Vamos gerar um numero aleatorio e conferir para saber se é igual o primerio, se for então escolhe outtro
            n1 = random.randrange(0, self.Tamanho_do_tabuleiro)
            n2 = random.randrange(0, self.Tamanho_do_tabuleiro)

            if n1 != self.Navio_linha_maquina or n2 != self.Navio_coluna_maquina:
                self.Navio_linha_maquina_2 = n1
                self.Navio_coluna_maquina_2 = n2
                break

    def Listas(self):
        # Essa variavel sera a matriz do jogo
        self.Tabuleiro_do_usuario = []
        self.Tabuleiro_da_maquina = []

        # Criando as duas tabelas
        for linha in range(self.Tamanho_do_tabuleiro):

            matriz_usuario = []
            matriz_maquina = []

            for coluna in range(self.Tamanho_do_tabuleiro):
                # Essa variavel é para adicionar um espaço em cada espaço da matriz
                adicionar = '-'
                matriz_usuario.append(adicionar)

            for coluna_maquina in range(self.Tamanho_do_tabuleiro):
                # Essa variavel é para adicionar um espaço em cada espaço da matriz
                adicionar_maquina = '-'
                matriz_maquina.append(adicionar_maquina)


            self.Tabuleiro_do_usuario.append(matriz_usuario)
            self.Tabuleiro_da_maquina.append(matriz_maquina)


        # Nesse "for" vamos fazer uma lista de todas as posições disponiveis para a maquina jogar
        self.Todas_posicoes_disponiveis = []
        for linha in range(self.Tamanho_do_tabuleiro):
            for coluna in range(self.Tamanho_do_tabuleiro):
                add = str(linha) + ' ' + str(coluna)
                self.Todas_posicoes_disponiveis.append(add)

        # Para salvar todas as jogadas
        self.Jogadas_feitas_do_usuario = []
        self.Jogadas_feitas_da_maquina = []

        # Essa lista é para salvar a mensagem de quem venceu
        self.msg_de_quem_venceu = []


class Batalha_Naval(Criando_algumas_variaveis):

    def __init__(self, tamanho_do_tabuleiro):
        # Vamos chamar a classe Criando_algumas_variaveis para criar as variaveis que vão contruir o jogo
        super(Batalha_Naval, self).__init__(tamanho_do_tabuleiro)

        # ja criamos o tabuleiro, agora vamos deixa o usuario jogar
        self.Usuario_jogando()

    def Salvar_jogada(self):
        '''
        Esse metodo salva a jogada do usuario ou da maquina na posição escolhida.
        OBS: Não recebe nenhum paramentro porque o metodo usa a variavel self.Linha e Self.Coluna para salvar a jogada,
        essas duas variaveis são criadas no metodo Validar_jogada
        '''

        for linha in range(self.Tamanho_do_tabuleiro):
            for coluna in range(self.Tamanho_do_tabuleiro):

                self.Adicionar_jogada(linha, coluna)

                # Se a jogada ja foi achada, então vamos parar o primeiro loop
                if self.Achou_uma_jogada:
                    break

            # Se a jogada ja foi achada, então vamos parar o segundo loop
            if self.Achou_uma_jogada:
                self.Achou_uma_jogada = False
                break

    def Adicionar_jogada(self, linha, coluna):

        # Para saber se ja chegou na posição escolhida, se sim então entra no if
        if linha == int(self.Linha) and coluna == int(self.Coluna):
            adicionar = ' '

            # Se entrou no if então ja achou a jogada
            self.Achou_uma_jogada = True

            # Para saber se acertou o navio da maquina
            if self.A_vez_do_usuario and (linha == self.Navio_linha_maquina and coluna == self.Navio_coluna_maquina or
                                          linha == self.Navio_linha_maquina_2 and coluna == self.Navio_coluna_maquina_2):

                adicionar = 'X'
                self.Contagem_de_acertos_no_navio_da_maquina += 1

                if self.Contagem_de_acertos_no_navio_da_maquina == 2:
                    self.msg_de_quem_venceu.append('\nVocê ganhou!')

                    # Se o usuario acertou o navio, então vamos parar o loop no metodo Usuario_jogando
                    self.flag = False

            # Para saber se acertou o navio do usuario
            elif not self.A_vez_do_usuario and (linha == self.Navio_linha_usuario and coluna == self.Navio_coluna_usuario
                                                or linha == self.Navio_linha_usuario_2 and coluna == self.Navio_coluna_usuario_2):

                adicionar = 'X'
                self.Contagem_de_acertos_no_navio_do_usuario += 1

                # Como são dois navios, então se a varivel for 2 o jogo acabou
                if self.Contagem_de_acertos_no_navio_do_usuario == 2:
                    self.msg_de_quem_venceu.append(f'\nVocê perdeu!\n\nO navio 1 da maquina estava em: '
                                                   f'Linha {self.Navio_linha_maquina}, Coluna {self.Navio_coluna_maquina}.'
                                                   f'\nO Navio 2 da maquina estava em: '
                                                   f'Linha {self.Navio_linha_maquina_2}, Coluna {self.Navio_coluna_maquina_2}')

                    # Se o usuario acertou o navio, então vamos parar o loop no metodo Usuario_jogando
                    self.flag = False

            # Nesse "if/else" vamos saber de quem é a jogada para adicionar a jogada no Tabuleiro
            if self.A_vez_do_usuario:
                # Vamos salvar a jogada do usuario no Tabuleiro da mauquina
                tab = self.Tabuleiro_da_maquina[linha]
                tab[coluna] = adicionar

            else:
                # Vamos salvar a jogada da maquina no Tabuleiro do usuario
                tab2 = self.Tabuleiro_do_usuario[linha]
                tab2[coluna] = adicionar

    def Validar_jogada(self, jogada, de_quem_eh_a_jogada):
        jogada_aceita = False
        try:
            # Vamos separar a linha e a coluna para tirar todos os espaços e obter apenas as duas posições
            self.Linha, self.Coluna = jogada.split()

            # As duas variaveis estão em str
            jogada = self.Linha + self.Coluna

            # Apos tirar os espaços vamos verificar se é um numero ou uma letra
            int(jogada)

            if jogada in de_quem_eh_a_jogada:
                print('Jogada ja feita! escolha outra!')

            # Para saber se o numero é maior que o Tabuleiro
            elif int(self.Linha) >= self.Tamanho_do_tabuleiro or int(self.Coluna) >= self.Tamanho_do_tabuleiro or int(self.Linha) < 0 or int(self.Coluna) < 0:
                print (f'Numero fora do intervalo de 0 a {self.Tamanho_do_tabuleiro - 1}')

            else:
                # Aqui vamos descobrir de quem é a lista que recebemos, do usuario ou da maquina, e depois adicionamos
                # a jogada que recebemos na lista de quem estiver jogando
                if de_quem_eh_a_jogada == self.Jogadas_feitas_do_usuario:
                    self.Jogadas_feitas_do_usuario.append(jogada)

                else:
                    self.Jogadas_feitas_da_maquina.append(jogada)

                # Se entrou no else, então a jogada foi valida
                jogada_aceita = True


        except:
            print('Numero invalido, escolha dois numeros separados por espaço')


        return jogada_aceita

    def Imprimir_Tabuleiro(self):
        def Imprimir_algumas_informacoes(Imprimir_tudo):
            # Se for para imprimir...
            if Imprimir_tudo:
                # Paara imprimir de quem é a tabela
                print('       Sua Tabela               Tabela da Maquina')

                # Essa variavel foi criada noa clase Criando_algumas_variaveis, ela tem a contagem de colunas
                # (ex: coluna 1, coluna 2,...)
                print(self.contagem_das_linhas, '       ', self.contagem_das_linhas)

            # Nesse print vamos inciar o 'quadro' com '+--------+'.
            # Esse print esta fora do if porque esse print vai no começo e no fim da tabela, então se for no começo vai
            # entrar no "if" primeiro e depois chegar nesse print, agora se for no fim então vai vim apenas nesse print
            print(f'  {self.Tracos_para_separar_a_posicao_do_tabuleiro}          '
                  f'{self.Tracos_para_separar_a_posicao_do_tabuleiro}')


        Imprimir_algumas_informacoes(True)


        # Esse cont sera a contagem das linhas para mostrar antes da linha da matriz (Tabela)
        cont = 0
        for linha_usuario in self.Tabuleiro_do_usuario:
            linha_maquina = self.Tabuleiro_da_maquina[cont]

            # Esse print é para colocar valores na linha (linha 1, linha 2,...)
            print(cont, '|',  ' ', end='')

            for coluna in linha_usuario:
                # Esse print vai salvar nele as colunas de uma linha, para no final do primeiro "for" imprimir tudo
                print(coluna, end='  ')

            # Se ja saiu do do for então vamos adicionar alguns espaços para adicionar outros numeros no outro for
            print('|       ',cont, '|  ', end='')

            for coluna in linha_maquina:
                # Esse print vai salvar nele as colunas de uma linha, para no final do primeiro "for" imprimir tudo
                print(coluna, end='  ')

            # Para começar a salvar no print as posições em outra linha
            print('| \n', end='')

            # Para atualizar o valor das linhas
            cont += 1

        Imprimir_algumas_informacoes(False)

    def Fazer_a_jogada_da_maquna(self):
        '''
        OBS: Nesse metodo não tem "while True" nem verificação se retornou True ou False para a jogada, poque a jogada
        da maquina, porque estaremos pegando uma jogada da lista de jogadas disponiveis, ou seja, será uma jogada valida
        '''

        jogada = random.choice(self.Todas_posicoes_disponiveis)

        # jogada_valida = self.Validar_jogada(jogada, self.Jogadas_feitas_da_maquina)

        self.Linha, self.Coluna = jogada.split()

        # Vamos tirar a posição escolhida aleatoriamente da lista de jogadas disponiveis
        self.Todas_posicoes_disponiveis.pop(self.Todas_posicoes_disponiveis.index(jogada))

        # No metodo Criar_tabuleiro_e_ou_salvar_jogada tem uma explicação de porque não tem argumento
        self.Salvar_jogada()

    def Escolha_do_navio_do_usuario(self):
        # O cont é para saber qual navio esta sendo salvo, se é o navio 1 ou o navio 2
        cont = 0
        while cont < 2:
            try:
                navio_l, navio_c = map(int, input(f'Escolha a posição que o seu navio estará no Tabuleiro (linhas coluna):').split())

                # Vamos validar a escolha da posição do navio
                if navio_l >= 0 and navio_c >= 0 and navio_l < self.Tamanho_do_tabuleiro and \
                        navio_c < self.Tamanho_do_tabuleiro and cont == 0:

                    self.Navio_linha_usuario = navio_l
                    self.Navio_coluna_usuario = navio_c
                    print('Navio 1 salvo!')
                    cont += 1

                # VAmos verificar se esta tudo certo com o navio 2, e não pode ser repetido
                elif navio_l >= 0 and navio_c >= 0 and navio_l < self.Tamanho_do_tabuleiro and \
                        navio_c < self.Tamanho_do_tabuleiro and cont == 1 and \
                        (navio_l != self.Navio_linha_usuario or navio_c != self.Navio_coluna_usuario):

                    self.Navio_linha_usuario_2 = navio_l
                    self.Navio_coluna_usuario_2 = navio_c
                    print('Navio 2 salvo!')
                    cont += 1

                else:
                    print('Numero invalido!')

            except:
                print('Posição invalida! Separe os numeros por espaços (Linha Coluna)')

        # Qaundo sair do while vamos mostrar as escolhas do usuario
        print(f'Navio 1 está em: Linha {self.Navio_linha_usuario}, Coluna {self.Navio_coluna_usuario}')
        print(f'Navio 2 está em: Linha {self.Navio_linha_usuario_2}, Coluna {self.Navio_coluna_usuario_2}\n')

    def Jogar_de_novo(self):
        jogar_dnv = input('\nVocê quer jogar de novo? [s]')

        if jogar_dnv.lower() == 's':
            self.__init__(5)

    def Usuario_jogando(self):
        # Antes de comçar vamos imprimir o Tabuleiro
        self.Imprimir_Tabuleiro()

        # Para o usuario escolher a posição do navio
        self.Escolha_do_navio_do_usuario()

        self.flag = True
        while self.flag:
            jogada = input('Escolha a posição para fazer a sua jogada (linhas coluna):')

            validado = self.Validar_jogada(jogada, self.Jogadas_feitas_do_usuario)

            if validado:
                # Vamos limpar a tala depois de validar a jogada do usuario
                os.system('cls')

                # Para continuar o jogo vamos verificar se alguem ja ganhou, se ja então vamos parar
                if len(self.msg_de_quem_venceu) != 0:
                    break

                self.A_vez_do_usuario = True

                # O metodo não tem argumento porque ele usa as variaveis que são criadas no metodo Validar_jogada
                self.Salvar_jogada()

                # A maquina so vai jogar se o usuario não tiver vencido
                if len(self.msg_de_quem_venceu) == 0:
                    # Antes de fazer a jogada da maquina vamos deixar a variavel falso
                    self.A_vez_do_usuario = False

                    # Apos validar a jogada do usuario agora vamos fazer a jogada da maquina
                    self.Fazer_a_jogada_da_maquna()

                # Vamos imprimir o tabuleiro com a jogada do usuario e da maquina
                self.Imprimir_Tabuleiro()


        # Se saiu do while é porque o jogo acabou, então vamos imprimir a mensagem que foi criada no metodo
        # Adicionar_jogada, a mensagem é uma lista, então vamos mostrar a primeira pessoa que ganhou
        print(self.msg_de_quem_venceu[0])

        self.Jogar_de_novo()




Batalha_Naval(5)

print('Obrigado por jogar!')




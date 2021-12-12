
import os
from time import sleep
from datetime import datetime


class Estacionamento:
    Valor = 2
    Registro = []

    def Quantidde_de_vagas(self, alterar_quantidade_de_vagas):

        def Fazer_a_alteracao():
            validado = Validar_alteracao()

            if validado:
                try:
                    nova_quantidade = int(input('Digite a nova quantidade de vagas:  '))

                    Criar_lista_das_vagas(nova_quantidade)

                except:
                    print('Digite apenas numero para poder ser feito a alteração')

        def Validar_alteracao():
            validado = True
            if len(self.Vagas_ocupadas) != 0:
                print('Impossivel diminuir a quantidade de vagas enquanto tiver carro no estacionamento')
                validado =False

            return validado

        def Criar_lista_das_vagas(qntd_de_vagas):
            self.Vagas_disponiveis.clear()
            self.Vagas_ocupadas.clear()

            cont = 1
            for i in range(qntd_de_vagas):
                vaga = 'V-' + str(cont).zfill(2)
                self.Vagas_disponiveis.append(vaga)

                cont += 1

        if alterar_quantidade_de_vagas:
            Fazer_a_alteracao()

        # Essa opção é para criar uma matriz inicial
        else:
            self.Vagas_disponiveis = []
            self.Vagas_ocupadas = []
            Criar_lista_das_vagas(5)

    def Vagas(self, disponivel_ou_ocupada):
        # Disponivel
        if disponivel_ou_ocupada:
            if len(self.Vagas_disponiveis) == 0:
                print('Não ha vagas disponiveis')
                input('\nPrecione quaquer tecla para continuar!')

            else:
                self.Imprimir_vagas(self.Vagas_disponiveis)

        # Ocupada
        else:
            if len(self.Vagas_ocupadas) == 0:
                print('Todas vagas estão disponiveis')
                input('\nPrecione quaquer tecla para continuar!')

            else:
                self.Imprimir_vagas(self.Vagas_ocupadas)

    def Imprimir_vagas(self, vagas_para_imprimir):

        if vagas_para_imprimir == self.Vagas_disponiveis:
            print(f'Total de vagas disponiveis: {len(self.Vagas_disponiveis)}')

        else:
            print(f'Total de vagas ocupadas: {len(self.Vagas_ocupadas)}')

        if len(vagas_para_imprimir) >= 10:
            print('+------+------+------+------+------+------+------+------+------+------+')
        else:
            print(f'+{"------+" * len(vagas_para_imprimir)}')

        # Vai contar para saber qual é a vaga. EX V02
        cont = 0
        print('|', end='')
        for vaga in vagas_para_imprimir:
            if cont <= 9:
                print(f' {vaga} |', end='')

                # Para zerar o cont
                if cont == 9:
                    print(f'\n+{"------+" * 10}', end='')

                    # Esse if é para saber se esta no ultima vaga da lista, se não tiver então vamos imprimir um "|"
                    if vagas_para_imprimir.index(vaga) != len(vagas_para_imprimir) - 1:
                        print('\n|', end='')

                    cont = 0

                cont += 1

        # Para saber se vai ter que colocar alguns "--" a mais
        if len(vagas_para_imprimir) % 10 != 0:
            qntd = len(vagas_para_imprimir) % 10
            print(f'\n+{"------+" * qntd}')

        input('\n\nPrecione qualquer tecla para continuar!')

    def Motorista(self):
        def Validar_telefone(numero):
            numero.lstrip()
            ddd, telefone = numero.split()
            ddd = ddd.replace(' ', '')
            telefone = telefone.replace(' ', '')

            if len(ddd) == 2 and telefone.isnumeric() and len(telefone) == 9:
                return True, str(ddd) + ' ' + str(telefone)

            else:
                print('Numero invalido, digite como o exemplo a seguir [Ex: 00 900110011]:  ')
                return False, telefone

        motorista = []

        nome = input('Digite o nome do motorista:  ')
        telefone = input('Digite o telefone do motorista: [Ex: 00 900110011] ')

        telefone_valido, telefone = Validar_telefone(telefone)

        motorista.append(nome)
        motorista.append(telefone)

        # No return vamos usar a variavel telefone_valido para saber se esta tudo certo com o numero
        return telefone_valido, motorista

    def Carro(self):
        def Modelo_e_cor():
            modelo = input('Qual o modelo do seu carro:  ')
            cor = input('Qual a cor do seu carro:  ')

            if input(f'O Modelo {modelo} e cor {cor} esta correto? [s/n]  ').lower() == 's':
                return True, modelo, placa

            else:
                return False, modelo, placa

        placa = input('Digite a placa:  ')

        todos_nomeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        todas_letras = []

        for n in range(65, 91):
            todas_letras.append(chr(n))
            # Vamos adicionar a letra "ç"
        todas_letras.append(chr(199))

        placa_valida = True
        for item in placa:
            if not (item.upper() in todas_letras or item in todos_nomeros):
                placa_valida = False

        modelo_e_cor_valido, modelo, cor = Modelo_e_cor()
        carro = []
        carro.append(placa)
        carro.append(modelo)
        carro.append(cor)

        # O "and" é para retornar true so se os dois forem
        return placa_valida and modelo_e_cor_valido, carro

    def Entrada_de_veiculo(self):
        '''
        Esse metodo vai fazer a entrado de um veiculo, então ele vai obter todos os requisitos
        '''

        def Adicionar_carro_na_vaga():
            vaga_valida = False
            try:
                vaga = int(input('Digite o numero da vaga:  '))

                vaga = 'V' + '-' + str(vaga).zfill(2)

                posicao = self.Vagas_disponiveis.index(vaga)

                # Apagando da lista de vagas dispniveis
                self.Vagas_disponiveis.pop(posicao)

                # Adicionando na lista de vagas ocupadas
                self.Vagas_ocupadas.append(vaga)

                vaga_valida = True

            except:
                vaga = ''
                print('Vaga invalida e/ou ja ocupada!')


            return vaga_valida, vaga

        Informacoes = []

        todos_reqquisitos = ['vaga', 'carro', 'data', 'motorista']
        cont = 0
        while True:
            try:
                qual_item = todos_reqquisitos[cont]

                if qual_item == 'vaga':
                    valido, item = Adicionar_carro_na_vaga()

                elif qual_item == 'carro':
                    valido, item = self.Carro()

                elif qual_item == 'data':
                    valido, item = self.Validacoes_da_data()

                else:
                    valido, item = self.Motorista()

                if valido:
                    if type(item) == list:
                        Informacoes += item

                    else:
                        Informacoes.append(item)

                    # Só vamos aumentar o cont se estiver valido o item retornado
                    cont += 1

            except:
                break

        self.Registro.append(Informacoes)

    def Validacoes_da_data(self):

        def Verificar_hora(data):
            # Separando a data que o usaurio digitou...
            hora_em_str, min_em_str = data.split(':')

            # Vamos transformar tudo em numero para ter certeza de que não é uma letra
            hora = int(hora_em_str)
            min = int(min_em_str)

            # Aqui vamos verificar e a hora esta correta
            a_hora_esta_valida = Validar_hora(hora, min)

            # Aqui vamos validar o mes e depois o ano, para o "if" não ficar muito grande
            if a_hora_esta_valida:
                data_sem_espacos = str(hora).zfill(2) + ':' + str(min).zfill(2)
                return True, data_sem_espacos

            else:
                print('Digite uma data valida que seja menor ou igual a atual\n')
                # Vamos retornar as duas variaveis porque se uma for False ira retornar False que é o que queremos
                return False, ''

        def Validar_hora(hora, min):
            min_hoje, hora_hoje = self.Obter_a_data_de_hoje()

            if hora > hora_hoje or hora < 0 or hora >= 24 or min > min_hoje or min < 0 or min >= 60:
                return False

            else:
                return True


        qual_data = input('Você quer usar a data do sistema? [s/n]  ')

        if qual_data.lower() == 's':
            min, hora = self.Obter_a_data_de_hoje()
            return True, str(hora).zfill(2) + ':' + str(min).zfill(2)

        else:
            while True:
                try:
                    data = input('Digite a data de hoje e hora: [Ex: 10:30]  ')

                    data_valida, data_sem_possiveis_espacos = Verificar_hora(data)

                    if data_valida:
                        # Vamos perguntar se é essa a data mesmo
                        a_data_esta_correta = input(f'A data {data_sem_possiveis_espacos} esta correta? [s/n]  ')

                        if a_data_esta_correta.lower() == 's':
                            data = []
                            data.append(data_sem_possiveis_espacos)
                            data.append(input('Escreva o motivo de usar a data manual:  '))
                            return True, data_sem_possiveis_espacos

                except:
                    print('Data invalida')

    def Obter_a_data_de_hoje(self):
        Hoje = datetime.now()

        # Obtendo as informações do dia e horario de hoje...
        hora, min = Hoje.strftime('%H %M').split()

        # Transformando em numero...
        hora = int(hora)
        min = int(min)

        return min, hora

    def Saida_de_veiculo(self):

        def Adicionar_no_arquivo(informacoes):
            with open('saida_de_veiculos.txt', 'a+') as arquivo:
                cont = 0
                for item in informacoes[0]:
                    cont += 1

                    # Para cada item da lista do aluno vamos transformar em str e adicionar um "; "
                    item = str(item) + '; '
                    # Agora vamos salvar essa linha no arquivo
                    arquivo.write(item)

                arquivo.write('\n')

            # Apos ja adicionar no arquivo vamos apagar da variavel
            posicao = self.Registro.index(informacoes)
            self.Registro.pop(posicao)

        def Total_a_pagar(vaga):
            informacoes = []
            # Vamos achar as informações do motorista na lista
            for item in self.Registro:
                # input(item)
                if item[0] == vaga:
                    informacoes.append(item)
                    break

            input(informacoes)
            input(self.Registro)

            # Obtendo a hora...
            tempo_inicial = informacoes[0][4]
            hora, min = tempo_inicial.split(':')
            hora = int(hora)
            min = int(min)

            min_agora, hora_agora = self.Obter_a_data_de_hoje()
            tempo_total = abs(hora_agora - hora) * 60 + (min_agora - min)

            # Antes de mostrar o valor a pagar vamos salvar as informações no arquivo
            # Adicionar_no_arquivo(informacoes)


            # Para saber se é hora certinha. Ex: 10:20  12:20;  12:00 14:00
            if tempo_total % 60 == 0:
                tempo_total = int(tempo_total / 60)
                valor = tempo_total * self.Valor

            # Ja que não esta certinho a hora então vamos pegar o int da divisão e adicionar 1 porque os min passou
            # Ex: 10:30  12:35;  12:00  14:20
            else:
                tempo_total = int(abs(tempo_total) / 60) + 1
                valor = tempo_total * self.Valor

            print(f'Total a pagar é ${valor},00')

            print(f'Obrigado por escolher nosso estacionamento! \nBoa viagem {informacoes[0][5]}, volte sempre!')

            input('\nPrecione qualquer tecla para continuar!')

        def Tirar_o_carro_da_vaga(posicao, vaga):
            # Apagando da lista de vagas ocupadas...
            self.Vagas_ocupadas.pop(posicao)

            # Adicioando na lista de vagas disponiveis...
            self.Vagas_disponiveis.insert(posicao, vaga)

        def Verificar_se_esta_valido(vaga):
            vaga = 'V' + '-' + str(vaga).zfill(2)

            # Vamos achar a vaga para saber se ela realmente esta valida
            posicao = self.Vagas_ocupadas.index(vaga)

            return vaga, posicao

        while True:
            try:
                vaga = int(input('Digite o numero da vaga'))

                vaga, posicao = Verificar_se_esta_valido(vaga)

                decisao = input(f'Quer mesmo tirar o carro da vaga {vaga}? [s/n]  ')

                if decisao.lower() == 's':
                    Total_a_pagar(vaga)
                    Tirar_o_carro_da_vaga(posicao, vaga)
                    break

                else:
                    print('Cancelando...')
                    sleep(2)
                break

            except:
                print('Não tem carro nessa vaga!\n')
                if input('Quer procurarmoutra vaga?  [s/n]'  ).lower() != 's':
                    break

    def Mudar_valor(self):
        while True:
            try:
                novo_valor = float(input('Digite o novo valor a hora:  '))

                if novo_valor > 0:
                    self.Valor = novo_valor
                    break

            except:
                print('Valor invalido!')


class Menu (Estacionamento):

    def __init__(self):
        # Vamos chamar esse metodo para adicionar uma quantidad inicial de vagas
        self.Quantidde_de_vagas(False)

        while True:
            os.system('cls')

            print(f'{"=" * 30} MENU {"=" * 30}')
            print('1 - Configurações do Sistema \n2 - Vagas Disponíveis  \n3 - Vagas Ocupadas '
                  '\n4 - Entrada de Veículo \n5 - Saída de Veículo \n6 - Sair')
            try:
                escolha = int(input('\nDigite a opção desejada:  '))

                if escolha == 6:
                    break

                elif escolha >= 1 and escolha <= 5:
                    self.Direcionando_opcao_escolhida(escolha)

                else:
                    print('Por favor, digite uma opção existente!')

            except:
                print('Por favor, digite uma opção existente!')

    def Direcionando_opcao_escolhida(self, opcao):
        if opcao == 1:
            self.Menu_da_opcao_1()

        elif opcao == 2:
            self.Vagas(True)

        elif opcao == 3:
            self.Vagas(False)

        elif opcao == 4:
            self.Entrada_de_veiculo()

        elif opcao == 5:
            self.Saida_de_veiculo()

    def Menu_da_opcao_1(self):
        def Opcao_escolhida(opcao):
            if opcao == 1:
                self.Quantidde_de_vagas(True)

            elif opcao == 2:
                self.Mudar_valor()

            else:
                Menu()

        while True:
            try:
                print('1 - Alterar a quantidade de vagas \n2 - Alterar o valor da hora \n3 - Voltar')
                opcao = int(input('\nEscolha uma opção: '))

                if opcao >= 1 and opcao <= 3:
                    Opcao_escolhida(opcao)
                    break

                else:
                    print('Opção invalida!')

            except:
                print('Digite uma opção valida')


Menu()




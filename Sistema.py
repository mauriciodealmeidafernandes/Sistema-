# 1 - Pessoa Física / 2 - Pessoa Jurídica / 3 - Sair
# 1 - Cadastrar Pessoa Física / 2 - Listar Pessoa Física / 3 - Sair
# 1 - Cadastrar Pessoa Jurídica / 2 - Listar Pessoa Jurídica / 3 - Sair


from datetime import date, datetime
from Pessoa import PessoaFisica, Endereco


def main():
    lista_pf= []
    while True:
        opcao = int(input("Escolha uma opção: 1 - Pessoa Física / 2 - Pessoa Jurídica / 0 - Sair"))
        if opcao == 1:
            while True:
                opcao_pf= int(input("Escolha uma opção: 1 -  Cadastrar Pessoa Física / 2 - Listar Pessoa Física / 0 - Sair"))
                #Cadastrar uma Pessoa Física
                if opcao_pf == 1:
                    novapf = PessoaFisica()
                    novo_end_pf = Endereco() 

                    novapf.nome= input("Digite o nome de pessoa física")
                    novapf.cpf= input("Digite o CPF")
                    novapf.rendimento= float(input("Digite o rendimento mensal (Digite somente numeros):"))

                    data_nascimento= input("Digit a data de nascimento (dd/mm/aaaa)") #solicita a data de nascimento
                    novapf.dataNascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
                    idade = (date.today() - novapf.dataNascimento).days // 365 #calcula a idade da pessoa

                    if idade >= 18:
                        print("A pessoa tem mais de 18 anos")

                    else:
                        print("A pessoa tem menos de 18 anos")

                        continue # Retornar ao inicio do loop

                    # CADASTRO DE ENDEREÇO

                    novo_end_pf.logradouro = input("Digite o logradouro: ")
                    novo_end_pf.numero = input("Digite o número: ")
                    end_comercial = input("Este endereco é comercial? S/N: ") #socitar se o endereço é comercial 
                    novo_end_pf.endereco_Comercial= end_comercial.strip().upper()== 'S' #define se o endereço é comercial

                    novapf.endereco = novo_end_pf

                    lista_pf.append(novapf)

                    print("Cadastro realizado com sucesso!")

                elif opcao_pf == 2:
                    if lista_pf:
                        for cada_pf in lista_pf:
                            print(f'Nome: {cada_pf.nome}')
                            print(f'CPF>{cada_pf.cpf}')
                            print(f'Endereco:{cada_pf.endereco.logradouro},{cada_pf.endereco.numero}')
                            print(f'Data Nascimento:{cada_pf.dataNascimento.strftime('%d/%m/%Y')}')
                            print(f'Imposto a ser pago:{cada_pf.calcular_imposto(cada_pf.rendimento)}')
                            print("Digite 0 para sair")
                            input()
                    else:
                        print("Lista Vazia")
        #SAIR DO MENU ATUAL
                elif opcao_pf == 0:
                    print("Voltando ao menu anterior")
                    break

                else:
                    print("Opção inválida! Por favor, digite uma das opções abaixo:")

        elif opcao_pf == 2:
            print("Funcionalidade para pessoa juridica não implementadas")
            pass  #utilizado para indicar que futuramente será feito código

        elif opcao_pf == 0:
            print("Obrigada por utilizar nosso sistema!")
            break

        else:
            print("Opção inválida! Por favor, digite uma das opções válidas!")


if __name__ == "__main__":
    main() #chama a função principal
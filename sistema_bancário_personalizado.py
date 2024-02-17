menu = """
[c] Criar conta
[d] Depositar
[s] Sacar
[t] Transferir
[e] Extrato
[q] Sair
=> """

class Conta:
    def __init__(self, nome, saldo=0, limite=500):
        self.nome = nome
        self.saldo = saldo
        self.limite = limite
        self.extrato = []
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            return True
        else:
            return False

    def sacar(self, valor):
        if valor > self.saldo:
            return False, "Saldo insuficiente"
        elif valor > self.limite:
            return False, "Valor excede o limite de saque"
        elif self.numero_saques >= self.LIMITE_SAQUES:
            return False, "Número máximo de saques excedido"
        elif valor <= 0:
            return False, "Valor inválido"
        else:
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            self.numero_saques += 1
            return True, "Saque realizado com sucesso"

    def transferir(self, destinatario, valor):
        if valor > self.saldo:
            return False, "Saldo insuficiente"
        elif valor <= 0:
            return False, "Valor inválido"
        else:
            self.saldo -= valor
            destinatario.saldo += valor
            self.extrato.append(f"Transferência enviada para {destinatario.nome}: R$ {valor:.2f}")
            destinatario.extrato.append(f"Transferência recebida de {self.nome}: R$ {valor:.2f}")
            return True, "Transferência realizada com sucesso"

    def ver_extrato(self):
        return self.extrato

contas = {}

while True:
    opcao = input(menu)

    if opcao == "c":
        nome = input("Informe o nome do cliente: ")
        if nome not in contas:
            contas[nome] = Conta(nome)
            print(f"Conta para {nome} criada com sucesso!")
        else:
            print("Conta já existe para este cliente.")

    elif opcao == "d":
        nome = input("Informe o nome do cliente: ")
        if nome in contas:
            valor = float(input("Informe o valor do depósito: "))
            if contas[nome].depositar(valor):
                print("Depósito realizado com sucesso")
            else:
                print("Operação não realizada! O valor informado é inválido.")
        else:
            print("Conta não encontrada")

    elif opcao == "s":
        nome = input("Informe o nome do cliente: ")
        if nome in contas:
            valor = float(input("Informe o valor do saque: "))
            sucesso, mensagem = contas[nome].sacar(valor)
            if sucesso:
                print(mensagem)
            else:
                print("Operação não realizada:", mensagem)
        else:
            print("Conta não encontrada")

    elif opcao == "t":
        remetente = input("Informe o nome do remetente: ")
        destinatario = input("Informe o nome do destinatário: ")
        valor = float(input("Informe o valor da transferência: "))
        if remetente in contas and destinatario in contas:
            sucesso, mensagem = contas[remetente].transferir(contas[destinatario], valor)
            if sucesso:
                print(mensagem)
            else:
                print("Operação não realizada:", mensagem)
        else:
            print("Conta não encontrada")

    elif opcao == "e":
        nome = input("Informe o nome do cliente: ")
        if nome in contas:
            print("\n ================== EXTRATO ==================")
            extrato = contas[nome].ver_extrato()
            print("Não foram realizadas movimentações." if not extrato else "\n".join(extrato))
            print(f"\nSaldo: R$ {contas[nome].saldo:.2f}")
            print("==========================================")
        else:
            print("Conta não encontrada")

    elif opcao == "q":
        break  

    else:
        print("Operação inválida, selecione novamente a operação desejada.")

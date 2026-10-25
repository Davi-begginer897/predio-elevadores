class Elevador:
    def __init__(self, nome):
        self.nome = nome
        self.__andar_atual = 1
    def capacidade(self):
        return "Sem limite definido"
    
    def mostrar_status(self): 
        print(f"Elevador {self.nome} está no andar {self.__andar_atual}") 

    def subir(self):
        if self.__andar_atual < 15:
            self.__andar_atual += 1
        else:
            print(f"O elevador {self.nome} já está no último andar! ")
    
    def descer(self):
        if self.__andar_atual > 1:
            self.__andar_atual -= 1
        else: 
            print(f"O Elevador {self.nome} já está no primeiro andar!")       

    def get_andar(self): #getter
        return self.__andar_atual

    def set_andar(self, novo_andar):
        if 1 <= novo_andar <= 15:
            self.__andar_atual = novo_andar
        else:
            print(f"Andar {novo_andar} inválido! O prédio vai de 1 a 15. ")    
#Classe filha da classe mãe elevador -- HERANÇA POO
class ElevadorDeCarga(Elevador):
    def __init__(self, nome, capacidade_kg):
        super().__init__(nome)
        self.capacidade_kg = capacidade_kg
        self.carga_atual = 0
    
    def capacidade(self):
        return f"{self.capacidade_kg} kg no total."
    
    def carregar(self, kg):
        if self.carga_atual + kg > self.capacidade_kg:
            print(f"A carga excede o limite de {self.capacidade_kg} kg com {self.capacidade_kg - self.carga_atual} kg a mais!")
        else:
            self.carga_atual +=kg

    def mostrar_status(self):
        print(f"Elevador de carga {self.nome} no andar {self.get_andar()} está com {self.carga_atual}/{self.capacidade_kg} kg")

class ElevadorSocial(Elevador):
    def __init__(self, nome, capacidade_pessoas):
        super().__init__(nome)
        self.capacidade_pessoas = capacidade_pessoas
        self.pessoas_atuais = 0

    def capacidade(self):
        return f"{self.capacidade_pessoas} pessoas."

    def entrar(self, qtd):
        if self.pessoas_atuais + qtd > self.capacidade_pessoas:
            print(f"O elevador {self.nome} não comporta mais {qtd} pessoa(s). Capacidade Máxima: {self.capacidade_pessoas}.")
        else:
            self.pessoas_atuais +=qtd

    def sair(self, qtd):
        if self.pessoas_atuais < qtd:
            print(f"O elevador {self.nome} não tem {qtd} de pessoas no seu interior. ")
        else:
            self.pessoas_atuais -= qtd

    def mostrar_status(self):
        print(f"O elevador Social {self.nome} está no andar {self.get_andar()} com {self.pessoas_atuais}/{self.capacidade_pessoas}")

class ElevadorPanoramico(Elevador):
        def capacidade(self):
            return "6 pessoas, vista panorâmica"
        def mostrar_status(self):
            print(f"O elevador Panorâmico {self.nome} está no andar {self.get_andar()}")

def relatorio(elevador):
        print("--- Relatório ---")
        elevador.mostrar_status()
        print("Capacidade:", elevador.capacidade())

elevador_a = Elevador("A")
elevador_b = Elevador("B")
elevador_c = Elevador("C")

for _ in range(3):
    elevador_a.subir()
for _ in range(7):
    elevador_b.subir()
for _ in range(2):
    elevador_b.descer()

elevadores = [elevador_a, elevador_b, elevador_c]
for elevador in elevadores:
    elevador.mostrar_status()


andar_destino = 14
mais_proximo = elevadores[0]

for elevador in elevadores:
    if abs(elevador.get_andar() - andar_destino) < abs(mais_proximo.get_andar() - andar_destino):
        mais_proximo = elevador

print(f"O elevador {mais_proximo.nome} é o mais próximo do andar {andar_destino}!")

#teste elevador de carga
carga = ElevadorDeCarga("Carga 1 ", 500)
carga.subir()
carga.subir()
carga.mostrar_status()
print(carga.capacidade_kg)
carga.carregar(300)
carga.carregar(300)
carga.mostrar_status()

#teste elevador social
social = ElevadorSocial("S1", 8)
for _ in range(4):
    social.subir()
social.entrar(3)
social.mostrar_status()
social.entrar(7)
social.sair(2)
social.sair(5)
social.mostrar_status()

#Exemplo de Polimorfismo (Cada elevador mostra o status do seu jeito, e o laço não verifica o tipo de nenhum. O Python decide qual versão chamar olhando para o objeto.)
print("="*30)

elevadoresA_B = [
    Elevador("D"),
    ElevadorDeCarga("C1", 500),
    ElevadorSocial("S1",8),
    ElevadorPanoramico("P1")
]

for e in elevadoresA_B:
        e.mostrar_status()
        print(f"{e.nome}: {e.capacidade()}")

for e in elevadoresA_B:
    relatorio(e)


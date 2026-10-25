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
    
    def ir_para(self, destino):
        if not 1 <= destino <= 15:
            print(f"Andar {destino} inválido! O prédio vai de 1 a 15.")
            return
        while self.get_andar() < destino:
            self.subir()
            print(f"Elevador {self.nome} no andar {self.get_andar()}")
        while self.get_andar() > destino:
            self.descer()
            print(f"Elevador {self.nome} no andar {self.get_andar()}")

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
            print(f"O elevador {self.nome} não tem {qtd} de pessoa(s).")
        else:
            self.pessoas_atuais -= qtd

    def mostrar_status(self):
        print(f"O elevador Social {self.nome} está no andar {self.get_andar()} com {self.pessoas_atuais}/{self.capacidade_pessoas}")

class ElevadorDeCarga(Elevador):
    def __init__(self, nome, capacidade_kg):
        super().__init__(nome)
        self.capacidade_kg = capacidade_kg
        self.carga_atual = 0
    
    def capacidade(self):
        return f"{self.capacidade_kg} kg no total."
    
    def carregar(self, kg):
        if self.carga_atual + kg > self.capacidade_kg:
            excesso = self.carga_atual + kg - self.capacidade_kg
            print(f"A carga excede o limite de {self.capacidade_kg} kg em {excesso} kg!")
        else:
            self.carga_atual +=kg

    def mostrar_status(self):
        print(f"Elevador de carga {self.nome} no andar {self.get_andar()} está com {self.carga_atual}/{self.capacidade_kg} kg")

class ElevadorPanoramico(Elevador):
    def capacidade(self):
        return "6 pessoas, vista panorâmica"
    def mostrar_status(self):
        print(f"O elevador Panorâmico {self.nome} está no andar {self.get_andar()}")

class Predio:
    def __init__(self):
        self.elevadores = []

    def adicionar(self, elevador):
        self.elevadores.append(elevador)

    def elevador_mais_proximo(self, andar):
        if not self.elevadores:
            return None
        mais_proximo = self.elevadores[0]
        for elevador in self.elevadores:
            if abs(elevador.get_andar() - andar) < abs(mais_proximo.get_andar() - andar):
                mais_proximo = elevador
        return mais_proximo

    def chamar(self, andar):
        
        if not 1 <= andar <= 15:
            print(f"Andar {andar} inválido! O prédio vai de 1 a 15.")
            return
        elevador = self.elevador_mais_proximo(andar)
        if elevador is None:
            print("Não há elevadores no prédio.")
            return
        print(f"\nChamado no andar {andar}: elevador {elevador.nome} atendeu (estava no andar {elevador.get_andar()})")
        elevador.ir_para(andar)

if __name__ == "__main__":
    predio = Predio()
    predio.adicionar(Elevador("A"))
    predio.adicionar(ElevadorDeCarga("C1", 500))
    predio.adicionar(ElevadorSocial("S1", 8))
    predio.adicionar(ElevadorPanoramico("P1"))

    predio.chamar(10)
    predio.chamar(4)
    predio.chamar(12)
    
    print("\n--- Testes extras ---")
    carga = ElevadorDeCarga("C2", 500)
    carga.carregar(300)
    carga.carregar(300)
    carga.mostrar_status()

    social = ElevadorSocial("S2", 8)
    social.entrar(3)
    social.entrar(7)
    social.sair(5)
    social.sair(2)
    social.mostrar_status()

    predio.chamar(20)
    Predio().chamar(5)
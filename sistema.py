# Sistema de adoção de gatinhos :)

from abc import ABC, abstractclassmethod

class Animal(ABC): #objeto
    def __init__(self, nome, idade, cor):
       self.__nome = nome 
       self.__idade = idade
       self.__cor = cor

    def get_nome(self):
        return self.__nome
    def get_idade(self):
        return self.__idade
    def get_cor(self):
        return self.__cor
    
    @abstractclassmethod
    def fazer_som(self): # método abstrato que deve ser implementado nas subclasses
        pass
    
# Herança Simples
    
class Gato(Animal):
    def __init__(self, nome, idade, cor, raca):
        super().__init__(nome, idade, cor)
        self.__raca = raca

    def get_raca(self):
        return self.__raca
    
    def fazer_som(self):
        return "Miau"
    

gatinho1 = Animal("Bolinha", 2, "branco") #criando animal
gatinho2 = Animal("Python", 3, "Preto")
gatinho3 = Gato("Frajola", 3,"Preto e branco", "Persa")

print(gatinho1.get_nome())
print(gatinho1.get_idade())
print(gatinho2.get_cor())
print(gatinho3.get_raca())

# Herança múltipla

class Adotante:
    def __init__(self,nome) :
        self.nome = nome

class AdocaoGatinho:
    def __init__(self, animal, adotante):
        self.animal = animal
        self.adotante = adotante

animal01 = Animal("Maker", 2,"Amarelo")
animal02 = Animal("Lion", 4,"Cinza")
animal03 = Animal("Jade", 1,"Tigrado")
animal04 = Animal("Bob", 2,"Preto")

adotante01 = Adotante("Isadora")
adotante02 = Adotante("Isabela")
adotante03 = Adotante("Camila")

#criar uma instancia de adoção

adocao01 =AdocaoGatinho(animal01, adotante01)
adocao02 =AdocaoGatinho(animal02, adotante02)

print("Nome do gatinho 1 adotado:", adocao01.animal.get_nome())
print("Idade do gatinho 1 adotado:", adocao01.animal.get_idade())
print("Nome do adotante do gatinho 2",adocao02.adotante.nome)



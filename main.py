# NOTE: 
import random


# NOTE: cria a classe
class  Pessoa:
    # os atributos são SEMPRE definidos dentro do  metodo construtos
    # NOTE: metodo construtos
    def __init__(self, nome, humor): 
    
      self.nome = nome
      self.humor = humor




# NOTE: COMPRIMENTAR
def cumprimentar(self):
   if self.humor:
      print(f'ola, ,eu nome é {self.nome}. Qual e o seu nome?')
   else:
      print(f'ta olhando o que? se manca....') 


def responder(self, nome, humor):
   if humor:
      print(f'ola {nome}, meu nome é {self.nome}.  prazer em te conhecer')
      self.humor = True
   else:
      print(f'vai se lascar, infeliz.')
      self.humor = False
      return self.humor
      

# NOTE: Programa principal
if __name__ == '__main__':
   
   humores = (True, False)
   nome1 =  input('Informe nome do 1º usuario: ')
   nome2 =  input('Informe nome do 2º usuario: ')

   # instancia do objeto
   usuario1 = Pessoa(nome1, humores[random.randint(0,1)])
   usuario2 = Pessoa(nome2, humores[random.randint(0,1)])

   usuario1.cumprimentar()
   usuario1.humor =  usuario2.responder(usuario1.nome, usuario2.humor)

   if usuario1.humor:
      print(f'{usuario1.nome} ficou feliz.')
   else:
      print(f'{usuario1.nome} ficou triste.')

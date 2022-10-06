from endereco import *
class pessoa:

  def __init__(self):
    self.__nome=input('insira seu nome: ')
    self.__numero=input('insira seu número: ')
    self.enderecoatual=endereco()

  def consultanome(self):
    return self.__nome

  def consultaendereco(self):
    return self.enderecoatual
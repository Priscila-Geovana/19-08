class endereco:

  def __init__(self):
    self.__logradouro=input('insisra o nome do endereço: ')
    self.__cidade=input('insira o nome da cidade: ')
    self.__estado=input('insira o nome do estado: ')

  def consultalogradouro(self):
    return self.__logradouro
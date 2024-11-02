class estoque:
    def __init__(self, nome: str, preco: float, quantidade: int)->None:
        """ iniciando minha classe


        args:

          nome(str): nome do estoque
          preco(float): preco do estoque
          quantidade(int): quantidade do estoque

        returns:
          
          None
        """


        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def exibir_informaçoes(self)->None:
       """ #abrindo uma função pra exibir as informaçoes do estoque
      
      Args:
        
        None
      
      
      Returns:
       
        None
      """



       print("informaçoes do estoque:")
       print(f"Nome: {self.nome}")
       print(f"preco: {self.preco}")
       print(f"quantidade: {self.quantidade}")

    def atualizar_nome(self, novo_nome: str)-> None:
        """criando essa função pra trocar nomes ou ate mesmo corrigir erro de digitação
      args:

       novo_nome(str): novo nome do estoque.
       """
        self.nome = novo_nome
        print(f"nome atualizado")

      
     
        

    def atualizar_preco(self, novo_preco: float)-> None:
        """utilizando essa função pra fazer alteração de preços
      args:

       novo_preco(float): novo preço do estoque.
      """
      
        self.preco = novo_preco
        print(f"preço atualizado para R${self.preco: .2f}")

    def atualizar_quantidade(self, nova_quantidade: int)-> None:
        """criando essa funçao pra fazer alteração de quantidade

      args:

       nova_quantidade(int): nova quantidade do estoque.
      """
        self.quantidade = nova_quantidade
        print(f"quantidade atualizada para {self.quantidade}")

        




        

        

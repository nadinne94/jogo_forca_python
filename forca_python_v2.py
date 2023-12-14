# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random
from os import system, name

# Função para limar a tela a cada execução
def limpa_tela():
 
    # Windows
    if name == 'nt':
        _ = system('cls')
 
    # Mac ou Linux
    else:
        _ = system('clear')

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

	# Método Construtor
    def __init__(self, palavra):
        
        self.palavra = palavra
        self.letras_erradas = []
        self.letras_escolhidas = []

	# Método para adivinhar a letra
    def guess(self, letra):

        if letra in self.palavra and letra not in self.letras_escolhidas:
             self.letras_escolhidas.append(letra)

        elif letra not in self.palavra and letra not in self.letras_erradas:
            self.letras_erradas.append(letra)
        
        else:
            return False
        
        return True

	# Método para verificar se o jogo terminou
    def hangman_over(self):
        return self.hangman_won() or (len(self.letras_erradas) == 6)
        
	# Método para verificar se o jogador venceu

    def hangman_won(self):

        if '_' not in self.hide_palavra():
            return True
        else:
            return False
		
	# Método para não mostrar a letra no board

    def hide_palavra(self):

        rtn = ''

        for letra in self.palavra:
            if letra not in self.letras_escolhidas:
                rtn +='_ '
            else:
                rtn += letra
        return rtn
		
	# Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        print (board[len(self.letras_erradas)])

        print ('\nPalavra: ' + self.hide_palavra())

        print ('\nLetras erradas ',)

        for letra in self.letras_erradas:
            print(letra,)
        
        print()
        print('Letras corretas ',)

        for letra in self.letras_escolhidas:
            print(letra,)
        
        print()

def rand_palavra():
    palavra = ['laranja','pera','banana', 'uva', 'morango', 'abacaxi', 'abacate', 'caqui','ameixa', 'goiaba', 'manga']

    palavra = random.choice(palavra)

    return palavra

def main():
    limpa_tela()
    print("\nBem vindo ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")

    game = Hangman(rand_palavra())

    while not game.hangman_over():
        game.print_game_status()

        user_input = input('\nDigite uma palavra: ')

        game.guess(user_input)
    
    game.print_game_status()

    if game.hangman_won():
        print('\nParabéns! Você venceu!!')
    
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.palavra)
    
if __name__ == '__main__':
    main()
    
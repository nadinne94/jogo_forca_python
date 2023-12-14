# Jogo da Forca aplicando Programação Orientada a Objetos
<div align='justify'>

A nova versão do jogo da forca foi elaborada explorando os conceitos de Programação Orientada a Objetos.

### Importações e Função para Limpar a Tela:
Comecei importando as bibliotecas necessárias e criando uma função chamada `limpa_tela()` para garantir uma interface mais limpa a cada execução do jogo. Isso proporcionou um visual mais organizado.

```python
import random
from os import system, name

def limpa_tela():
    # Código para limpar a tela, dependendo do sistema operacional
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
```

### Tabuleiro do Jogo:
Defini um tabuleiro com representações visuais da forca em diferentes estágios. Isso adiciona um toque interativo e visual ao jogo.

```python
board = ['''  
>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''
... (outros estágios do tabuleiro) ...
=========''']
```

### Classe Hangman:
Em seguida, criei a classe `Hangman` que encapsula a lógica do jogo. O método construtor `__init__` inicializa a palavra a ser adivinhada, as letras erradas e as letras escolhidas.

```python
class Hangman:
    def __init__(self, palavra):
        self.palavra = palavra
        self.letras_erradas = []
        self.letras_escolhidas = []
```

### Método para Adivinhar a Letra:
Implementei o método `guess()` para verificar se a letra escolhida está na palavra. As letras são adicionadas às listas apropriadas, e o método retorna True ou False.

```python
    def guess(self, letra):
        if letra in self.palavra and letra not in self.letras_escolhidas:
            self.letras_escolhidas.append(letra)
        elif letra not in self.palavra and letra not in self.letras_erradas:
            self.letras_erradas.append(letra)
        else:
            return False
        return True
```

### Métodos para Verificar o Status do Jogo:
Implementei métodos como `hangman_over()`, `hangman_won()`, e `hide_palavra()` para verificar se o jogo terminou, se o jogador venceu, e para ocultar as letras ainda não adivinhadas.

```python
    def hangman_over(self):
        return self.hangman_won() or (len(self.letras_erradas) == 6)

    def hangman_won(self):
        return '_' not in self.hide_palavra()

    def hide_palavra(self):
        rtn = ''
        for letra in self.palavra:
            if letra not in self.letras_escolhidas:
                rtn += '_ '
            else:
                rtn += letra
        return rtn
```

### Método para Imprimir o Status do Jogo:
O método `print_game_status()` imprime o tabuleiro, a palavra oculta e as letras escolhidas/erradas na tela.

```python
    def print_game_status(self):
        print(board[len(self.letras_erradas)])
        print('\nPalavra: ' + self.hide_palavra())
        print('\nLetras erradas ',)
        for letra in self.letras_erradas:
            print(letra,)
        print()
        print('Letras corretas ',)
        for letra in self.letras_escolhidas:
            print(letra,)
        print()
```

### Função para Palavra Aleatória:
Criei uma função `rand_palavra()` que retorna uma palavra aleatória da lista.

```python
def rand_palavra():
    palavra = ['laranja', 'pera', 'banana', 'uva', 'morango', 'abacaxi', 'abacate', 'caqui', 'ameixa', 'goiaba', 'manga']
    palavra = random.choice(palavra)
    return palavra
```

### Função Principal (main):
Na função principal `main()`, iniciei o jogo, interagindo com o usuário para adivinhar a palavra até que o jogo termine.

```python
def main():
    limpa_tela()
    print("\nBem vindo ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")
    game = Hangman(rand_palavra())
    
    while not game.hangman_over():
        game.print_game_status()
        user_input = input('\nDigite uma letra: ')
        game.guess(user_input)
    
    game.print_game_status()

    if game.hangman_won():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.palavra)

if __name__ == '__main__':
    main()
```
</div>

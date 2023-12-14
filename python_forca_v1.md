# Jogo da Forca em Python
## Projeto de conclusão do módulo introdutório do curso de Python da DSA
<div align="justify">

### Introdução:
No âmbito do módulo introdutório do curso de Python, foi proposto o desenvolvimento de um projeto prático para consolidar os conceitos aprendidos. Neste artigo, vou detalhar o código criado, uma versão simples do clássico jogo da forca. Este projeto permitiu aplicar os conhecimentos adquiridos nos capítulos iniciais do curso, proporcionando uma experiência prática e divertida.

### Importações:
No início do código, realizamos as importações necessárias. A biblioteca **random** foi utilizada para facilitar a seleção aleatória de palavras, e a função **system** da biblioteca **os** foi empregada para limpar a tela entre as execuções do jogo.
```
import random 
from os import system, name
```
### Função para Limpar a Tela:
Para manter a interface do jogo mais limpa a cada execução, foi implementada a função **limpa_tela()**. Esta função detecta o sistema operacional em uso e executa o comando apropriado para limpar a tela.
```
def limpa_tela():
  if name == 'nt':
    _ = system('cls')
  else:
    _ = system('clear')
```
### Função Principal do Jogo:
A função **game()** é a peça central do projeto. Aqui está um resumo dos passos executados dentro dela:

**1. Apresentação Inicial**:
- Limpo a tela.
- Apresento uma mensagem de boas-vindas e instruções para o jogador.
```
def game():
  limpa_tela()
  print('\nBem-vindo(a) ao jogo da forca!')
  print('Advinhe a palavra abaixo:\n')
```
**2. Palavras para o Jogo:**
- Criei uma lista de palavras que serão usadas no jogo da forca.
```
  palavras = ['banana','abacate','uva','morango','laranja','pera','abacaxi','mamão','caqui','manga']
```
**3. Escolha Aleatória da Palavra:**
- Utilizei a função random.choice() para escolher aleatoriamente uma palavra da lista.
```
  palavra = random.choice(palavras)
```
**4. Inicialização das Listas:**
- Utilizei uma list comprehension para criar a lista letras_descobertas, inicialmente preenchida com underscores, representando as letras ainda não descobertas.
- Defini o número inicial de chances como 6.
- Criei uma lista vazia letras_erradas para armazenar as letras que foram tentadas mas não estão na palavra.
```
  letras_descobertas = ['_' for letra in palavra]
  chances = 6
  letras_erradas = []
```
**5. Loop Principal:**
- Criei um loop que continua enquanto o número de chances é maior que zero.
- Durante cada iteração, exibo as letras descobertas, o número de chances restantes e as letras erradas já tentadas.
- Solicito uma letra ao jogador.
```
  while chances > 0:
    # Exibição das informações do jogo
    print(' '.join(letras_descobertas))
    print('\nChances restantes:', chances)
    print('Letras erradas',' '.join(letras_erradas))
  
    # Entrada do jogador
    tentativa = input('\nDigite uma letra: ').lower()
```
**6. Verificação da Tentativa:**
- Verifico se a letra tentada está na palavra.
- Se estiver, atualizo a lista de letras descobertas.
- Se não estiver, reduzo o número de chances e adiciono a letra à lista de letras erradas.
```
    if tentativa in palavra:
      # Atualização das letras descobertas
      index = 0
      for letra in palavra:
        if tentativa == letra:
          letras_descobertas[index] = letra
          index += 1
        else:
          # Redução de chances e registro da letra errada
          chances -= 1
          letras_erradas.append(tentativa)
```
**7. Verificação de Vitória ou Derrota:**
- Verifico se todas as letras foram descobertas. Se sim, o jogador venceu e o jogo é encerrado.
- Se ainda houver underscores na lista letras_descobertas, o jogador perdeu.
```
        if '_' not in letras_descobertas:
          print('\nVocê venceu, a palavra era: ', palavra)
          break
      
      if '_' in letras_descobertas:
        print('\nVocê perdeu, a palavra era:', palavra)
```
**8. Conclusão:**
Ao final do código, adiciono uma verificação para garantir que a função game() seja chamada apenas quando o script é executado diretamente, não quando é importado como um módulo. Isso evita que o jogo seja iniciado automaticamente se o arquivo for importado em outro script.
```
if __name__ == "__main__":
    game()
    print("\nMeu primeiro jogo em Python :)\n")
```
</div>




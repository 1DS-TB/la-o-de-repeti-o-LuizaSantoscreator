# Lista laço de repetição

## `Aviso`
- Válide as entradas fornecidas pelos usuarios, ou seja, verificar se ele digitou algo invalido: Exemplo: Numero negativo em idade. Caso seja fornecido uma entrada invalida, retornar APENAS o texto "INVALIDO"
- Prestar atenção ao nome do arquivo de cada exercicio
- Não esquecer de enviar ( push ), para o repositório criado para você

## Exercicio 1 -> `exercicio1.py`
Escreva um programa que use um laço for para imprimir os números de 1 a 10.

## Exercicio 2 -> `exercicio2.py`
Peça ao usuário um número inteiro positivo N e calcule a soma de todos os números de 1 até `N` usando um laço `while`.

## Exercicio 3 -> `exercicio3.py`
Peça ao usuário um número e exiba sua tabuada de multiplicação de 1 a 10 usando um laço `for`.

## Exercicio 4 -> `exercicio4.py`
Peça ao usuário um número inteiro positivo e calcule seu fatorial usando um laço `for` ou `while`.
Exemplo: `5! = 5 × 4 × 3 × 2 × 1 = 120`.

## Exercicio 5 -> `exercicio5.py`
Peça ao usuário um número e verifique se ele é primo usando um laço. Um número primo é divisível apenas por 1 e por ele mesmo.

## Exercicio 6 -> `exercicio6.py`
Peça ao usuário um número `N` e gere os primeiros `N` termos da sequência de Fibonacci usando um laço.
Exemplo: `0, 1, 1, 2, 3, 5, 8....`

## Exercicio 7 -> `exercicio7.py`
Peça ao o usuário um numero `N`. E o utilize laços aninhados para imprimir o seguinte padrão :
`N = 5`
```
*
**
***
****
*****
```

## Exercicio 8 -> `exercicio8.py`
Calcule a soma da série harmônica até `N` termos:
`S = 1 + 1/2 + 1/3 + ... + 1/N.`
Arredonde o resultado para 2 casas decimais.

## Exercicio 9 -> `exercicio9.py`
Um número perfeito é aquele cuja soma de seus divisores (exceto ele mesmo) é igual a ele mesmo.
Ex: `6` (1 + 2 + 3 = 6).
Encontre todos os números perfeitos entre 1 e 10000 usando laços.

## Exercicio 10 -> `exercicio10.py`
Implemente um algoritmo que encontre e imprima todos os números de Kaprekar em um intervalo definido pelo usuário (ex: 1 a 10000). Onde você irá solicitar os 2 numeros do intervalo

### O que é um número de Kaprekar?
Um número `K` de `n` dígitos é Kaprekar se, ao elevar `K` ao quadrado, a soma das duas partes do resultado (esquerda e direita) for igual a `K`.

### Regras específicas:
Se `K²` tem um número ímpar de dígitos, a parte direita deve ter `n` dígitos, e a parte esquerda terá o restante.

- Exemplo: `K = 297` (n = 3 dígitos).
  - K² = 297² = 88209.
  - Parte direita: 209 (3 dígitos).
  - Parte esquerda: 88.
  - Soma: 88 + 209 = 297 (é Kaprekar).
- Se a parte direita for composta apenas de zeros, o número não é Kaprekar.
  - Exemplo: K = 100 → 100² = 10000 → Partes 100 + 00 = 100, mas é inválido.
- O número 1 é considerado Kaprekar (1² = 1 → 0 + 1 = 1).

## Exercicio 11
Criar um jogo onde dois jogadores (ou um jogador e a CPU) lutam em turnos até que um seja derrotado.

### Regras Básicas:
1. Cada personagem tem vida (HP), ataque e defesa.
2. O jogador escolhe entre atacar ou curar a cada turno.
3. O jogo mostra o resultado de cada ação e o estado atual dos combatentes.
4. Vence quem reduzir o HP do oponente a zero.

### Regras especificas:
1. O dano e a defesa do jogador e do inimigo é sorteado aleatóriamente no inicio do game. Com valores possiveis entre 1 e 50
   1.1 utilize a biblioteca `random`
   ``` python
   import random
   numero_aleatorio = random.randint(numero_inicial, numero_final)
   ```
   1.2 Sortear também a quantidade de vida. Com valores ente 200 e 1000. O HP de ambos deve ser o mesmo


2. A ação do inimigo deve ser aleatória entre atacar ou curar
   2.1 Utilize a biblioteca random
   ``` python
   import random
   escolha = random.choices(["atacar", "curar"])
   ```
   
3. O dano causado, será o maior valor entre 0 e ataque - defesa, portanto o dano não poderá ser negativo.
4. Criar um menu com opções para iniciar o game sair do game
   4.1. Quando alguem vencer, deve ser dado uma mensagem e retornado para a tela de menu.
5. Exemplo de tela:
``` terminal
=== DUELO DE HERÓIS ===
=== Você            ===
HP:  725     
ATQ: 27      DEF: 8

=== Inimigo         ===
HP:  725
ATQ: 12       DEF: 26

--- Turno 1 ---
Seu HP: 725 | Inimigo HP: 725
Sua vez: [1] Atacar ou [2] Curar? 1
Você ataca! Inimigo perde 1 HP.
Inimigo ataca! Você perde 4 HP.

--- Turno 2 ---
Seu HP: 721 | Inimigo HP: 724
Sua vez: [1] Atacar ou [2] Curar? 2
Você se cura em 20 HP!
Inimigo ataca! Você perde 4 HP.
```

## Desafio
No jogo criado na atividade 11, adicionar as seguintes funcionalidades:
1. Sistema de Crítico
   Adicione uma chance de 10% de dar o dobro de dano.
2. Itens Especiais
   Use números para escolher itens como "Poção de Força" (aumenta ataque por 2 turnos).
   Use a criatividade para criar pelo menos 4 itens
3. Dois jogadores:
   Adicione ao menu a opção de multiplayer, onde a CPU é substituida por outro jogador.
4. Efeito de status, onde cada status só pode ser usado uma vez por partida:

   4.1 "Buffer Overflow"
       Assim como um buffer overflow sobrecarrega a memória, esse efeito sobrecarrega a saúde do personagem

      - Efeito: A cada turno, o personagem sofre dano equivalente a 5% do seu HP máximo
     
   4.2 "Loop Infinito"
       Assim como um loop infinito paralisa um programa
      - Efeito: O alvo perde a vez por 1 turno enquanto "reinicia o sistema"
      
   4.3 "Tela Azul"
       Assim como a "tela azul" deixa o sistema vulnerável.
      - Reduz a defesa para 0 por 2 turnos
      
   4.4 "Cache Hit"
      - Recupera 30% do HP máximo. Só pode ser usado quando HP está abaixo de 25%. 

# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random
from time import sleep

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
	def __init__(self, word):
		self.word = word
		self.right_letters = []
		self.wrong_letters = []
		self.hidden_word = '_' * len(word)

	# Método para adivinhar a letra
	def guess(self, letter):
		if letter in self.wrong_letters or letter in self.right_letters:
			print("This letter has already been chosen")
			sleep(2)
		else:
			if letter in self.word:
				self.right_letters.append(letter)
				hdd_word = ''
				for i, l in enumerate(self.word):
					if l == letter:
						hdd_word += letter
					else:
						if self.hidden_word[i] != "_":
							hdd_word += self.hidden_word[i]
						else:
							hdd_word += "_"
				self.hidden_word = hdd_word
				print(self.hidden_word)
			else:
				self.wrong_letters.append(letter)
				print("Wrong word")

	# Método para verificar se o jogo terminou
	def hangman_over(self):
		if self.wrong_letters == 6:
			return True
		else:
			return False
		
	# Método para verificar se o jogador venceu
	def hangman_won(self):
		if self.hidden_word == self.word:
			return True
		else:
			return False

	# Método para não mostrar a letra no board
	def hide_word(self):
		return self.hidden_word
		
	# Método para checar o status do game e imprimir o board na tela
	def print_game_status(self):
		print(board[len(self.wrong_letters)])
		print(f"\nWord: {self.hidden_word}\n")
		print(f"Wrong letters: {self.wrong_letters}")
		print(f"Right letters: {self.right_letters}")

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
        with open("palavras.txt", "rt") as f:
                bank = f.readlines()
        return bank[random.randint(0,len(bank))].strip()


# Função Main - Execução do Programa
def main():

	# Objeto
	game = Hangman(rand_word())
	# Verifica o status do jogo
	game.print_game_status()

	while True:
		if game.hidden_word == game.word:
			break
		elif len(game.wrong_letters) >= 6:
			break

		letter = ''
		while True:
			letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
					   'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
			letter = input("Letter: ").upper()

			if letter in letters:
				break
			else:
				print("Error!!")
				continue

		game.guess(letter.lower())
		game.print_game_status()

	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter


	# De acordo com o status, imprime mensagem na tela para o usuário
	if game.hangman_won():
		print ('\nParabéns! Você venceu!!')
	else:
		print ('\nGame over! Você perdeu.')
		print ('A palavra era ' + game.word)
		
	print ('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa		
if __name__ == "__main__":
	main()

import os
import random


def schon():
    pass # Aquí va el hangman chido


def interfaz(word, underscores, vidas):
    characters_of_word = [letter for letter in word]
    characters_of_word = "".join(characters_of_word)
    print(characters_of_word)
    while vidas > 0:
        print(underscores)
        print(f'Vidas: {vidas}')
        eleccion = input('Type a letter: ')
        i = 0
        for letter in word:
            if eleccion == characters_of_word[i]:
                underscores[i] = eleccion
                vidas += 1
            i += 1
        vidas -= 1
        os.system('cls')
    print('Game over.')



def worter(): #get a random word from the database
    words = []
    with open('./words.txt', 'r', encoding='utf-8') as f:
        for name in f:
            words.append(name)
        
        random_number = random.randint(0, 203)
        word = words[random_number]
        word = word.replace('\n', '')
        underscores = [' _ ' for i in word]
        #underscores = "".join(underscores)
        vidas = 5
        interfaz(word, underscores, vidas)


def run():
    print('Guess the word: ')
    worter()    


if __name__ == '__main__':
    run()
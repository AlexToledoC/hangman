import os
import random


def interfaz(word, underscores, vidas, lenght):
    while vidas > 0:
        for i in underscores:
            print(i, end=' ')
        print(f'\nVidas: {vidas}')
        eleccion = input('Type a letter: ')
        i = 0
        for letter in word:
            if eleccion == word[i]:
                underscores[i] = eleccion
                lenght += 1
                vidas += 1
            i += 1
        vidas -= 1
        os.system('cls')
        if lenght == len(word):
            underscores = "".join(underscores)
            print(underscores)
            print('Congratulations!')
            print('You´ve guessed the word')
            break
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
        vidas = 5
        lenght = 0
        interfaz(word, underscores, vidas, lenght)


def run():
    print('Guess the word: ')
    worter()    


if __name__ == '__main__':
    run()
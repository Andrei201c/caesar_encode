import random
import word_list
import ascii_figure

complete = False
lifes = 3
word = random.choice(word_list.words)
word_lenght = len(word)
# print(word) #for see the  word, like a hint

display = []
for _ in range(word_lenght):
    display += "_"

print("***** HANGMAN GAME *****")
guess = input("Enter a letter").lower()

end_of_game = False

while not end_of_game:
    if guess not in word:
        lifes -= 1

    for num in range(word_lenght):
        letter = word[num]
        if letter == guess:
            display[num] = letter

    if lifes == 3:
        print(ascii_figure.ascii_figure[0])
    elif lifes == 2:
        print(ascii_figure.ascii_figure[1])
    elif lifes == 1:
        print(ascii_figure.ascii_figure[2])
    elif lifes == 0:
        print(ascii_figure.ascii_figure[3])
        print("                 ** IDIOT YOU LOST THE GAME              **")

    if "_" not in display:
        end_of_game = True
        print("YOU WIN")

    if lifes == 0:
        end_of_game = True

    strWord = "".join(display)

    print(strWord)
    guess = input()

print(word)

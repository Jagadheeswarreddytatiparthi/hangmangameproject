import random
word_list=["apple","mango","potato"]
lives=6
print("you have only 6 lives so try to guess the word within 6 attempts!Good luck!!")
chosen_word=random.choice(word_list)
display=[]
for words in chosen_word:
    display+='-'
game_over=False
while not game_over:
     guessed_letter=input("Guess a letter:").lower()
     for position in range(len(chosen_word)):
         letter = chosen_word[position]
         if letter==guessed_letter:
             display[position]= guessed_letter
     print(display)
            
     if guessed_letter not in chosen_word:
        lives-=1
        if lives ==0:
            game_over=True
            print("you lose!")
     if "-" not in display:
        game_over=True
        print("you win!")
     
       
   

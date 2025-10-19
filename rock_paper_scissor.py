import random
def get_winner(player_choise,com_choi):
   if player_choise == com_choi:
      return "it is a tie"
   elif (player_choise =="rock" and com_choi == "scissor") or (player_choise == "paper" and com_choi =="rock") or (player_choise == "scissor" and com_choi =="paper"):
      return "player"
   return "computer"
print(' hello to rock-paper-scissor I hope you injoy  ')
print(' choose one of these choises \n  1- rock \n 2- paper \n 3- scissor')
while True:
 player_choise = int(input(' enter a number from  1 to 3 : '))

 if player_choise == 1:
    player_choise = 'rock'
 elif player_choise == 2:
    player_choise = 'paper'
 else:
    player_choise = 'scissor'
 print('your choice is : ', player_choise)
 print('now it is the computer turn ')
 com_choi = random.randint(1, 3)
 if com_choi == 1:
    com_choi = 'rock'
 elif com_choi == 2:
    com_choi = 'paper'
 else:
    com_choi = 'scissor'

 print(' the computer chooses : ', com_choi)
 winner = get_winner(player_choise,com_choi)
 if winner == "it is a tie":
    print('it is a tie')
 elif winner == "player":
    print('you won ')
 elif winner == 'computer':
    print('you lose')



 again = input(' you want to play again ?(yes or no) ').strip().lower()
 if again == "no":     
    print('goodbye')
    break

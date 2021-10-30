n = 18
no_guess = 1
print('Limited guess upto 9')
while (no_guess <= 9):
    g_no = int(input('guess no. : \n'))
    if g_no<18:
        print('no. enter is less try again \n')
    elif g_no>18:
        print('no. enter is greater try again \n')
    else:
        print('u won\n')
        print(no_guess,"guesses took to finish")
        break
    print(9 - no_guess,'guesses left')
    no_guess = no_guess + 1
if(no_guess>9):
    print('game over')  

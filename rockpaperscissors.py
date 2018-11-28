while True:
    a = input('Player 1 choice: ').lower()
    b = input('Player 2 choice: ').lower()

    if((a=='rock'and b=='scissors')or(a=='scissors' and b=='paper')or(a=='paper' and b=='rock')):
        print('Player 1 wins!')
    
    elif((a=='rock'and b=='paper')or(a=='scissors'and b=='rock')or(a=='paper'and b=='scissors')):
        print('Player 2 wins!')
    
    elif((a=='rock' and b=='rock')or (a=='scissors' and b=='scissors')or(a=='paper'and b=='paper')):
        print('It is a tie!')
        
    check = input('Type yes if you want to play again: ').lower()
    if (check) == 'yes':
        continue
    else:
        break
def game(mini = 0, maxi = 100):
    message = 'Enter H to indicate the guess is too high. Enter L to indicate the guess is too low. Enter G to indicate I guessed correctly.'
    print 'Please, think of a number between ' + str(mini) + ' and ' + str(maxi)  + message

    answer = (mini + maxi) / 2
    question = ''

    while 1:
        question = raw_input('Your secret number is ' + str(answer) + '? Please, to continue, enter H, L or G: ')
        if question == 'G':
            return ('I win')
        elif question == 'H':
            maxi = answer
        elif question == 'L':
            mini = answer
        else:
            print message
        answer = mini +(maxi - mini) / 2
        if answer == maxi - 1:
            maxi = maxi + 1

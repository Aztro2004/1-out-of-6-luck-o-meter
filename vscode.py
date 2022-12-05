import matplotlib.pyplot as plt
import random
right_i = 0
wrong_i = 0
results =[0]
x_i =0
x =[0]
print('\n',"Instructive: ",'\n',"1.-Guess a number between 1 and 6, the amount of times you want",'\n',"2.-A graph will appear when you type and enter: PRINT",'\n',"4.-To restart all type: RESTART",'\n',"5.-After printing the graph, close its window to continue the program",'\n',"6.-To break after trying the amount of times you want type: EXIT",'\n',)
while True:
    num_al = random.randint(1,6)
    num_us = input("number between 1 and 6 OR command: ")
    print('\n')
    if num_us.isdigit():
        num_us = int(num_us)
        if num_us == num_al:
            right_i += 1
            print("You guessed right!")
        else:
            wrong_i+=1
        x_i+=1
        results.append(right_i/x_i)
        x.append(x_i)
    elif num_us == 'PRINT':
        plt.plot(x,results)
        plt.axhline(0.16, color='r',label ='Avg.Luck')
        plt.legend(loc ="lower right")
        plt.ylabel("Luck")
        plt.xlabel("Num of tries")
        plt.title("Your 1 out of 6 luck-o-meter")
        plt.grid()
        plt.show()
        print("|right:",right_i,"|wrong:",wrong_i,"|# of tries:",x_i,"|")
    elif num_us == 'EXIT':
        print("|right:",right_i,"|wrong:",wrong_i,"|# of tries:",x_i,"|")
        print("Exiting...")
        break
    elif num_us == 'RESTART':
        print("Program restarted",'\n')
        x_i =0
        right_i=0
        wrong_i =0
        x.clear()
        results.clear()
    else:
        print("command not recognized")
# 1 out of 6 luck-o-meter

A program that measures your luck. The program creates a random number between 1 and 6, and you have to guess it, if you guessed right the program will tell you and will save a value that saves the chance of that guess happening according to the number of tries. The program has 4 main inputs or commands:
1. Num. between 1 and 6: your guess of the number between 1 and 6 the computer generates.
2. 'PRINT': Displays a graph of your luck with each try up to the point you type the command.
3. 'RESTART': Resets the program and all your previous data.
4. 'EXIT': Ends the program.

## How your luck is calculated
With each right guess you get it will get taken into account with the number of tries up to that point. the general formula is:
- num of right guesses / num of tries. 

## How the graph is made
The results of the previous operation is positioned against the number of tries, to see the increase or decrease of your luck across the span of your tries.

Here are some examples of the graph the program will give:
graph1
<img width="1252" alt="Screen Shot 2022-12-04 at 16 40 30" src="https://user-images.githubusercontent.com/111297109/205519862-e45a8776-cd3a-4afe-88bc-809d996d626c.png">

graph2
<img width="1237" alt="Screen Shot 2022-12-04 at 16 37 47" src="https://user-images.githubusercontent.com/111297109/205522272-05d00374-b7e5-418c-9365-102912ef924c.png">

## Dependencies
- [MatPlotlib](https://matplotlib.org/)

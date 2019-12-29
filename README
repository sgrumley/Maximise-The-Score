# Maximise The Score

Maximise The score is an assignment from the course Computing Algorithms

## Problem Description

>- In this game there are n values on a table each with a value written on it
>- Starting with a coin toss to determine who goes first
>- Each round the player is allowed to take max k turns
>- In each turn the player (Scott or Rusty) will choose a value with the hope of ending on the larger score
>- Player Rusty will choose the highest summed value e.g. he 19 over 21 since the sum of the values is greater 10 (1+9) > 3 (2+1)
>- Player Scott will simply choose the largest value


## Input Format
First line contains an integer T, denoting the number of test-cases.

Next 3T lines contain the test-cases
First line contains two integers n and k, representing the number of balls present on the table and the
maximum number of turns allowed per round.

Second line contains n space separated integers (a1, a2, ... an). Here, ai indicates the score written on ith ball.

Third line contains result of the toss. Here, "HEADS" indicates Scott starts the game, while "TAILS"
indicates Rusty starts the game.


```
2
3 2
1000 99 98
TAILS
2 1
5 6
HEADS
```
## Output Format
Points scored by Scott and Rusty

```
1000 197
6 5
```

## Design
A priority queue is used with each element a tuple containing Scotts value and rustys value (12, 3) each turn the player starts their turn the queue will heapify based on which player is currently choosing.

Based off the worst case situation which is Rusty getting all the turns, the program will run at O(n^2 - 1logn)

## How To Run
Use python 3 to run the main.py

The program will run from input.txt

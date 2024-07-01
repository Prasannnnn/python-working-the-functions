'''
Game Rules
Both players are given the same string.
Stuart makes words starting with consonants.
Kevin makes words starting with vowels.
The game ends when all possible substrings have been made.
Scoring
A player gets +1 point for each occurrence of their substring in the string.
For example, with the string “BANANA”:
Kevin’s vowel beginning word “ANA” occurs twice in “BANANA”, so Kevin gets 2 points.
Function Description
You need to complete the minion_game function which takes a string as input and prints the winner’s name and score, or “Draw” if there is no winner.

Sample Input
BANANA

Sample Output
Stuart 12

Solution Approach
Here’s a simple Python function to determine the winner:
'''
def minion_game(string):
    # your code goes here
    kevin_score = 0
    stuart_score = 0
    length = len(string)
    
    for i in range(length):
        if string[i] in 'AEIOU':
            kevin_score += (length - i)
        else:
            stuart_score += (length - i)
            
    if kevin_score > stuart_score:
        print("Kevin",kevin_score)
    elif stuart_score > kevin_score:
        print("Stuart",stuart_score)
    else:
        print("Draw") 

if __name__ == '__main__':
    s = input()
    minion_game(s)

'''
This function calculates the scores for both players based on the starting letter of each substring and determines the winner
'''
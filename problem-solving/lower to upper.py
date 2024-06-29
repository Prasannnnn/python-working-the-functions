'''
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2  
Function Description

Complete the swap_case function in the editor below.

swap_case has the following parameters:

string s: the string to modify
Returns

string: the modified string
Input Format

A single line containing a string .

Constraints


Sample Input 0

HackerRank.com presents "Pythonist 2".
Sample Output 0

hACKERrANK.COM PRESENTS "pYTHONIST 2".

'''
def swap_case(word):
    swap_word=""
    for letter in word:
        if letter.islower():
            swap_word+= letter.upper()
        elif letter.isupper():
            swap_word+=letter.lower()
        else:
             swap_word += letter

    return swap_word 

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
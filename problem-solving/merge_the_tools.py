'''
Problem Explanation
Input:
A string s of length n.
An integer k, where k is a factor of n.
Process:
Split the string s into n/k substrings, each of length k.
For each substring, create a new string by removing duplicate characters while maintaining the order of their 
first occurrence.
Output:
Print each processed substring on a new line.
Example
Given the string AABCAAADA and k = 3:

Substrings: AAB, CAA, ADA
Processed substrings: AB, CA, AD
Function Description
You need to complete the merge_the_tools function which takes a string s and an integer k as input and 
prints the processed substrings.

Sample Input
AABCAAADA
3

Sample Output
AB
CA
AD

Solution Approach
Here’s a Python function to solve this problem:
'''

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        substring = string[i:i+k]
        unique_chars = []
        for char in substring:
            if char not in unique_chars:
                unique_chars.append(char)
        print(''.join(unique_chars))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
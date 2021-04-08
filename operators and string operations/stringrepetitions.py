#Given a word and a number (N), program to print the last three characters of the word N times in a single line

word = input()
N = int(input())
print(word[-3:]*N)

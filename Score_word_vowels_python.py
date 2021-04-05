'''  The score of a single word is 2 if the word contains an even number of vowels. 
    Otherwise, the score of this word is 1. 
    The score for the whole list of words is the sum of scores of all words in the list
'''
def score_words(words):
    vow=["a","e","i","o","u"]
    vow_cnt=0
    total=0
    for word in words:
        for i in range(len(word)):
            if word[i] in vow:
                vow_cnt+=1
        if vow_cnt%2==0:
            total+=2
        else:
            total+=1
        vow_cnt=0
    return total

n = int(input("Enter number of words: "))
words = input("Enter the word: ").split()
print("The score is: ")
print(score_words(words))
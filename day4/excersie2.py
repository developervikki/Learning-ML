sentence=input("Enter a sentence: ")


#split the sentene in the word


words=sentence.split()



#initialize the dictionary

word_count={}


#count word frequence

for word in words:
    word=word.lower()
    if word in word_count:
        
        word_count[words]+=1
        
    else:
        word_count[word]=1
        
print(word_count)
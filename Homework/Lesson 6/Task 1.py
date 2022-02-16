string = input("Please enter any String : ")
words = []

words = string.split()
frequency = [words.count(i) for i in words]

dict_1 = dict(zip(words, frequency))
print("Dictionary Items  :  ",  dict_1)
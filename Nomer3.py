words = {"банан": "banana", "яблоко": "apple", "и": "and"}
stroka = input("Введите строчку: ")

a = [i for i in stroka.split(' ')]

for j in range(len(a)):
    if a[j] in words:
        print(words[a[j]], end = " ")
    else:
        print(a[j], end = " ")
        

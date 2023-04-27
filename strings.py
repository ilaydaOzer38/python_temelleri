name = 'İlayda'
surname = 'Kandemir'
age= 27

greeting = 'My name is ' + name + ' ' + surname + ' and \nI am ' + str(age) + ' years old'
length = len(greeting)

#print(greeting)
print(greeting[0])
print(greeting[3])
print(len(greeting))  #greeting içindeki kaç karakter olduğunu öğrenmek için kullanılan metot
print(greeting[length-1]) #sondan bir önceki karakteri bulmak için
print(greeting[-2])#sondan bir önceki karakteri bulmak için

print(greeting[3:7]) #3den başla 7. indeksine kadar
print(greeting[:10]) #baştan başla 10. indeksine kadar git
print(greeting[2:42:2]) #2den başla 42. indeksine kadar 2şer 2şer git

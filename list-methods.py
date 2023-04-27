numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a','g','s','b','y','a','s']

val = min(numbers)
val = max(numbers)
val = max(letters)
val = min(letters)

val = numbers[3:6]
val = numbers[:3]
val = numbers[4:]

numbers[4] = 40 

numbers.append(50)  #append metodu dizinin en sonuna 50 sayısını eklemek için kullanılır.
numbers.append(60)
numbers.insert(3, 80)   #insert metodu ile 3.indeksten sonra 80 sayısını ekler.
numbers.insert(-1,51)   #en sondan bir önceki indekse 51 sayısını ekler.

# numbers.pop()  # listenin en sondaki dizideki sayıyı siler
# numbers.pop(0)  #listenin 0. indeksindeki sayıyı siler.
numbers.remove(10)  #remove metodu ile silmek istediğimiz karakteri girip listede onu bulup silmesini sağlar.

numbers.sort  #sayıları küçükten büyüğe doğru sıralar.
numbers.reverse() #diziyi tam tersi çevirir.
letters.sort #harfleri alfabetik sıraya göre sıralar.
letters.reverse() #diziyi tam tersi çevirir.

print(len(numbers))
print(len(letters))

print(numbers.count(10))  #dizide kaç tane 10 oldugunu verir.
numbers.clear()  #numbers dizisini temizler.
print(numbers)

print(numbers)
print(val)

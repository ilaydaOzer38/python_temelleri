maasAli=5000
maasAhmet=4000
vergi=0.27


print(maasAli-(maasAli*vergi))
print(maasAhmet-(maasAhmet*vergi))

#Değişken Tanımlama Kuralları

# rakam ile başlayamaz

number1 = 10
print(number1)
number1 = 20
print(number1)

number1 += 30
print(number1)

# Büyük Küçük harf duyarlılığı vardır

age = 20 
Age = 30
print(age)
print(Age)

#Türkçe karakter kullanmayalım

yas = 20
_age = 20

x=1                     #int
y=2.3                   #float
name = "Çınar"          #string
isStudent = True        #bool

#4 satırlık kodu aşağıdaki gibi tek satır haline getirilmiştir
x, y, name, isStudent = (1, 2.3 , "Çınar", True ) 

a='10'
b='20'
print(a+b)   #30  0 => 1020


firstName = 'ilayda'
lastName = "yakup"
print(firstName + lastName) # ilayda yakup
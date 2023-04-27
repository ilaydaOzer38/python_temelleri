"""
1- Bir müşterinin aşağıdaki bilgileri için değişken oluşturunuz.
Müşteri adı
Müşteri soyadı
Müşteri adı+soyadı
Müşteri cinsiyet
Müşteri tc kimlik
Müşteri doğum yılı 
Müşteri adres bilgisi
Müşteri yaşı
"""

customerName = 'ali'
customerSurname = 'yılmaz'
customerNameSurname = customerName + ' ' + customerSurname
customerGender = True # Erkek
customerTc = '14789652325'
customerBirthdayYear = '1995'
customerAddress = 'İstanbul Kadıköy'
customerAge = 2019 - customerBirthdayYear

"""
2- Aşağıdaki siparişlerin toplam bilgisini hesaplayınız.

Sipariş 1 => 110 TL
Sipariş 2 => 1100.5 TL
Sipariş 3 => 356,95 TL

"""
order1 = 110
order2 = 1100.5
order3 = 356,95

total = order1 + order2 + order3
print('Total:', total)
# key - value

# 41 => kocaeli 34 => istanbul

# sehirler = ['kocaeli','istanbul']
# plakalar = [41, 34]

# print(plakalar[sehirler.index('kocaeli')])
# print(plakalar[sehirler.index('istanbul')])

# plakalar = {'kocaeli' : 41, 'istanbul' : 34 }

# print(plakalar['kocaeli'])
# print(plakalar['istanbul'])

# plakalar['ankara'] = 6
# plakalar['kocaeli'] = 'new value'

# print(plakalar)

users = {
    'ilaydaözer' : {
    'age':27,
    'roles' : ['user'],
    'email':'ilayda@gmail.com',
    'address' : 'tekirdağ',
    'phone' : '1235956'
    },
    'yakupözer' : {
    'age':26,
    'roles' : ['admin','user'],
    'email':'yakup@gmail.com',
    'address' : 'tekirdağ',
    'phone' : '255952586'
    }
}

print(users['ilaydaözer']['age'])
print(users['yakupözer'])
print(users['yakupözer']['roles'][0])

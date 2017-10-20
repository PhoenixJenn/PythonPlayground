myCat = {'size':'fat', 'color':'orange', 'disposition':'angry'}

print(myCat['size'])

#unordereds


bln = 'name' in myCat
print(bln)


k = list(myCat.keys())
#.items(), .items()
print(k)

if 'age' not in myCat:
    myCat['age'] = 1

#makes sure it doesnt' exist first
myCat.setdefault('size','small')
myCat.setdefault('weight','12')


for v in myCat.values():
    print(v)

for k, v in myCat.items():
    print(k,v)

for i in myCat.items():
    print(i)


if 'color' in myCat:
    print(myCat['color'])

p = myCat.get('age',0)
print(p)

p = myCat.get('color','')
print(p)
#get colorz or return blank string
p = myCat.get('colorz','')
print(p)





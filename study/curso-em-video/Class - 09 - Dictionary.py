"""
Obs; Dict in Python is named map too
Dict are colection for type key/value

dict1={}

dict2=['pt':'Portugal','USA':'United States']

dict3={'age':20,'name':'Jo'}

You can use this, but it´s not recomended
dict4={one=1,two=2,three=3}
print(dict4[one])

You can use get
dict3.get('pt')
dict3.get('ru') -> None error
value = dict3.get('get this value on there','if you not find, use this value')
value = dict3.get('ru','Doesnt exist')
print(value)

print('pt' in dict2)
print('usa' in dict2)
print('ru' in dict2)

Tuples are common use as key in dict
dict4 = {
    (35.2435, 39235): Tokyo Oficce,
    (39.1923, 10395): New York Office
}

adding data 

dict5 = {'jan':100,'feb':120,'mar':300}
More common
dict5['apr']=350
Other way
new_data={'may':500}
dict5.update(new_data) -> dict5.update({'may':500})

updating data

one way
dict5['may'] = 550
other way
dict5.update({'may':550})

Obs: YOU CAN'T REPEAT A KEY

In pop we need to give the key, if not find it returns a KeyError
dict5.pop('may')

If you delet a key with pop, it always returns the value associated

del dict5['feb']

Doesnt return the value

dict5.clear()
It cleans a dict

deep copy
new = dict5.copy()
shallow copy
new2 = dict5

non usual way
other = {}.fromkeys('a','b')
other = {}.fromkeys(['name','point','email','profile'],'unknom')
fromkyes method receive two parameters, one interable and one value
it will generate for each interable one key, and will give to the key a value
entered
other = {}.fromkeys(range(1,11),'b')

"""

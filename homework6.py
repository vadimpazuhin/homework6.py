my_dict = {'Mark': 2004,'Veta': 2008,'Vilina': 2012}
print(my_dict)
print('Existing value:',my_dict['Mark'])
print(my_dict.get('Kira','Not existing value:None'))
my_dict.update({'Kira': 2019,'Vadim': 2011})
print('Deleted value:',my_dict.pop('Mark'))
print('Modified dictionary:', my_dict)

mu_set = {0,1,1,23,"dom",1.66,23}
print('Set:',mu_set)
mu_set.add(15)
mu_set.add((16,17))
mu_set.discard(1.66)
print('Modified set:',mu_set)
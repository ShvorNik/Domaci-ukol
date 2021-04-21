# 1. На склад поступил новый товар. Надо пересмотреть склад и исправить ошибки, сделать первую товара букву заглавной.
# Все типы товаров должны быть неизменяемыми, чтобы кто-то случайно не перепутал их снова.
# В овощи забыли добавить капусту. Цифра в категории - это цена товара этого типа.
# 2. Для удобства хранения, нужно объединить все товары в один объект, при этом сохранить структуру типов.
# 3. На складе закончились морковка и арбузы. Надо перенести их в категорию "finished".
# 4. Если название продукта длиннее 6 символов, нужно отображать только первые 6.

fruit = ('apple', 'pear', 'cherry', 'banana', 12)
vegetables = ['tomato', 'onion', 'carrot', 17]
berries = ('blueberry', 'cranberry', 'watermelon', 8)
# работа с фруктами
fruit = list(fruit)
new_fru = []
for s in fruit[0:-1]:
    new_fru.append(s[0:6].capitalize())
# ^промежуточный список с обрезанными фруктами с заглавными буквами^
fruit[0:-1] = new_fru
print('список фруктов:', fruit)
# работа с овощами
vegetables.insert(-1, 'cabbage')
new_veg = []
for s in vegetables[0:-1]:
    new_veg.append(s[0:6].capitalize())
# ^промежуточный список с обрезанными овощами с заглавными буквами^
vegetables[0:-1] = new_veg
print('список овощей:', vegetables)
# работа с ягодами
berries = list(berries)
new_ber = []
for s in berries[0:-1]:
    new_ber.append(s[0:6].capitalize())
# ^промежуточный список с обрезанными ягодами с заглавными буквами^
berries[0:-1] = new_ber
print('список ягод:', berries)
#
storage = {'fruit': fruit, 'vegetables': vegetables, 'berries': berries}
print('весь список:', storage)
finished = (vegetables[2], berries[-2])
del vegetables[2], berries[-2]

# преобразование в картежи
fruit, vegetables, berries = tuple(fruit), tuple(vegetables), tuple(berries)

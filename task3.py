# Напишите программу, которая получает на вход строку и подсчитывает, 
# сколько раз в ней встречается каждый символ (независимо от регистра).
# Результат нужно вывести без фигурных скобок
# Пример. 
# ввод:
# Абракадабра
# Вывод
# а-5 б-2 д-1 к-1 р-2
bukvi=input()
proverki={}
for i in range(len(bukvi)):
    if bukvi[i] in proverki:
        proverki[bukvi[i]]+=1
    else:
        proverki[bukvi[i]]=1
print(proverki) 

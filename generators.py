numbers = {1, 2, 3, 4, 5, 6, 7, 8, 100}
result = []
for number in numbers:
    if number > 5 :
        result.append(1)
    if number < 5 :
        result.append(0)
print(result)
result = filter(lambda number:number > 5 and number < 50, numbers)
print(list(result))


numbers = [2,8,7,3,12,120,4521]
result1 =  [numbers for numbers in numbers if numbers > 5 and numbers < 50]
print(result)

names = ['leo','mag','kat','max']
names1 = []
for i in names:
    if 'm' in i[0]:
        names1.append(i)
print(names1)


resuly02 = {i:i**2 for i in range(1,10)}
print(resuly02)
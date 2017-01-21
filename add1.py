lst_nums = list()

while (True):
    number = input('enter a number to calculate or type done: ')
    if number == 'done': break
    value = float(number)
    lst_nums.append(value)
   


print(lst_nums)
print('maximum: ', max(lst_nums))
print('minimum: ', min(lst_nums))
print('total: ', sum(lst_nums))
print('average: ', sum(lst_nums)/len(lst_nums))

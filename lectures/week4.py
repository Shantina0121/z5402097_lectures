test_lis = [0,1,2,3,4,5,6,7,8,9,10,20,22,23,25,29,30,31]
def is_even_num(lis):
    evennum = []
    for n in lis:
        if n % 2 == 0:
            evennum.append(n)
    return evennum
is_even_num(test_lis)

lst = [2,3,12,14,20,21,25,13,15]
new_lst = [x**2 for x in lst if x**2>150]
print(f'the new list with value of square greater than 150 is {new_lst}')

hours = input('Enter number of hours you worked this week: ')
#Python 3 output numeric value as a string in input () function
hours = int(hours)
normal_rate = 51.45
overload_rate = 88.9
if hours > 35 :
    pay = (35 * normal_rate) + ((hours - 35) * overload_rate)
else :
    pay = hours * normal_rate
print(f'This weekly payment is: {pay}')



numbers = [3,9,1,5,7,2,11,0,3,12,3,15]
temp_largest = None
print('Before', temp_largest)
for number in numbers:
    if temp_largest is None:
        temp_largest = number
    elif number > temp_largest:
        temp_largest = number
print(number, temp_largest)
print(f'The largest value is {temp_largest}')

largest = max(numbers)
print(f'The largest value is {largest}')



for i in range(1,4):
    for j in range(1,4):
        if i<=j:
            print(i,j)

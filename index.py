names = ['John', 'Bob', 'Bill']
print(type(names), names)
# str.startwith(), str.endwith(), str.upper(), str.lower(),
joining = ','.join(names)
print(type(joining), joining)

replacing = joining.replace('Bob', 'Bobby')
print(type(joining), joining)

splitting = joining.split(',')
print(type(splitting), splitting)

print(abs(-12.5)) #min, max, sum



# person = {
#     'name': 'bob',
#     'age': 25
# }
# print('hi {human[name]}, Im  {human[age]}'.format(human=person))

# x = 25
# y = 5
# x,y = y,x
# print(str(x) + '   ' + str(y))

# name = 'Bob'
# age = 25
#
# print('hi %s im %d\n this%s' % (name, age))


# list = [34, 54]
#
# print(list[0])
#
# dictionary = {
#     'key1': 25,
#     'm': [34, 54]
# }
# print(dictionary['key1'])



# file = open('text.txt', 'r')
#
# innerText = file.read()
#
# print(len(innerText))
#
# file.close()


# file = open('text.txt', 'r')
#
# arr = file.readlines()
#
# print(arr)
# print(arr[0])
#
# file.close()

# def divide(num):
#     try:
#         assert num != 0, 'number must be != 0'
#         print(str(10/num))
#     except AssertionError:
#         print('zero')
#         pass
#
# divide(0)

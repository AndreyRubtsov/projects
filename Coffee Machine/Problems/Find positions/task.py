list = input('')
list = list.split(' ')
new = []
for i in list:
    new.append(int(i))
num = int(input(''))
if num in new:
    out = ''
    for i in range(len(new)):
        if num == new[i]:
            out += str(i) + ' '
    print(out)
else:
    print('not found')

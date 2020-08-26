my_time=630
my_t=input()
if my_t=='0':
    print('Tuesday')
if my_t[0]=='-':
    i=int(my_t[1:])
    res=my_time-i*60
    if res<0:
        print('Monday')
    else:
        print('Tuesday')
elif my_t[0]=='+':
    i = int(my_t[1:])
    res = my_time + i * 60
    if res > 1440:
        print('Wednesday')
    else:
        print('Tuesday')
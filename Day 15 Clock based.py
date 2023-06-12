#Time based nested loop problem
import time
def abc(a,b,c):
    if(c<30):
        print(30-c,'minutes remaining to',b,': 30')
    elif(c>30):
        print(60-c,'minutes remaining to',b+1,':00')
a = time.strftime('%H:%M:%S')
print('Current time',a)
b = int(time.strftime('%H'))
c = int(time.strftime('%M'))
# Morning
if(b>=4 and b<12):
    print("Good morning")
    abc(a,b,c)
# Afternoon
elif(b>=12 and b<16):
    print('Good afternoon')
    abc(a,b,c)
# Evening
elif(b>=16 and b<20):
    print('Good Evening')
    abc(a,b,c)
# Night
else:
    print('Good night')
    abc(a,b,c)
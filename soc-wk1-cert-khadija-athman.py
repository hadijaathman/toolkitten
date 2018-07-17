print(1+2)
print(5*(4*3)*4)
print(1<<9)
print(2%4)
print(2**8)
print( 24*7)
print(24*365)
print(60*24)
print(60*(365*10))
print(24*365)
print(8760*8030)
print(60*(8760*8030))
print(60*(60*(8760*8030)))
#my age in seconds	
print(365*8640)
#converting age in seconds to years	
print(48618000 /3153600)
#days to time overflow
print(20*356)
#calculating my exact age
from datetime import datetime, timedelta
age = datetime.now() - datetime.strptime("Sun, 4 fenruary 1996 12:00:32 +0200 ","%a, %d %b %Y %H:%M:%S +0200")
print (age.days)

#working with strings
print('hello,world')
print(' ')
print('goodbye')
print('i like '+ 'apple pie')
print('12+12')
print('12'+'12')

print('you\'re swelling!')

#back slashes
my_string = 'you can say that again'
print(my_string)

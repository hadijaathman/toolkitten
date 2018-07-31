import string
for i in range(65, 65+26):
    print(i, "stand for ",chr(i))

print((string.ascii_lowercase))
print((string.ascii_uppercase))

input = input('Write Text: ')
input = input.lower()
output = []
for character in input:
    number = ord(character) 
    output.append(number)
print(output)

m= 'land'
o= 'water'
world = [[o,o,o,o,o,o,o,o,o,o,o],
[o,o,o,o,m,m,o,o,o,o,o],
[o,o,o,o,o,o,o,o,m,m,o],
[o,o,o,m,o,o,o,o,o,m,o],
[o,o,o,m,o,m,m,o,o,o,o],
[o,o,o,o,m,m,m,m,o,o,o],
[o,o,o,m,m,m,m,m,m,m,o],
[o,o,o,m,m,o,m,m,m,o,o],
[o,o,o,o,o,o,m,m,o,o,o],
[o,m,o,o,o,m,o,o,o,o,o],
[o,o,o,o,o,o,o,o,o,o,o]]

def continent_counter(world, x, y):
    if world[x][y]!='land':
        return 1

    size =1 
    world[x][y]= 'counted land'

    size = size + continent_counter(world,x-1,y-1)
    size = size + continent_counter(world,x,y-1)
    size = size + continent_counter(world,x+1,y-1)
    size = size + continent_counter(world,x-1,y)
    size = size + continent_counter(world,x+1,y)
    size = size + continent_counter(world,x-1,y+1)
    size = size + continent_counter(world,x,y+1)
    size = size + continent_counter(world,x-1,y+1)
    return size
    
print(continent_counter(world,5,5))





#.......wk2 day 3 things to try

my_dict = {
    "a": 35000,
    "b":8000,
    "z":450
}
print(my_dict)
print(my_dict["a"])
my_dict["rocio"]="pretty"
print(my_dict["rocio"])
print(my_dict)

my_dict["a"]=56
print(my_dict["a"])
print(my_dict)

filename = "alice_in_wonderland.txt"
file = open(filename, "r")
raw = file.read()
print('from zero to sixty-five: ' + raw[:100])

print('AGAIN: ' + raw[0:100])
print('the length of alice in wonderland in this text file is: ' +str(len(raw)))

def char_frequency(raw):
    dict =my_dict
    for n in raw:
        keys = dict.keys()
        if n in keys:
            dict[n]+=1
        else:
            dict[n]=1 
    return dict
print(char_frequency(raw))

dictionary={
    "fav":'chocolate',
    "fast":'cheeter',
    "slowest":'snail'
}
print(dictionary)
dictionary["pretty"]='barbie'
print(dictionary)

#............classes.............
class student():
    def __init__(self,name,email,dream):
        self.name = name
        self.email = email
        self.dream = dream

s1 = student("hadija", "athman.hadi@gmail.com","full stack network, web and software engineer.")
print(s1)  
print(s1.name)
print(s1.dream)      

class interactions():
    def __init__(self, fname, lname, dream):
        self.fname = fname
        self.lname = lname
        self.dream = dream
p1 = interactions("hadija","athman","full stack engineer")
p2 = interactions("dija","ath","piloting and commuity empowerment")
p3 = interactions("hadi","man"," engineer")
p4 = interactions("suzan","schinders","programing")
p5 = interactions("molly","nadal"," engineer")
p6 = interactions("tracy","melany","patriot")
print(p1.fname)
print(p2.fname)

class students():
    def __init__(self, first_name,last_name,
    email,country_code,phone_number,country, 
    self_identification):

    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.country_code = country_code
    self.phone_number = phone_number
    self.country = country
    self.self_identification = self_identification



    




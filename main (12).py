#tell method
f =open('s.txt','r')
print('position of blink initially:',f.tell()) # tells current position of blink
a = f.read(8) # read only 8 character 
print(a)
print('position of blink after read:',f.tell())

#seek method
f.seek(8)  #bring blink on 8th position
b = f.read() #read from 8th position
print(b)
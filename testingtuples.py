empty_tuple = ()

time = (23, 45, 0)

hour, minute, second = time

hour, minute, second = minute, hour, second 



print(time, hour)

#Bytes practice

a = bytes([1,2,3,4,124,54])
b= bytes([0,0x40, 0x70,0xa0,0xff])

a = 'ä'.encode('utf8')
b= b'\xc3\xa4'.decode('utf8')



print(a, b)
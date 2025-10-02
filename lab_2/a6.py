n = int(input())

sec = n % 60 
hous = n // 3600
minutes = (n % 3600) // 60

print('{}:{:02}:{:02}'.format(hous, minutes, sec))
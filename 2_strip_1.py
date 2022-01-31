file1 = open("t2.txt", "r")
lines=""
str=""
# считываем все строки
lines = file1.readlines()

# итерация по строкам
for line in lines:
    str=(line.lstrip(', '))
    print(str.rstrip('\n'))
	
# закрываем файл
file1.close
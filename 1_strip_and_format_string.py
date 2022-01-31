file1 = open("1.txt", "r")
lines=""
str=""
str1=""
# считываем все строки
lines = file1.readlines()

# итерация по строкам
for line in lines:
    str = str+(line.strip(",\n"))
	
print(str.replace('}', '}\n'))
# закрываем файл
file1.close
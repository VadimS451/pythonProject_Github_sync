print("                                               ")
print("Cортировка массива (списка) пузырьковым методом")
print("===============================================")
print("                                               ")

SourceList = [54, 55, 2, -4, 2, 89, 104, 33, 20, 1]

print("Исходный список в виде массива: " + str(SourceList))

ListLenth = len(SourceList)
print("Длина списка: " + str(ListLenth))

print("Исходный список в столбец:")
for x in range(0, ListLenth):
    print(SourceList[x])

# поменяем местами первые два элемента списка (специальная конструкция Python swap? кажется)
SourceList[0], SourceList[1] = SourceList[1], SourceList[0]
print("Измененный список вручную - поменяны местами 1й и 2й элементы: " + str(SourceList))


# объявляется функция
def bubble_sorting_function(workinglist):
    print("Будет использовано два цикла: один проходит он начала до конца списка, второй - делает это несколько раз,"
          " чтобы все цифры были проверены")
    print("т.к. позиции идут от нуля до v - цикл учитывающий позицию сравниваемых элементов должен быть меньше "
          "на единицу, иначе цикл переходит в режим out of range")
    print("а ечсли отнять еще и z - то это оптимизация кода за счет того, что после первого прохода по v позициям"
          "последняя цифра уже становится на свою позицию и проходить можно на одну позицию меньше")
    for z in range(0, ListLenth):
        print("z=" + str(z))
        for v in range(0, ListLenth-1-z):
            print("v=" + str(v))
            print(workinglist)
            if workinglist[v] > workinglist[v+1]:
                workinglist[v], workinglist[v+1] = workinglist[v+1], workinglist[v]
                #print(workinglist)
    return workinglist


SortedList = bubble_sorting_function(SourceList).copy()
print("Отсортированный список: ", str(SortedList))

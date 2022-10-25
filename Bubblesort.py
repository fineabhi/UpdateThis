def bubbleesort(list):
    for i in range(len(list) - 1, 0, -1):
        no_swap = True
        for j in range(0, i):
            if list[j + 1] < list[j]:
                list[j], list[j + 1] = list[j + 1], list[j]
                no_swap = False
        if no_swap:
            return
 
 
list = input('Enter the list of numbers: ').split()
list = [int(x) for x in list]
bubbleesort(list)
print('Sorted list: ', end='')
print(list)

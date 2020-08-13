'''Subarray with sum'''

def subarrsum():
    lst = [1,2,3,4,5]
    lst2 = lst.copy()
    num = 10
    leng = len(lst)
    print('The list : ',lst)
    sum = 0
    idfirst = 0
    idlast = 1
    c = None
    initial = lst[0]


    while  c is None and num is not None and num != initial:

        for  i in lst :
            for j in lst[lst.index(i)+1::]:
                idlast += 1
                sum = initial + j
                initial = sum

                if num == sum:
                    print('from the index {0} to {1} is {2}'.format(idfirst,idlast-1,num))
                    c = 1
                    break


                elif idlast == leng:
                    idfirst += 1
                    idlast = idfirst + 1
                    id = lst.index(i)
                    initial = lst[id + 1]
                    sum = 0
                    break


subarrsum()





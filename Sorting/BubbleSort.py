def bubble_sort(elements):
    size=len(elements)

    for i in range(size-1):
        swapped=False
        for j in range(size-1-i):
            if elements[j]>elements[j+1]:
                elements[j],elements[j+1]=elements[j+1],elements[j]
                swapped=True
        if not swapped:
            break

if __name__ == '__main__':
    elements=[2,5,23,34,1,60,32,8]
    bubble_sort(elements)
    print(elements)

def BinarySearch(numbers_list,number_to_find):
    low=0
    high=len(numbers_list)-1

    while(low<=high):
        mid=(low+high)//2
        if(number_to_find==numbers_list[mid]):
            return mid
        elif(number_to_find>numbers_list[mid]):
            low=mid+1
        else:
            high=mid-1
    return -1

def BinarySearchRecursion(numbers_list,number_to_find,low,high):
    mid=(low+high)//2
    if low>high or mid>=len(numbers_list) or mid<0:
        return -1

    if(number_to_find==numbers_list[mid]):
        return mid
    elif(number_to_find>numbers_list[mid]):
        low=mid+1
    else:
        high=mid-1

    return BinarySearchRecursion(numbers_list,number_to_find,low,high)

if __name__ =='__main__':
    numbers_list=[1,4,6,9,10,15,17]
    number_to_find=900
    print((BinarySearch(numbers_list,number_to_find)))
    print((BinarySearchRecursion(numbers_list,number_to_find,0,len(numbers_list))))

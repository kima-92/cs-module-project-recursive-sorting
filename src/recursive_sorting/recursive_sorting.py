
# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # Set index value for the list to the left, and the list to the right
    i = 0   # Current index in arrA
    j = 0   # Current index in arrB

    # set a new list
    list_length = len(arrA) + len(arrB)
    merged_arr = [0] * list_length

    # Set index for the merged_arr, to insert the new values
    x = 0

    # Compare arrA[i] with arrB[j]

    # While i is less than the length of arrA AND j is less than the length of arrB
    while i < len(arrA) and j < len(arrB):
        # if arrA[0] is smaller than arrB[0]
        if arrA[i] < arrB[j]:
            # Set merged_arr[0] as arrA[0]
            merged_arr[x] = arrA[i]

            # Increment index of both arrA and merged_arr
            i += 1      # So we ignore the previous index from now on
            x += 1      # So we can add items to next index

        # else
        else:
            # Set arr[0] as arrB[0]
            merged_arr[x] = arrB[j]

            # Increment index of both arrB and merged_arr
            j += 1      # So we ignore the previous index from now on
            x += 1      # So we can add items to next index

    # Make sure we add whatever items are left in each array
    while i < len(arrA):
        merged_arr[x] = arrA[i]
        
        i += 1
        x += 1

    while j < len(arrB):
        merged_arr[x] = arrB[j]
        
        j += 1
        x += 1

    # Return the sorted array
    return merged_arr




# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    
    # Base case
    if len(arr) > 1: 

        # Grab the middle index of the array
        mid = len(arr) // 2

        # Separate arr into two lists 
        left = arr[:mid]
        right = arr[mid:]
        print("Divided a list")

        # For each list, use the merge function
        merge_sort(left)  # By the time this gets done, it will be a sorted list
        merge_sort(right) # By the time this gets done, it will be a sorted list
        
        # Set index value for the list to the left, and the list to the right
        i = 0   # Current index in left
        j = 0   # Current index in right
        
        # Set index for arr, to insert the new values
        x = 0
        
        # Compare left[i] with righ[j]
        # While i is less than the length of left AND j is less than the length of right
        while i < len(left) and j < len(right):
            
            # if left[0] is smaller than right[0]
            if left[i] < right[j]:
                # Set the element at arr[0] as left[0]
                arr[x] = left[i]
                
                # Increment index of both left and arr
                i += 1      # So we ignore the previous index from now on
                x += 1      # So we can add items to next index

            # else
            else:
                # Set arr[0] as right[0]
                arr[x] = right[j]

                # Increment index of both right and arr
                j += 1      # So we ignore the previous index from now on
                x += 1      # So we can add items to next index

        # Make sure we add whatever items are left in each array
        while i < len(left):
            arr[x] = left[i]
        
            i += 1
            x += 1

        while j < len(right):
            arr[x] = right[j]
        
            j += 1
            x += 1


    return arr


arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

print(merge_sort(arr1))


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here


    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here


    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr

#Find maximum and minimum element in an array with minimum number of comparisons

def min_max(array):
    # #using built-in functions min and max
    # return min(array), max(array)
    
    # #using built-in sorted() function
    # array.sort()
    # return array[0], array[-1]
    
    # #looping through the array
    # fmin = fmax = array[0]
    # for x in array[1:]:
    #     if x>fmax:
    #         max = x
    #     if x<fmin:
    #         fmin = x
    # return fmin, fmax
    
    #GfG method: using recursion (divide and conquer approach)
    l = len(array)
    if l==1:
        return array[0], array[0]
    elif l==2:
        if array[0]>array[1]:
            return array[1], array[0]
        else:
            return array[0], array[1]
    elif l>2:
        lmin, lmax = min_max(array[:(l//2)+1])
        rmin, rmax = min_max(array[l//2:])
        if lmin>=rmin:
            fmin = rmin
        else:
            fmin = lmin
        if lmax>=rmax:
            fmax = lmax
        else:
            fmax = rmax
        return fmin, fmax
    
        
    
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(min_max(arr))
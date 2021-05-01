# Reverse an array

def reverseWord(s):
    #your code here
    
    ##using in-built function reversed()
    #return ''.join(reversed(s))
    
    ##using string slicing
    #return s[::-1]
    
    ##looping through the string
    #new = ''
    #for char in s:
        #appending consequent characters to the start of new string
    #    new = char + new
    #return new
    
    ##GfG method: swap end characters
    new = [c for c in s]
    for i in range(len(s)//2):
        new[i], new[-(i+1)] = s[-(i+1)], s[i]
    return ''.join(new)
    
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        print(reverseWord(s))
        t = t-1

# } Driver Code Ends
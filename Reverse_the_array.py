class Solution:
    @staticmethod
    def Reverse_the_array(array):
        i,j = 0,len(array)-1
        while i<j:
            array[i],array[j]=array[j],array[i]
            i+=1
            j-=1

if __name__ == '__main__':
    array=list(map(int,input().split()))
    ob=Solution()
    ob.Reverse_the_array(array)
    print(*array)

class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if array == []:
            return 0
        max_number = max(array)
        n = len(array)
        for i in range(n-1):
            midnumber = array[i]
            for j in range(i+1,n):
                midnumber += array[j]
                if midnumber > max_number:
                    max_number = midnumber

        return max_number


s = Solution()
print(s.FindGreatestSumOfSubArray([1,-2,3,10,-4,7,2,-5]))
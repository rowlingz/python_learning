class Solution:
    def reOrderArray(self, array):
        eve_array = []
        odd_array = []
        for number in array:
            if (number % 2):
                odd_array.append(number)
            else:
                eve_array.append(number)

        for eve in eve_array:
            odd_array.append(eve)

        return odd_array


class Solution:
    def findLucky(self, arr):
        array = [-1]
        Set = set(arr)
        for value in Set:
            if arr.count(value) == value:
                array.append(value)
        return max(array)

# Create an instance of the Solution class
solution = Solution()
# Call the findLucky method on the instance and print the result
print(solution.findLucky([1, 2, 2, 3, 3, 3,4,4,4,4]))
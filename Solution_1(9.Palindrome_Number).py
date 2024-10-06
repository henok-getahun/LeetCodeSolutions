class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        i = 0
        size = len(x)
        j = math.floor(size/2)
        print(j)
        for i in range(j):
                if x[i] != x[size - 1 - i]:
                    return False
        return True

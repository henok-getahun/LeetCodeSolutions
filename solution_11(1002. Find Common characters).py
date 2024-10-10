class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        arr = []
        res = []
        for i in range(len(words)):
            arr.append(list(words[i]))

        for i in range(len(arr[0])):
            count = 0
            for j in range(1, len(arr)):
                if arr[0][i] in arr[j]:
                    count += 1
                    arr[j].remove(arr[0][i])
            if count == len(words)-1:
                res.append(arr[0][i])
        return res

# Time complexity => O(n * m^2) space complexity => O(n * m)

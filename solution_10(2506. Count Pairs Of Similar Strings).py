class Solution:
    def similarPairs(self, words: List[str]) -> int:
        list = []
        for i in range(len(words)):
            list.append(set(words[i]))

        count = 0
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if list[i] == list[j]:
                    count += 1
        return count

         # Time Complexity: O(n*m + n^2*m) = (n^2*m) 
         # where m  is the average length of the word
         # Space Complexity:O(n⋅m)

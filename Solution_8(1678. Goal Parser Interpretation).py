class Solution:
    def interpret(self, command: str) -> str:
        res=''
        i = 0
        while True:
            if i >= len(command):
                return res
            if command[i] == 'G':
                res += 'G'
                i +=1
            elif(command[i:i+4]=='(al)'):
                res +='al'
                i += 4
            else:
                res +='o'
                i +=2
            

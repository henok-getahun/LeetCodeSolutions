class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        answer = []
        Tk = celsius + 273.15
        Tf = celsius * 1.80 + 32.00
        answer.append(Tk)
        answer.append(Tf)

        return answer
        

class Solution:
    def processStr(self, s: str, k: int) -> str:
        count = 0
        for i in s:
            if (i.islower()):
                count += 1
            if (i == '*'):
                count -= 1
            if (i == '#'):
                count *= 2
        if k >= count:
            return '.'
        result = ""
        for i in s:
            if (i.islower()):
        	    result += i
            if (i == '*'):
                result = result[:-1]
            if (i == '#'):
            	result += result
            if (i == '%'):
                result = result[::-1]
        return result[k] if k < len(result) else '.'

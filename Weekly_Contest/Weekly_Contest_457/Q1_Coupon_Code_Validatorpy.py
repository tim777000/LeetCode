class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        result = []
        valid_business = ["electronics", "grocery", "pharmacy", "restaurant"]
        for i in range(len(code)):
            if (self.code_valid(code[i]) and businessLine[i] in valid_business and isActive[i] is True):
                result.append((code[i], businessLine[i]))
        return [i[0] for i in sorted(result,key=lambda x: (x[1], x[0]))]

    def code_valid(self, code: str) -> bool:
        if (not code):
    	    return False
        for i in code:
            if (not i.isdigit() and not i.isalpha() and i != '_'):
        	    return False
        return True

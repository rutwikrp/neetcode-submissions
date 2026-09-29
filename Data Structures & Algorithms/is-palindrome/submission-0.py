class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=list(s)
        a=[cleaned for item in a if (cleaned := re.sub(r'[^a-zA-Z0-9]', '', item))]
        rev_a=a[::-1]
        answer=[s.casefold() for s in a] == [s.casefold() for s in rev_a]
        return answer
        
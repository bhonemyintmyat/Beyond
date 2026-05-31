class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        exp = len(columnTitle)-1
        asc = 0
        for num in columnTitle:
            asc = (ord(num)-64)*26**exp+asc
            exp-=1
        return asc


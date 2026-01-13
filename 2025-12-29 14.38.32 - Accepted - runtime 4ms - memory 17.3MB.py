class Solution:
    def countAsterisks(self, s: str) -> int:
        count = 0
        in_pair = False
        for c in s:
            if c == '|':
                in_pair = not in_pair
            elif c == '*' and not in_pair:
                count += 1
        return count
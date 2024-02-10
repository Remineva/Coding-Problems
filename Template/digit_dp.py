import collections
import math
import itertools
import functools
class Solution:
    def count(self, nums):
        s = str(nums)
        # is_zero: can this digit be zero
        # is_limit: upper bound is s[i]
        @functools.cache
        def dp(i: int, mask: int, is_limit: bool, is_zero: bool) -> int:
            if i == len(s):
                return int(is_zero)
            res = 0
            if not is_zero:
                res = dp(i + 1, mask, False, False)
            bound = int(s[i]) if is_limit else 9
            for d in range(1 - int(is_zero), bound + 1):
                if mask >> d & 1 == 0:
                    res += dp(i + 1, mask ^ 1 << d, is_limit and d == bound, True)
            return res
        return dp(0, 0, True, False)


#Find the numbers between num1 and num2 such that the digit sum is between min_sum and max_sum.
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        M = 10 ** 9 + 7
        @functools.cache
        def dp(i, is_limit, s, st) -> int:
            if s > max_sum:
                return 0
            if i == len(st):
                return s >= min_sum
            res = 0
            bound = int(st[i]) if is_limit else 9
            for d in range(bound + 1):
                res += dp(i + 1, is_limit and d == bound, s + d, st)
            return res % M
        return (dp(0, True, 0, num2) - dp(0, True, 0, str(int(num1)-1))) % M

#v 2.0
    def count(self, start: int, finish: int) -> int:
        low = str(start)
        high = str(finish)
        n = len(high)
        low = '0' * (n - len(low)) + low
        @functools.cache
        def dfs(i: int, limit_low: bool, limit_high: bool) -> int:
            if i == n:
                return 1
            
            lo = int(low[i]) if limit_low else 0
            hi = int(high[i]) if limit_high else 9
            
            res = 0
            for d in range(lo, hi + 1):
                res += dfs(i + 1, limit_low and d == lo, limit_high and d == hi)
            return res
        return dfs(0, True, True)


a = Solution()
a.count()

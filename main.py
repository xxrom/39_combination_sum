from typing import List


class Solution:

  def checkPath(self, path: List[int]):
    path.sort()

    strPath = '/'.join([str(num) for num in path])

    if strPath not in self.foundPaths:
      self.foundPaths[strPath] = path

  def bfsFind(self, path: List[int], currentSum: int):

    for nextNumber in self.candidates:
      nextSum = currentSum + nextNumber

      if nextSum <= self.target:
        if nextSum == self.target:
          self.checkPath(path + [nextNumber])

        else:
          self.bfsFind(path + [nextNumber], nextSum)

      else:
        break

  def combinationSum(self, candidates: List[int],
                     target: int) -> List[List[int]]:
    self.foundPaths = {}
    self.candidates = candidates
    self.candidates.sort()
    self.target = target

    self.bfsFind([], 0)

    return self.foundPaths.values()


my = Solution()
c = [2, 3, 6, 7]
n = 7
ans = my.combinationSum(c, n)
print("ans", ans)

# Runtime: 780 ms, faster than 5.08% of Python3 online submissions for Combination Sum.
# Memory Usage: 13.8 MB, less than 6.06% of Python3 online submissions for Combination Sum.

# Runtime: 404 ms, faster than 7.48% of Python3 online submissions for Combination Sum.
# Memory Usage: 13.8 MB, less than 6.06% of Python3 online submissions for Combination Sum.

# Runtime: 312 ms, faster than 8.65% of Python3 online submissions for Combination Sum.
# Memory Usage: 13.7 MB, less than 7.57% of Python3 online submissions for Combination Sum.

# added self.candidates.sort() + for break
# Runtime: 188 ms, faster than 13.41% of Python3 online submissions for Combination Sum.
# Memory Usage: 13.9 MB, less than 6.06% of Python3 online submissions for Combination Sum.
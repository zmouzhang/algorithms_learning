class Solution(object):
	def reverse(self, x):
		"""
		:type x: int
		:rtype: int
		"""

		if (-2 ** 31 <= x <= 2 ** 31 - 1) and (x != 0):
			tmp = ''
			s = str(x)
			length = len(s)
			if x < 0:
				tmp = '-'
				for i in range(1, length):
					tmp += s[length - i]
			else:
				for i in range(0, length):
					tmp += s[length - i - 1]
			target = int(tmp)
			return target if -2 ** 31 <= target <= 2 ** 31 - 1 else 0
		else:
			return 0


a = Solution()
b = 123456789
print(a.reverse(b))

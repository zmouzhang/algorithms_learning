"""
翻转数字
1，将证数强转成字符串
2，判断数字是否小于0，如果小于0，则将前面添加‘-’；
3，将数字字符串进行翻转
"""

class Solution(object):
	def reverse(self, x):
		"""
		:type x: int
		:rtype: int
		"""

		if (-2 ** 31 <= x <= 2 ** 31 - 1) and (x != 0):
			tmp = ''
			# 整型转字符串
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
print(type(b))
print(a.reverse(b))

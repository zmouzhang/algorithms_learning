class Solution(object):
	def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		if not self:
			return 0
		else:
			left = 0
			current = 0
			maxLength = 0
			temp = set()
			for i in range(len(s)):
				current += 1
				while s[i] in temp:
					temp.remove(s[left])
					left += 1
					current -= 1
				if maxLength < current:
					maxLength = current
				temp.add(s[i])
			return maxLength
a = Solution()
print(a.lengthOfLongestSubstring('abca'))
class Solution(object):
	
	def isValid(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		if len(s) == 0 :
			return False
		stack = []
		dic = {'(': ')', '[': ']', '{': '}'}
		for item in s:
			if item in dic:
				stack.append(item)
				continue
			elif stack and dic[stack[-1]] == item:
				del stack[-1]
			else:
				return False
		return not stack
		
a = Solution()
print a.isValid("()")
	
		

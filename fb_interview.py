def match(pattern, text):
	import re
	try:
		temp = pattern.index('.')
		pattern = pattern[:temp] + '[\w\d]' + pattern[temp + 1:]
	except:
		pass

	match = re.search(pattern, text)
	if match:
		return True
	return False

print match('fac.bo*k', 'facebook')

'''
Implementation of Python 3 in built function str.split() which splits a string according to 
the delimiter passed. By default it will split on " "(whitespace). 
'''
def split(string, delimiter = " ") -> list:
	if not string:
		return [string]
	result = []
	start = 0
	for idx, ch in enumerate(string):
		if ch == delimiter:
			result.append(string[start:idx])
			start = idx + 1
	result.append(string[start:idx+1])
	if start == 0:
		return [string]
	return result

if __name__ == "__main__":
	print(split("ab cd ef"))
	print(split("ax,cd", ","))
	

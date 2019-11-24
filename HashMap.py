'''
This is a implementation of string hashing using Python list. I have implemented according 
to the functionality of dict(). The ADT hashmap defined to provide O(1) time complexity add(), 
get() and delete() operation. 

The size can be made variable using some minor modifications. In later versions, I will try 
to implement the functionality we have with dict().keys() to iterate over the keys and also 
will try to generalize for hashing with other immutable keys as we can do in dict(). 

@author 
Tarit Goswami
Dept. of Comp. Sc. and Engg.
'''

class HashMap:
	def __init__(self, size):
		self.size = size
		self.map = [None] * self.size

	# private function implements the hash-function for string type key
	# implements only string hashing
	def _get_hash(self, key:str)->int:
		h = 0
		for ch in key:
			h += ord(ch)
		return h % self.size

	def add(self, key, val):
		key_hash = self._get_hash(key)
		key_val = [key, val]

		if self.map[key_hash] is None:
			self.map[key_hash] = [key_val] # using list because we may face collision later
			return True
		else:
			# we will be here when we face collision or adding val to a 
			# pre-existing key
			for pair in self.map[key_hash]:
				if pair[0] == key:
					# if the key already exists then update the value
					self.map[key_hash] = val 
					return True
			self.map[key_hash].append(key_val)
			return True

	def get(self, key):
		key_hash = self._get_hash(key)

		if self.map[key_hash] is not None:
			for pair in self.map[key_hash]:
				if pair[0] == key:
					return pair[1]
		return '{} is not in the HashMap'.format(key)

	def delete(self, key):
		key_hash = self._get_hash(key)

		if self.map[key_hash] is None:
			return 'No key '+ key + ' to delete'
		for i in range(0, len(self.map[key_hash])):
			if self.map[key_hash][i][0] == key:
				self.map[key_hash].pop(i)
				return True

	def __repr__(self):
		# usually used by developer to debug, so showing the structure itself
		# will be hellpful
		for ind, pair in enumerate(self.map):
			if pair is None:
				print('{}: {}'.format(ind, pair))
			else:
				print(ind, end = ": ")
				for pair in self.map[ind]:
					print(pair, end = ", ")
				print() 


	def __str__(self):
		dic = []
		for ll in self.map:
			if ll is not None:
				for pair in ll:
					dic.append(pair[0] + ': ' + str(pair[1]))
		return '{' + ', '.join(dic) + '}'

hmap = HashMap(10)
hmap.add('Abc', 4)
hmap.add('Dpgh', 9)
hmap.add('Pgh', 3)
hmap.add('Hkjmp', 1)
hmap.__repr__()
print(hmap)




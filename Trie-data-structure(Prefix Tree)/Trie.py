'''
Python 3 implementation of Trie data structure, which stores lowercase english alphabets and every node
has an attribute `terminating` to store number of strings inserted which was terminated at that node. 

It can be used as this code below:
>>> t = Trie()
>>> t.insert("pqrs") # inserts "pqrs" to the Trie
>>> t.insert("pqst")
>>> t.query("pqrs")
1
--------------------------------
@author: Tarit Goswami, Software Developer, India
@date: 09/04/2020
'''


class TrieNode:
	'''Represents a single node in a Trie, it contains a variable to keep track of number of strings ends at that node and a list of length 26 to store address of next nodes'''

	def __init__(self):
		self.terminating = 0          # storing number of strings end at this node 
		self.trieNodes = [None] * 26   # keeping a pointer to all possible 26 lowercase letters
	                                   
	def next(self, ch:str) -> 'TrieNode object':
		'''Returns a TrieNode object, if there is any, corresponds to character passed as argument'''
		return self.trieNodes[ord(c)-ord('a')]

class Trie:
	'''Trie data structure'''
	def __init__(self):
		self.root = TrieNode()

	def insert(self, s:str) -> None:
		'''Inserts a string to the Trie'''
		trav = self.root
		i = 0
		while i < len(s):
			idx = ord(s[i]) - ord('a')
			if trav.trieNodes[idx]:
				trav = trav.trieNodes[idx]
				i += 1
			else:
				break
		if i == len(s):
			trav.terminating += 1
		else:
			for k in range(i, len(s)):
				idx = ord(s[k]) - ord('a')
				trav.trieNodes[idx] = TrieNode()
				trav = trav.trieNodes[idx]
			trav.terminating = 1

	def query(self, s:str)->int:
		'''Returns the number of times a string occurs in the Trie, if the string does not exists in Trie then return 0'''
		trav = self.root
		for i in range(len(s)):
			idx = ord(s[i]) - ord('a')
			if trav.trieNodes[idx]:
				trav = trav.trieNodes[idx]
			else:
				return 0
		return trav.terminating 

	def delete(self, s:str) -> None:
		'''Deletes a string from the Trie'''
		raise NotImplementedError("Trie().delete(str) is not implemented yet")

t = Trie()
t.insert("pqrs")
t.insert("pqrs")
t.insert("qstp")
t.insert("abdc")
t.insert("psst")
print(t.query("pqrs"))    # -> 2, "pqrs" was inserted twice
print(t.query("pqrstu"))  # -> 0, "pqrs" is in the Trie, but "pqrstu" is not there
print(t.query("psst"))    # -> 1, "psst" was inserted once
print(t.query("adb"))     # -> 0, as no string "adb" present, though "adbc" is present



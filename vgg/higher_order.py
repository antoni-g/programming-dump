class Test:
	def __init__(self,function):
		self.function = function

	def call(self):
		self.function()

def method():
	print("woop")

s = Test(method)
s.call()
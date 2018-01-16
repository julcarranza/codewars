class Block(object):
	def __init__(self, object):
		Block.object = object
	
	def get_width(self):
		
		return self.object[0]

	def get_length(self):
	
		return self.object[1]

	def get_height(self):
		
		return self.object[2]

	def get_volume(self):
	
		return self.object[0] * self.object[1] * self.object[2]
	
	def get_surface_area(self) :
		return self.object[0] * self.object[1] * 2 + self.object[0] * self.object[2] * 2 + self.object[2] * self.object[1] * 2

b = Block([89,17,41])

print (b.get_width())
print (b.get_length())
print (b.get_height())
print (b.get_volume())
print (b.get_surface_area())

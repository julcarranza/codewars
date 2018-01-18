import math
class Sphere(object):
	def __init__(self, r, m):
		Sphere.r = r
		Sphere.m = m
	
	def get_radius(self):	
		return self.r

	def get_mass(self):	
		return self.m

	def get_volume(self):
		return round( ((4/3)*(math.pi)*self.r**3), 5)
	
	def get_surface_area(self) :
		return round( (4*(math.pi)*self.r**2), 5 )

	def get_density(self):
		return round( (self.m/((4/3)*(math.pi)*self.r**3)), 5)

b = Sphere(2, 50)

print (b.get_radius())
print (b.get_mass())
print (b.get_volume())
print (b.get_surface_area())
print (b.get_density())

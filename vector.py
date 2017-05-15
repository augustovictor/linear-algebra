from math import sqrt

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def sum(self, v):
        return Vector([el1 + el2 for el1, el2 in zip(self.coordinates, v.coordinates)])
    
    def minus(self, v):
        return Vector([el1 - el2 for el1, el2 in zip(self.coordinates, v.coordinates)])
    
    def times_scalar(self, v):
        return Vector([el1 * el2 for el1, el2 in zip(self.coordinates, v.coordinates)])
    
    def magnitude(self):
        coord_squared = [coord**2 for coord in self.coordinates]
        return sqrt(sum(coord_squared))
        
    
    def normalization(self):
        try:
            magnitude = self.magnitude()
            return [1/magnitude * n for n in self.coordinates]
        except ZeroDivisionError:
            raise Exception('Cannot normalize zero vector') 
        


# ARITIMETICAL OPERATIONS
vec1 = Vector([1, 2, 3])
vec2 = Vector([3, 2, 1])
print vec1.sum(vec2)
print vec1.minus(vec2)
print vec1.times_scalar(vec2)

# NORMALIZATION
v1 = Vector([-0.221, 7.437])
v2 = Vector([8.813, -1.331, -6.247])

v3 = Vector([5.581, -2.136])
v4 = Vector([1.996, 3.108, -4.554])
# STEP 1
print v1.magnitude()
print v2.magnitude()

# STEP 2
print v3.normalization()
print v4.normalization()
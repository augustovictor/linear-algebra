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
        

vec1 = Vector([1, 2, 3])
vec2 = Vector([3, 2, 1])
print vec1.sum(vec2)
print vec1.minus(vec2)
print vec1.times_scalar(vec2)

# numbers = [1, 2, 3]
# doubled = []

# for n in numbers:
#     if n % 2 == 0:
#         doubled.append(n * 2)
# print doubled

# com_list = [n * 2 for n in numbers if n % 2 == 0]


# names = ['Victor', 'Augusto', 'Tai', 'Costa']
# big_name = [name + ' has more than 5 chars' for name in names if len(name) > 5]
# print big_name
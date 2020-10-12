shapes1 = {'round', 'square', 'triangle'}
shapes2 = {'oval', 'rectangle'}
shapes3 = {'square', 'oval', 'round'}

shape_union = shapes1.union(shapes2).union(shapes3)
print(shape_union)

shape_intersection = shapes1.intersection(shapes3).intersection(shapes2)
print(shape_intersection)

shape_difference = shapes1.difference(shapes3)
print(shape_difference)
def add_arrays(x,y):
    z=[]
    for x_elem, y_elem in zip(x,y):
        z.append(x_elem+y_elem)
    return z
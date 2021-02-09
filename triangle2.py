def triangle_2(height):
    for count in range(1, height+1):
        print(' ' * (height-count), '*' * ((2*count)-1))


triangle_2(5)

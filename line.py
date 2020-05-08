#! python3

print('Hello student, hope you are doing well in maths and are constantly revising! \nHere is a program that calculates the equation of a straight line.')

def my_slope(x1, x2, y1, y2):
    dx = x2 - x1
    dy = y2 - y1
    slope = dy/dx
    return slope

def my_distance(x1, x2, y1, y2):
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    distance = (dy**2 + dx**2)**0.5
    return distance

def get_c(x1, y1, gradient):
    y_intercept = y1 - (x1 * gradient)
    return y_intercept

#print(get_c(3,2,1))

x1 = int(input('First what is the first coordinate X value? \n'))
y1 = int(input('Now input the first coordinate Y value? \n'))
x2 = int(input('Alright what is the second coordinate X value? \n'))
y2 = int(input('And finally what is the second coordinate Y value? \n'))


m = my_slope(x1, x2, y1, y2)

try:
    distance = my_distance(x1, x2, y1, y2)
except ZeroDivisionError:
    print('Tried dividing by zero')

c = get_c(x1, y1, m)


print('Great the gradient of the line is ' + str(round(m, 2)) + ' and the distance between the \
two coordinates is '+str(round(distance, 2))+' units.')
print('The line equation is Y = ' +str(round(m, 2))+'X + ' +str(round(c, 2))+'.')
print('Have a nice day!')


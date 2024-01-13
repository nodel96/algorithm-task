# Factorial
def factorial(n):
    if n == 0: return 1
    return n * factorial(n - 1)

# Factorial grows very fast (no limits for integer values)
factorial(50)

# Collatz sequence
def collatz(n):
    print(n, end=' ')
    if n == 1: return
    if n % 2 == 0: collatz(n // 2)
    else: collatz(3 * n + 1)

collatz(7)

# Convert a number to binary representation
def convert(n):
    if n == 1: return '1'
    return convert(n // 2) + str(n % 2)

convert(6)

# H-Tree Drawing
import matplotlib
import matplotlib.lines as lines
import matplotlib.pyplot as plot

def hTree(n, sz, x, y, canvas):
    if n == 0: return
    x0 = x - sz/2
    x1 = x + sz/2
    y0 = y - sz/2
    y1 = y + sz/2

    canvas.add_line(lines.Line2D([x0, x1],[y, y]))
    canvas.add_line(lines.Line2D([x0, x0],[y0, y1]))
    canvas.add_line(lines.Line2D([x1, x1],[y0, y1]))
    
    hTree(n-1, sz/2, x0, y0, canvas)
    hTree(n-1, sz/2, x0, y1, canvas)
    hTree(n-1, sz/2, x1, y0, canvas)
    hTree(n-1, sz/2, x1, y1, canvas)

def draw(n):
    fig, canvas = matplotlib.pyplot.subplots()
    plot.axis('square')
    canvas.set_xlim(0, 1)
    canvas.set_ylim(0, 1)
    sz = .5
    x  = .5
    y  = .5
    
    hTree(n, sz, x, y, canvas)
    plot.show()

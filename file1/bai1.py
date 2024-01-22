with open("TCMT.INP") as f:
    x = int(f.readline())
def gcd(x, y):
    while y:
        x,y = y,x % y
        return x
x = x
y = 100 -x
g = gcd(x,y)
b = g // x + g // y
with open("TCMT.OUT", "w") as c:
    c.write(str(b))
    

    
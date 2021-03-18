def roots(a, b, c):
  from math import sqrt
  q = sqrt(b**2 - 4 * a * c)
  x1 = (-b - q)/(2*a)
  x2 = (-b + q)/(2*a)
  return (x1,x2)

def test_roots_floats():
  b = 10
  a = 1
  c = 8
  print (roots (a,b,c))
  return
test_roots_floats()
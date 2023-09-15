from shapes import Rectangle, Triangle

def main():
  r1 = Rectangle(5, 5)
  r2 = Rectangle(2, 4)

  print(f'The area of r1 is {r1.area}')
  print(f'The perimeter of r2 is {r2.perimeter}')
  print(f'r1 is square: {r1.is_square}')

  t1 = Triangle(2, 4, 5, 3)
  t2 = Triangle(3, 3, 8, 5)

  print(f'The area of t1 is {t1.area}')
  print(f'The area of t2 is {t2.perimeter}')
  print(f't1 is a valid triangle: {t1.is_valid}')

if __name__== "__main__":
  main()
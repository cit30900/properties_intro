from shapes import Rectangle, Triangle

def main():
  r1 = Rectangle(2,2)
  r2 = Rectangle(3,5)

  print(f'The area of r1 is {r1.area}.')
  print(f'The perimeter of r2 is {r2.perimeter}.')
  print(f'r1 is square: {r1.is_square}')
  print(f'r2 is square: {r2.is_square}')

  t1 = Triangle(3, 3, 3, 5)
  t2 = Triangle(3, 5, 7, 6)

  print(f'The area of t1 is {t1.area}.')
  print(f'The perimeter of t2 is {t2.perimeter}.')
  print(f't1 is valid: {t1.is_valid}')
  print(f't2 is valid: {t2.is_valid}')

if __name__== "__main__":
  main()
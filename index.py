from shapes import Rectangle, Triangle

def main():
  r1 = Rectangle(2,2)
  r2 = Rectangle(3,5)

  print(f'The area of r1 is {r1.area}.')
  print(f'The perimeter of r2 is {r2.perimeter}.')

  t1 = Triangle(3, 3, 3, 5)
  t2 = Triangle(3, 5, 7, 6)

  print(f'The area of t1 is {t1.area}.')
  print(f'The perimeter of t2 is {t2.perimeter}.')

if __name__== "__main__":
  main()
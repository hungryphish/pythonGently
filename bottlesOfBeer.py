def bottles99():
  for bottles in reversed(range(2,100)):
    if bottles-1 > 0:
      print(f"{bottles} bottles of beer on the wall")
      print(f"{bottles} bottles of beer")
      print("Take one down,\nPass it around,")
      print(f"{bottles-1} bottles of beer on the wall\n")
  print(f"1 bottle of beer on the wall")
  print(f"1 bottle of beer")
  print("Take one down,\nPass it around,")
  print('No more bottles of beer on the wall!')

bottles99()

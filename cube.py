print("Give me a number, and I'll give you the volume of that cube")
cube = input("enter it here: ")


def cubeIt(cube):
  try:
    cube = int(cube)
  except ValueError:
    print("Aw, hell nah I ain't do letters n shit. I'm gonna just input 10 for ya")
    cube = 10
  if cube > 0:
    print(cube*cube*cube)
    return cube*cube*cube
  else:
    print("Sorry, I can't take the volume of a cube that doesn't exist or has negative dimensions\n sorry, m8 I stop working now")
    return -1


cubeIt(cube)
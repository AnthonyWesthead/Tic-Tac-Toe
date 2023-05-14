import time
#Original Board
row1 = ["1", "2", "3"]
row2 = ["4", "5", "6"]
row3 = ["7", "8", "9"]
a=2
print("Welcome to Tic Tac Toe")

print(row1[0]+"|"+row1[1]+"|"+row1[2])
print(row2[0]+"|"+row2[1]+"|"+row2[2])
print(row3[0]+"|"+row3[1]+"|"+row3[2])

#Input of X
def x_function():
  xinput = input("X's turn. Pick the number for the square. >> ")
  if xinput == ("1"):
      row1[0] = "x"
  elif xinput == ("2"):
    row1[1] = "x"
  elif xinput == ("3"):
    row1[2] = "x"
  elif xinput == ("4"):
    row2[0] = "x"
  elif xinput == ("5"):
    row2[1] = "x"
  elif xinput == ("6"):
    row2[2] = "x"
  elif xinput == ("7"):
    row3[0] = "x"
  elif xinput == ("8"):
    row3[1] = "x"
  elif xinput == ("9"):
    row3[2] = "x"
  else:
    print("Input a number 1-9")
  print(row1[0]+"|"+row1[1]+"|"+row1[2])
  print(row2[0]+"|"+row2[1]+"|"+row2[2])
  print(row3[0]+"|"+row3[1]+"|"+row3[2])

#Input of O
def o_function():
  oinput = input("O's turn. Pick the number for the square. >> ")
  if oinput == ("1"):
    row1[0] = "o"
  elif oinput == ("2"):
    row1[1] = "o"
  elif oinput == ("3"):
    row1[2] = "o"
  elif oinput == ("4"):
    row2[0] = "o"
  elif oinput == ("5"):
    row2[1] = "o"
  elif oinput == ("6"):
    row2[2] = "o"
  elif oinput == ("7"):
    row3[0] = "o"
  elif oinput == ("8"):
    row3[1] = "o"
  elif oinput == ("9"):
    row3[2] = "o"
  else:
    print("Input a number 1-9")
  print(row1[0]+"|"+row1[1]+"|"+row1[2])
  print(row2[0]+"|"+row2[1]+"|"+row2[2])
  print(row3[0]+"|"+row3[1]+"|"+row3[2])

#Xwin is player X winning

def xwin_function():
  if row1[0]=="x" and row1[1]=="x" and row1[2]=="x":
    print("X wins")
    time.sleep(3)
    a=3
    print(chr(27) + '[2j')
    print('\033c')
    print('\x1bc')
    
  elif row2[0]=="x" and row2[1]=="x" and row2[2]=="x":
    print("X wins")
    time.sleep(3)
    a=3
    print(chr(27) + '[2j')
    print('\033c')
    print('\x1bc')
    
  elif row3[0]=="x" and row3[1]=="x" and row3[2]=="x":
    print("X wins")
    time.sleep(3)
    a=3
    print(chr(27) + '[2j')
    print('\033c')
    print('\x1bc')
    
  elif row1[0]=="x" and row2[0]=="x" and row3[0]=="x":
    print("X wins")
    time.sleep(3)
    a=3
    print(chr(27) + '[2j')
    print('\033c')
    print('\x1bc')
    
  elif row1[1]=="x" and row2[1]=="x" and row3[1]=="x":
    print("X wins")
    time.sleep(3)
    a=3
    print(chr(27) + '[2j')
    print('\033c')
    print('\x1bc')
    
  elif row1[2]=="x" and row2[2]=="x" and row3[2]=="x":
    print("X wins")
    time.sleep(3)
    a=3
    print(chr(27) + '[2j')
    print('\033c')
    print('\x1bc')
    
  elif row1[0]=="x" and row2[1]=="x" and row3[2]=="x":
    print("X wins")
    time.sleep(3)
    a=3
    print(chr(27) + '[2j')
    print('\033c')
    print('\x1bc')
    
  elif row1[2]=="x" and row2[1]=="x" and row3[0]=="x":
    print("X wins")
    time.sleep(3)
    a=3
    print(chr(27) + '[2j')
    print('\033c')
    print('\x1bc')
    
#Owin is player O winning
  
def owin_function():
  if row1[0]=="o" and row1[1]=="o" and row1[2]=="o":
    print("O wins")
    time.sleep(3)
    a=3
    print(chr(27) + '[2j')
    print('\033c')
    print('\x1bc')
    
  elif row2[0]=="o" and row2[1]=="o" and row2[2]=="o":
    print("O wins")
    time.sleep(3)
    a=3
    print(chr(27) + '[2j')
    print('\033c')
    print('\x1bc')
    
  elif row3[0]=="o" and row3[1]=="o" and row3[2]=="o":
    print("O wins")
    time.sleep(3)
    a=3
    print(chr(27) + '[2j')
    print('\033c')
    print('\x1bc')
    
  elif row1[0]=="o" and row2[0]=="o" and row3[0]=="o":
    print("O wins")
    time.sleep(3)
    a=3
    print(chr(27) + '[2j')
    print('\033c')
    print('\x1bc')
    
  elif row1[1]=="o" and row2[1]=="o" and row3[1]=="o":
    print("O wins")
    time.sleep(3)
    a=3
    print(chr(27) + '[2j')
    print('\033c')
    print('\x1bc')
    
  elif row1[2]=="o" and row2[2]=="o" and row3[2]=="o":
    print("O wins")
    time.sleep(3)
    a=3
    print(chr(27) + '[2j')
    print('\033c')
    print('\x1bc')
    
  elif row1[0]=="o" and row2[1]=="o" and row3[2]=="o":
    print("O wins")
    time.sleep(3)
    a=3
    print(chr(27) + '[2j')
    print('\033c')
    print('\x1bc')
    
  elif row1[2]=="o" and row2[1]=="o" and row3[0]=="o":
    print("O wins")
    time.sleep(3)
    a=3
    print(chr(27) + '[2j')
    print('\033c')
    print('\x1bc')
    

for x in range(4):
  x_function()
  xwin_function()
  if a== (3):
    print(chr(27) + '[2j')
    print('\033c')
    print('\x1bc')
  o_function()
  owin_function()
  if a== (3):
    print(chr(27) + '[2j')
    print('\033c')
    print('\x1bc')
x_function()
xwin_function()

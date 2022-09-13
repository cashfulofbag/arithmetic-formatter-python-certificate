import re

def arithmetic_arranger(problems, show = False):
  list_piece_top = list()
  list_piece_operator = list()
  list_piece_bot = list()
  list_piece_ans = list()

  piece_top = ""
  piece_bot = ""
  piece_answer = ""
  piece_line = ""
  
  arranged_problems = str()
  
  #Check number of problems
  v = len(problems)
  if v > 5:
    return("Error: Too many problems.")
 
  #Search for signs other than digits and not correct operators
  for problem in problems:
    if (re.search("[^\s0-9.+-]",problem)):
      if(re.search("[/]", problem) or re.search("[*]", problem)):
         return("Error: Operator must be '+' or '-'.")
      return("Error: Numbers must only contain digits.")
  
  #Spliting and calculating answers 
  for problem in problems:
    list_piece = problem.split()
    list_piece_top.append(list_piece[0])
    list_piece_operator.append(list_piece[1])
    list_piece_bot.append(list_piece[2])
    if(list_piece[1] == "+"):
      list_piece_ans.append(str(int(list_piece[0]) + int(list_piece[2])))
    if(list_piece[1] == "-"):
      list_piece_ans.append(str(int(list_piece[0]) - int(list_piece[2])))
  for i in range(v):
    if(len(list_piece_top[i]) > 4 or len(list_piece_bot[i]) > 4):
      return("Error: Numbers cannot be more than four digits.")
    
  #Preparing pieces of answers
  for i in range(v):
    width = max(len(list_piece_top[i]), len(list_piece_bot[i]))
    if(i < v -1):
      piece_top = piece_top + list_piece_top[i].rjust(width + 2) + "    "
      piece_bot = piece_bot + list_piece_operator[i] + list_piece_bot[i].rjust(width + 1) + "    "
      piece_line = piece_line + "-"*(width + 2) + "    "
      piece_answer = piece_answer + list_piece_ans[i].rjust(width + 2) + "    "
  
    else:
      piece_top = piece_top + list_piece_top[i].rjust(width + 2)
      piece_bot = piece_bot + list_piece_operator[i] + list_piece_bot[i].rjust(width + 1)
      piece_line = piece_line + "-"*(width + 2)
      piece_answer = piece_answer + list_piece_ans[i].rjust(width + 2)
  
  #Conecting pieces
  if(show):
    arranged_problems = piece_top + "\n" + piece_bot + "\n" + piece_line + "\n" + piece_answer
  else:
    arranged_problems = piece_top + "\n" + piece_bot + "\n" + piece_line
  
  return arranged_problems
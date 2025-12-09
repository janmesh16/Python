print("*****************Question paper ****************")
var_score=0
var_correct=0
var_incorrect=0
print("1. Which command is use for the adding the file to the git ")
print("A. git add")
print("B. git commit")
print("c. git init")
print("d. git push")
x = (input('enter your ans here'))
if (x == 'a'):
  print("correct answer")
  var_correct=var_correct+1
  var_score=var_score+5
else:
  print("wrong answer")
  var_incorrect=var_incorrect+1
for i in x:
  if(i == 'a'):
    print("+5 marks")
  else:
    print("0 marks")

print("2. Which command is use for the adding the commit to the git ")
print("A. git add")
print("B. git commit")
print("c. git init")
print("d. git push")
x = (input('enter your ans here'))
if (x == 'b'):
  print("correct answer")
  var_correct=var_correct+1
  var_score=var_score+5
else:
  print("wrong answer")
  var_incorrect=var_incorrect+1
for i in x:
  if(i == 'b'):
    print("+5 marks")
  else:
    print("0 marks")

print("3. Which command is use for the push to the git ")
print("A. git add")
print("B. git commit")
print("c. git init")
print("d. git push")
x = (input('enter your ans here'))
if (x == 'd'):
  print("correct answer")
  var_correct=var_correct+1
  var_score=var_score+5
else:
  print("wrong answer")
  var_incorrect=var_incorrect+1
for i in x:
  if(i == 'd'):
    print("+5 marks")
  else:
    print("0 marks")


print("4. Which command is use for the initialization the file to the git ")
print("A. git add")
print("B. git commit")
print("c. git init")
print("d. git push")
x = (input('enter your ans here'))
if (x == 'c'):
  print("correct answer")
  var_correct=var_correct+1
  var_score=var_score+5
else:
  print("wrong answer")
  var_incorrect=var_incorrect+1
for i in x:
  if(i == 'c'):
    print("+5 marks")
  else:
    print("0 marks")


print("4. Which command is firstly used to the git ")
print("A. git add")
print("B. git commit")
print("c. git init")
print("d. git push")
x = (input('enter your ans here'))
if (x == 'c'):
  print("correct answer")
  var_correct=var_correct+1
  var_score=var_score+5
else:
  print("wrong answer")
for i in x:
  if(i == 'c'):
    print("+5 marks")
  else:
    print("0 marks")

  print("score",var_score)
  print("correct answer",var_correct)
  print("incorrect answer",var_incorrect)
print("***************End of the paper****************")
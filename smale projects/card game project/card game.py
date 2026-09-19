
name = "osayed"
GUI = int(input(f"wellcome to {name} gmae\n1-Play\n2-About the game\n"))
full_dgree = 0

def stage1():
   
   dgree = 0
   q1 = str(input("10 + 9 - 4 = ?\na-15\nb-12\nc-20\nd-0\n"))

   if q1 == "a":
      print("thats right")
      dgree =+ 1
      full_dgree =+ 1
   else:
      print("thats worng good try")

   q2 = str(input("from what the water is ?\na-Lithum\nb-Iron\nc-carbon\nd-H2O\n"))
   
   if q2 == "d":
      print("thats right")
      dgree =+ 1
      full_dgree += 1
   else:
      print("thats worng good try")

   q3 = str(input("whats the best restaurant = ?\na-Al bake\nb-al watane\nc-bn b5et\nd-al safwah\n"))
   
   if q3 == "a":
      print("thats right")
      dgree =+ 1
      full_dgree += 1
   else:
      print("thats worng good try")

   q4 = str(input("50 + 20 = ?\na-40\nb-20\nc-10\nd-70\n"))
   
   if q4 == "d":
      print("thats right")
      dgree =+ 1
      full_dgree += 1
   else:
      print("thats worng good try")
   return
 
def stage2():
     
     
     q1 = input("solve this quastion\nwhat is the best car in the world ?\n")
     car = "GMC"
     dgree2 = 0

     if q1 == "GMC":
        print("thats right")
        dgree2 =+ 1
        full_dgree =+ 1

     else:
        print("thats wrong")

     q2 = input("solve this quastion\nwhat is the best suse in the world ?\n")
     suse = "garlic"

     if q2 == "garlic":
        print("thats right")
        dgree2 =+ 1
        full_dgree =+ 1
     else:
        print("thats wrong")

def theGame():
   print(f"this game made from {name}")
   return

if GUI == 1:
    peack = int(input("stage1\nstage2\n"))
    if peack == 1: 
       stage1()

    elif peack == 2:
       stage2()

    else:
       print("error")

elif GUI == 2:
   theGame()

else:
   print("error")
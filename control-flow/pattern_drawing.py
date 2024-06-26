num=int(input("Enter the size of the pattern:"))
outer_counter=0
while outer_counter<num:
  inner_counter=0
  while inner_counter<num:
    print("*", end= "")
    inner_counter+=1
  print()
  outer_counter+=1
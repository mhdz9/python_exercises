levels = int(raw_input("Enter the number of levels you want for the pyramid\n"))
character = raw_input("Enter the character you want to see as pattern\n")

for i in range(1,levels+1):
 for j in range(1,i+1):
   print "*",
 print
from sys import argv

script,filename =argv

print(f"We are going to erase{filename}.")
print("if you dont want that,hit CTRL+C (^C).")
print("If you do want that,hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename,'w')

print("Truncating the file.Goodbye!")
target.truncate()

print("Now im going to ask you for three lines.")

line1=input("line1: ")
line2=input("line2: ")
line3=input("line3:  ")

print("Im going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally , we close it." )
target.close()
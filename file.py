

# Writing to new.txt
f = open('new.txt', 'a')
f.write("what are you doing\n")
f.write("new line\n")
f.write("yesss\n")
f.close()

# Reading from new.txt
f = open('new.txt', 'r')
print("Contents of new.txt:")
print(f.read())
f.close()



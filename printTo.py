#Import the module engine_1.
import engine_1

#Write to file.
file = open(“TestFile.txt”, “w”)
file.write(str(engine_1.var))
file.close()

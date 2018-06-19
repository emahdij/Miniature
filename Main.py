from machine import Minature
file = open("E:\\bininput.txt", "r")
txtinput = file.read()
arr = txtinput.split("\n")
miniature = Minature(arr)
miniature.run()

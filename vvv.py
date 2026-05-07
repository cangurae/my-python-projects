import time

print("Welcome to the timer")
time.sleep(1.2)
print("What is the starting point? ")
time.sleep(1.2)
timer = int(input("Please enter your time in seconds: "))
while timer >= 0:
    print (timer)
    time.sleep(1)
    timer = timer - 1
print ("End")
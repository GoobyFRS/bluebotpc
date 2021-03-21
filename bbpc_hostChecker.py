import os #Used to ping
import platform #Not sure, but it works....
import time #Used for system pause...

print("**********")
print("BlueBotPC Host Checker")
print("**********")
targetHost = input("Target Host: ")
print("Pinging " + targetHost + " in two seconds...")
time.sleep(2)
_pingAttempt_ = os.system("ping -n -c 5  " + targetHost) #Unix ping command. Sending 5 pings.
#command = ["ping -c 1", targetHost]

if _pingAttempt_ == 0:
    print(targetHost + " replied")
else:
    print(targetHost + " didn't reply")





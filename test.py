from os import path
if path.isdir("/opt/jenkins-test"):
    print("Yes Test OK")
else:
    print("Ohhhh, No Test Failed")

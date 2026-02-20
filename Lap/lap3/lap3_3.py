inputstrr  = " [WARN] user=Somchai action=LoginFailed ip= 192.168.1.10 "


level = inputstrr.split('[')[1].split(']')[0].strip()
user = inputstrr.split(" ")[2].split('=')[1].strip().lower()
action = inputstrr.split(" ")[3].split('=')[1].strip().lower()
ip = inputstrr.split(" ")[5].strip().lower()



print("Level:" ,level.split())
print("User:",user )
print("Action:",action.upper())
print("IP:", ip)
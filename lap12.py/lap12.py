with open('user_activity.txt') as f:
 for line in f:
  parts = line.split(" ")
user = parts[0]
action = parts[1]
command = " Start "
command = command.strip().lower()

print("Command:",command)

if command == "start":
    print("Result: System started")
elif command == "stop" :
    print("Result: System stopped")
elif command =="restarting":
    print("Result: System restarting")
else :
    print("Result: Unknown command") 
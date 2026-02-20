#6809658138 suwijuk bouchum
connect = 'y'
i = 0 
info = 0
warn = 0
error = 0
unknow =0
while connect == 'y' :
    
    while i < 3 :
        log  = input("Enter log:")
        log = log.split('[')[1].split(']')[0].upper().strip()
        log = ('[' + log + ']')

        if log == "[INFO]":
          print("Type: Information message")
          info +=  1

        elif log == "[WARN]" :
          print("Type: Warning message")
          warn += 1 

        elif log == "[ERROR]" :
          print("Type: Error message")
          error += 1

        else :
          unknow += 1
          print("Type: Unknow message")   

        print("--------------------")
        i += 1
    

    
    i = 0 
    connect = input('Continue? (y/n):\n')


print("Summary")
print("INFO: ",info)
print("WARN: ",warn)
print("ERROR: ",error)
print("UNKNOWN: ",unknow)  
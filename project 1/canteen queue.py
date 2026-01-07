import queue
temp=0
while(True):
    q=queue()
    print("1.add/n2.status/n3.serve/n4.exit")
    temp=input("enter your choice")
    if(temp==100):
        temp=0
    elif(temp==1):
        inputu=input()
        temp+=inputu
        q.append(inputu)
        print("Token generated:",inputu)
    
    elif(temp==2):
        print("students waiting:",temp)
    
    elif(temp==3):
        serve=q.popleft()
        print("serving token:",serve)
    else:
        break

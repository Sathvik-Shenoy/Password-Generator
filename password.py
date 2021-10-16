i=0
while(i==0):
    n=int(input("Press 1 to sign in or press 2 to sign up"))
    if(n==1):
        f1=open("file.txt","r")
        c=input("Enter the password:-")
        if(c==f1.readline()):
            print("Welcome")
            f2=open("file2.txt","r")
            print(f2.read())
        else:
            n1=int(input("Press 1 to try again or press 2 to forget password:-"))
            if(n1==1):
                f1 = open("file.txt", "r")
                c = input("Enter the password:-")
                if (c==f1.readline()):
                    print("Welcome")
                    f2 = open("file2.txt", "r")
                    print(f2.read())
            if(n1==2):
                f1=open("file.txt","w")
                c1=input("Enter the new password:-")
                f1.write(c1)
    else:
        f1 = open("file.txt", "w")
        c1 = input("Enter the new password:-")
        f1.truncate()
        f1.write(c1)

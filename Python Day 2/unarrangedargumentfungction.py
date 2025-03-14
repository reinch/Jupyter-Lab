def greetings(*VarArgs):
    print("Hello Fellow ")
    print("Welcome To Russia ", end='')
    for Arg in VarArgs:
        print(Arg, end='')

greetings("John ","Remedy ","Sony ")
    
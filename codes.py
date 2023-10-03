def greetings():
    name = input("entrez votre nom: ")
    print("Hello "+ name) 

def ismajor(age):
    if age >= 18:
        return True
    else : 
        return False

def square(x):
    return x*x

def somefunction():
    print("Hello world!")


def main():
    greetings()
    age = int(input("Entrez votre age: " ))
    if ismajor(age):
        print("Bienvenue dans le programme!")
    else :
        print("Desole, mais vous n'avez pas l'age requis!")
main()
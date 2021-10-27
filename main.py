def main():
    read()

def read():
    while True:
        exp = input("Introdu o expresie: ")
        exp = clean(exp)
        check(exp)

def clean(exp):
    return "".join(exp.split())

def check(exp):
    n = len(exp)
    l_pan = 0
    r_pan = 0
    conn = 0
    error = 0
    for i in range(n):
        if i < n-1:
            next = i+1
        else:
            next = None

        if exp[i]=="(":
            l_pan = l_pan + 1

            if next != None and (exp[next] in ["(", "¬", "!", "˜"] or exp[next].isalpha()):
                continue
            else:
                print("In '", exp[0:next+1], "' caracterul, '", exp[next], "' nu are ce cauta aici! Trebuia sa urmeze '(','¬' sau o propozitie atomica!", sep="")
                error = 1
                break

        if exp[i] in ["¬", "!", "˜"]:
            conn = conn + 1
            if next != None and (exp[next] == "(" or exp[next].isalpha()):
                continue
            else:
                print("In '", exp[0:next+1], "' caracterul, '", exp[next], "' nu are ce cauta aici! Trebuia sa urmeze '(' sau o propozitie atomica!", sep="")
                error = 1
                break

        if exp[i].isalpha():
            if next != None and (exp[next] in ["∨", "∧" ,"⇒" ,"⇔"] or exp[next] == ")"):
                continue
            else:
                print("In '", exp[0:next+1], "' caracterul, '", exp[next], "' nu are ce cauta aici! Trebuia sa urmeze '∨', '∧' ,'⇒' ,'⇔' sau ')'!", sep="")
                error = 1
                break
        
        if exp[i] in ["∨", "∧" ,"⇒" ,"⇔"]:
            conn = conn + 1
            if next != None and (exp[next].isalpha() or exp[next] == "("):
                continue
            else:
                print("In '", exp[0:next+1], "' caracterul, '", exp[next], "' nu are ce cauta aici! Trebuia sa urmeze o propozitie atomica sau '('!", sep="")
                error = 1
                break

        if exp[i]==")":
            r_pan = r_pan + 1
            if next == None or (next != None and (exp[next] == ")" or exp[next] in ["∨", "∧" ,"⇒" ,"⇔"])):
                continue
            else:
                print("In '", exp[0:next+1], "' caracterul, '", exp[next], "' nu are ce cauta aici! Trebuia sa urmeze '∨', '∧' ,'⇒' ,'⇔' sau ')'!", sep="")
                error = 1
                break

    if l_pan > r_pan:
        if error == 0:
            print("Lipsesc ", l_pan - r_pan, " ')'!", sep="")
            error = 1

    if r_pan > l_pan:
        if error == 0:
            print("Lipsesc ", r_pan - l_pan, " '('!", sep="")
            error = 1

    if l_pan == r_pan and l_pan > conn:
        if error == 0:
            print("Trebuie scoase ", (l_pan - conn), " perechi de parateze!", sep="")
            error = 1

    if l_pan == r_pan == conn:
        if error == 0:
            print("Expresia '", exp, "' este valida!", sep="")
            error = 1
    
main()
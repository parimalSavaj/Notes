# just like switch case
def choice(ch):
    match ch:
        case 'A':
            return "you are A"
        case 'B':
            return "you are B"
        case 'C':
            return "you are C"
        case _:
            return "Unknown"
    
print(choice("A"))
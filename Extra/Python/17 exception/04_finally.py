def abc():
    try:
        a = int(input("Enter number: "))
        return a
    except Exception as e:
        print(e)
        return
    finally:
        print("in case of return this finally block we run")
    
abc()
while True:
    try:
        number = int(input("What is your fav number?\n"))
        print(10/number)
        break
    except ValueError:
        print("Make sure and enter a number")
    except ZeroDivisionError:
        print("Dont pick Zero")
    except:
        break
    finally:
        print("loop complete")

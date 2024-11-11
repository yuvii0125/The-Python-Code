def MyFunc():
    print("Hello World")


if __name__ == "__main__":
    #this will only run if the file is run directly
    print("This file is being run directly")
    MyFunc()
    print(__name__)
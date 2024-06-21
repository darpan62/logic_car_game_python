#logic car game
started = False

while True:
    command = input(">").lower()
    
    if command == "start":
        print("car started..")
        if started:
            print("car is already started")
        else:
            started = True
    elif command == "stop":
        print("car stopped..")

        if not started:
            print("car is already stopped")
        else:
            started = False
    elif command == "help":
        print('''
start-to start the car
stop-to stop the car
quit- to end the game''')
    elif command == "quit":
        break
    else:
        print("sorry, wrong command")
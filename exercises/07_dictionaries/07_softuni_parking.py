iterations = int(input())
parking = {}

for _ in range(iterations):
    command = input().split(' ')

    if command[0] == 'register':
        if command[1] in parking:
            print(f"ERROR: already registered with plate number {parking[command[1]]}")
        else:
            parking[command[1]] = command[2]
            print(f"{command[1]} registered {command[2]} successfully")
    elif command[0] == 'unregister':
        if command[1] not in parking:
            print(f"ERROR: user {command[1]} not found")
        else:
            del parking[command[1]]
            print(f"{command[1]} unregistered successfully")

for key, value in parking.items():
    print(f"{key} => {value}")

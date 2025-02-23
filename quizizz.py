import requests
import random
import json
import threading

# Initialize the file
with open("codes.txt", "w") as f:
    pass

# Define the function that each thread will run
def check_room():
    while True:
        pin = str(random.randint(111111, 999999))
        url = "https://game.quizizz.com/play-api/v5/checkRoom"

        data = {
            "roomCode": pin
        }

        response = requests.post(url, json=data).json()
        if "success" in response:
            responseCode = response['success']
        else:
            if response.get("room", {}).get("totalPlayers") > 1:
                data = "Pin: " + pin + " Players: " + str(response.get("room", {}).get("totalPlayers")) + " Host: " + str(response.get("room", {}).get("hostOccupation")) + " State: " + str(response.get("room", {}).get("state") + " Type: " + str(response.get("room", {}).get("type")))
                print("Adding: " + data)
                with open("codes.txt", "a") as f:
                    f.write(data + "\n")



# Create and start threads
threads = []
for i in range(15):
    t = threading.Thread(target=check_room)
    t.start()
    threads.append(t)

# Optionally, wait for all threads to complete
for t in threads:
    t.join()

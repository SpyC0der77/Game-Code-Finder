import requests
import random
import json
import threading
print("Starting")
print("To use, go to https://gimkit.com/join")

# Define the function that each thread will run
def check_room():
    while True:
        pin = str(random.randint(0, 999999)).zfill(6)
        url = "https://www.gimkit.com/api/matchmaker/find-info-from-code"

        data = {
            "code": pin
        }

        response = requests.post(url, json=data).json()
        if "message" in response:
            responseCode = response['message']
        else:
          print(pin + " - " + str(response['useRandomNamePicker']))


# Create and start threads
threads = []
for i in range(20):
    t = threading.Thread(target=check_room)
    t.start()
    threads.append(t)
    print("Thread " + str(i + 1) + " initialized")

# Optionally, wait for all threads to complete
for t in threads:
    t.join()

import requests
import time
import random
import json

class UpdatingFirebase:
    def _init_(self):
        self.firebase_URL = "https://careband-5792a-default-rtdb.firebaseio.com/"

    def valueGenerator(self):
        return {
            "position": random.randint(1,10),
            "posture": random.randint(1,10),
            "weightLift": random.randint(1,10), 
        }

    def dataParser(self, data):
        return {
            "date":time.strftime("%d/%m/%Y"),
            "time":time.strftime("%H:%M:%S"),
            "value": data,
        }

    def post(self, data):
        requests.post(self.firebase_URL + '/' + 'careband' + '/sensor.json', data=json.dumps(data))

if __name__ == "__main__":
    updatingFirebase = UpdatingFirebase()
    while(True):
        data = updatingFirebase.valueGenerator()
        data = updatingFirebase.dataParser(data)
        print(data)
        updatingFirebase.post(data)
        time.sleep(5)
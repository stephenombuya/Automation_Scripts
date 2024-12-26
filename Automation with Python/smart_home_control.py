import requests
import time

class SmartHomeController:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.smarthome.example.com/v1"
        self.headers = {"Authorization": f"Bearer {self.api_key}"}

    def get_devices(self):
        response = requests.get(f"{self.base_url}/devices", headers=self.headers)
        return response.json()

    def toggle_device(self, device_id, state):
        data = {"state": state}
        response = requests.post(f"{self.base_url}/devices/{device_id}/toggle", 
                                 headers=self.headers, json=data)
        return response.json()

    def run_evening_routine(self):
        devices = self.get_devices()
        for device in devices:
            if device['type'] == 'light' and device['room'] in ['living_room', 'kitchen']:
                print(f"Turning on {device['name']}")
                self.toggle_device(device['id'], 'on')
                time.sleep(1)  # Wait for 1 second between actions
            elif device['type'] == 'thermostat':
                print(f"Setting {device['name']} to 72°F")
                # Assume there's a method to set temperature
                # self.set_temperature(device['id'], 72)
                time.sleep(1)

# Example usage
api_key = "your_api_key_here"
controller = SmartHomeController(api_key)

print("Running evening routine...")
controller.run_evening_routine()
print("Evening routine completed.")

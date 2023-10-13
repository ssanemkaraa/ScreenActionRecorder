import json
import os
import time
import pyautogui
from pynput import mouse

class RecorderHelper:
    def __init__(self, file_name):
        self.base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        self.file_path = os.path.join(self.base_dir, "config", f"{file_name}.json")
        self.data = self.load_constants()

    def load_constants(self):
        if not os.path.isfile(self.file_path):
            with open(self.file_path, 'w') as new_file:
                new_file.write("{}")
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Constants file not found: {self.file_path}")
            return {}

    def get(self, key):
        return self.data.get(key)

    def on_click(self, x, y, button, pressed):
        if pressed and button == mouse.Button.left:
            click_data = {'x': x, 'y': y}
            self.data[f'click_{len(self.data) + 1}'] = click_data
            print(f"Coordinate saved: {x},{y}")
            with open(self.file_path, 'w') as file:
                json.dump(self.data, file)
        elif pressed and button == mouse.Button.middle:
            print("Recording stopped.")
            return False
    def start_record(self):
        with mouse.Listener(on_click=self.on_click) as listener:
            listener.join()

    def run_record(self):
        for i in range(1, len(self.data) + 1):
            click_data = self.get(f'click_{i}')
            if click_data:
                x, y = click_data['x'], click_data['y']
                pyautogui.click(x, y)
                time.sleep(1)

if __name__ == "__main__":
    recorder = RecorderHelper("abc")
    recorder.start_record()
    recorder.run_record()

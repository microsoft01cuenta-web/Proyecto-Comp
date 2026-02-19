import tkinter as tk
import requests

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Flask + Tkinter App")

        # Example: Create a label
        self.label = tk.Label(root, text='Welcome to the Tkinter GUI')
        self.label.pack()

        # Example: A button to fetch data from Flask backend
        self.fetch_button = tk.Button(root, text='Fetch Data', command=self.fetch_data)
        self.fetch_button.pack()

    def fetch_data(self):
        try:
            response = requests.get('http://your-flask-backend-url/api/data')
            data = response.json()
            # Process the data from Flask
            print(data)
        except requests.exceptions.RequestException as e:
            print(f'Error fetching data: {e}')

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
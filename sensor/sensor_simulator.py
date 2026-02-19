import random
import time

def simulate_iot_sensor_data(sensor_id, delay=1):
    while True:
        # Simulate sensor data
        temperature = round(random.uniform(20.0, 30.0), 2)  # Simulating temperature data
        humidity = round(random.uniform(30.0, 70.0), 2)      # Simulating humidity data
        pressure = round(random.uniform(950.0, 1050.0), 2)   # Simulating pressure data

        # Print or process the sensor data
        sensor_data = {
            'sensor_id': sensor_id,
            'temperature': temperature,
            'humidity': humidity,
            'pressure': pressure,
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
        }
        print(sensor_data)  # For demonstration, print the data

        time.sleep(delay)  # Delay for the next simulation

# Example usage:
# simulate_iot_sensor_data('sensor_1')  # You can call this function to start simulation

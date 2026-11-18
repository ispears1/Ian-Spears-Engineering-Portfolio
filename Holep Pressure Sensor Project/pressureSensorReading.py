import serial
import csv
import time
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import collections
import threading

#Initialize objects
ser = serial.Serial('COM4', 9600)
csvFile = open('pressureOutputs.csv', 'w', newline='')
writer = csv.writer(csvFile)
writer.writerow(['Timestamp', 'Elapsed Seconds', 'North', 'East', 'South', 'West'])

#Set up max size variable and containers for the graph
GRAPH_WINDOW_SIZE = 50
timeList = collections.deque(maxlen=GRAPH_WINDOW_SIZE)
northList = collections.deque(maxlen=GRAPH_WINDOW_SIZE)
eastList = collections.deque(maxlen=GRAPH_WINDOW_SIZE)
southList = collections.deque(maxlen=GRAPH_WINDOW_SIZE)
westList = collections.deque(maxlen=GRAPH_WINDOW_SIZE)

#Establish graph parameters
graph, axes = plt.subplots(figsize=(12, 8))
lines = {
    "NorthLine": axes.plot([],[], label="North", linewidth = 1.5)[0],
    "EastLine": axes.plot([],[], label="East", linewidth = 1.5)[0],
    "SouthLine": axes.plot([],[], label="South", linewidth = 1.5)[0],
    "WestLine": axes.plot([],[], label="West", linewidth = 1.5)[0]
}
axes.set_ylim(0, 3.3)
axes.set_xlabel("Time")
axes.set_ylabel("Voltage Reading")
axes.set_title("Live Pressure Sensor Reading")
axes.legend(loc="upper left")
axes.grid(True, alpha = 0.3)

#Define the background function that will collect data from the arduino
def get_arduino_data():
    while True:
        try:
            #Read and decode a line from the Arduino
            line = ser.readline().decode('utf-8').strip()
            if line:
                #Separate that line into a list, based on comma placement
                values = line.split(",")
                if len(values) == 4:

                    #Separate the list into individual readings, and print
                    north, east, south, west = [float(v) for v in values]
                    print(f"North: {north}  East: {east}  South: {south}  West: {west}")

                    #Log time and Pressure Sensor Readings to CSV
                    now = time.time()
                    timestamp = datetime.now().strftime('%H:%M:%S')
                    elapsed_seconds = now - start_time
                    writer.writerow([timestamp, round(elapsed_seconds, 2), north, east, south, west])
                    csvFile.flush()

                    timeList.append(round(elapsed_seconds, 2))
                    northList.append(north)
                    eastList.append(east)
                    southList.append(south)
                    westList.append(west)
        except (ValueError, UnicodeDecodeError):
            continue

#Define a function to be called to update the matplotlib animation
def update(_frame):
    if timeList:
        for key, dataList in zip(['NorthLine', 'EastLine', 'SouthLine', 'WestLine'], [northList, eastList, southList, westList]):
            lines[key].set_data(list(timeList), list(dataList))
        axes.set_xlim(min(timeList), max(timeList) + 0.1)
    return lines.values()

#Define a function to exit the program
def key_exit(event):
    if event.key == 'q':
        plt.close()

ani = animation.FuncAnimation(graph, update, interval=50, blit=True, cache_frame_data=False)
graph.canvas.mpl_connect('key_press_event', key_exit)

#Start the actual data collection here
start_time = time.time()
print("Reading sensors...")

#Start the daemon thread for the arduino collection to run in the background
thread = threading.Thread(target=get_arduino_data, daemon=True)
thread.start()

#Try, finally statement to execute the real time graphing, while the daemon function updates the graph data in the background
try:
    plt.tight_layout()
    plt.show()
finally:
    print("Data Collection Complete\nRemember to Rename Data File")
    csvFile.close()
    ser.close()
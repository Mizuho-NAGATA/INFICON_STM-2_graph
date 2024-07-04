# -------------------------------------------------------------
# Graphing INFICON STM-2 USB Thin Film Rate/Thickness Monitor Log Files: Displaying Average Rate in Graph Title
# This program was developed with the assistance of ChatGPT.
# Copyright (c) 2024 NAGATA Mizuho. Institute of Laser Engineering, Osaka University.
# Created on: 2024-05-15
# Last updated on: 2024-07-04
# -------------------------------------------------------------
import tkinter as tk
from tkinter import filedialog, simpledialog
import matplotlib.pyplot as plt
import numpy as np

def read_log_file(filename):
    time = []
    rate = []
    thick = []
    frequency = []

    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith('Time'):
                continue  # Skip header line
            if line.startswith('Stop Log'):
                break  # Stop reading at end of data

            data = line.split(',')
            if len(data) < 4:
                continue  # Skip invalid lines

            time.append(float(data[0].strip()))
            rate.append(float(data[1].strip()))
            thick.append(float(data[2].strip()))
            frequency.append(float(data[3].strip()))

    return time, rate, thick, frequency

def plot_graph(x, y, title, x_label, y_label, color):
    avg_rate = np.mean(y) if 'Rate' in title else None
    title = f'{title} (Average Rate: {avg_rate:.2f} \u212B/s)' if avg_rate else title
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, color=color)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

def plot_all_graphs_in_one_window(time, rate, thick, frequency, title):
    fig, axs = plt.subplots(3, 1, figsize=(10, 12))
    fig.suptitle(title, fontsize=16)

    avg_rate = np.mean(rate)
    axs[0].plot(time, rate, color='blue')
    axs[0].set_title(f'Rate vs Time (Average Rate: {avg_rate:.2f} \u212B/s)')
    axs[0].set_xlabel('Time')
    axs[0].set_ylabel('Rate')

    axs[1].plot(time, thick, color='green')
    axs[1].set_title('Thickness vs Time')
    axs[1].set_xlabel('Time')
    axs[1].set_ylabel('Thickness')

    axs[2].plot(time, frequency, color='red')
    axs[2].set_title('Frequency vs Time')
    axs[2].set_xlabel('Time')
    axs[2].set_ylabel('Frequency')

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()

def select_file_and_plot():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(title="Select log file", filetypes=[('Log Files', '*.log')])
    if file_path:
        time, rate, thick, frequency = read_log_file(file_path)

        # Allow users to enter a title.
        graph_title = simpledialog.askstring("Graph Title", "Enter graph title:")

        if graph_title:
            # Display each graph in a separate window
            plot_graph(time, rate, graph_title + ' (Rate vs Time)', 'Time', 'Rate', color='blue')
            plot_graph(time, thick, graph_title + ' (Thickness vs Time)', 'Time', 'Thickness', color='green')
            plot_graph(time, frequency, graph_title + ' (Frequency vs Time)', 'Time', 'Frequency', color='red')

            # Three graphs in one window
            plot_all_graphs_in_one_window(time, rate, thick, frequency, graph_title)

if __name__ == '__main__':
    select_file_and_plot()

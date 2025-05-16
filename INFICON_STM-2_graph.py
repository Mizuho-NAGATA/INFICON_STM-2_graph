# -------------------------------------------------------------
# Graphing INFICON STM-2 USB Thin Film Rate/Thickness Monitor Log Files: Displaying Average Rate in Graph Title
# This program was developed with the assistance of ChatGPT and Copilot.
# Copyright (c) 2024 NAGATA Mizuho. Institute of Laser Engineering, Osaka University.
# Created on: 2024-05-15
# Last updated on: 2025-05-16
# -------------------------------------------------------------

import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np

# 日本語フォントを指定
font_path = "C:/Windows/Fonts/BIZ-UDGothicR.ttc"
fp = FontProperties(fname=font_path)
plt.rcParams['font.family'] = fp.get_name()

def read_log_file(filename):
    try:
        time, rate, thick, frequency = [], [], [], []
        shutter_open_times = []
        shutter_open_rates = []

        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                if line.startswith('Time'):
                    continue  # Skip header line
                if line.startswith('Stop Log'):
                    break  # Stop reading at end of data

                data = line.split(',')
                if len(data) < 4:
                    continue  # Skip invalid lines

                t = float(data[0].strip())
                r = float(data[1].strip())
                thick.append(float(data[2].strip()))
                frequency.append(float(data[3].strip()))

                time.append(t)
                rate.append(r)

                # 蒸着レートが有意の値（例: 0.1 Å/s 以上）の場合、シャッターが開いていると判断
                if r > 0.1:
                    shutter_open_times.append(t)
                    shutter_open_rates.append(r)

        avg_deposition_rate = np.mean(shutter_open_rates) * 0.1  # nm/s に変換
        shutter_open_duration = max(shutter_open_times) - min(shutter_open_times) if shutter_open_times else 0

        return time, rate, thick, frequency, avg_deposition_rate, shutter_open_duration
    except Exception as e:
        messagebox.showerror("Error", f"Error reading log file: {e}")
        return None, None, None, None, None, None

def plot_graph(x, y, title, x_label, y_label, color):
    try:
        # 蒸着レートが有意の値（例: 0.1 Å/s 以上）の場合、シャッターが開いていると判断
        shutter_open_times = [x[i] for i in range(len(y)) if y[i] > 0.1]
        shutter_open_rates = [y[i] for i in range(len(y)) if y[i] > 0.1]

        avg_rate_nm = np.mean(shutter_open_rates) * 0.1 if shutter_open_rates else 0  # nm/s に変換
        open_duration = (max(shutter_open_times) - min(shutter_open_times)) if shutter_open_times else 0

        # グラフタイトルに平均蒸着レート(nm/s)とシャッター開時間(秒)を追加
        title = f'{title} (Avg Rate: {avg_rate_nm:.2f} nm/s, Open Duration: {open_duration:.1f} sec)'

        plt.figure(figsize=(8, 6))
        plt.plot(x, y, color=color)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", f"Error plotting graph: {e}")

def plot_all_graphs_in_one_window(time, rate, thick, frequency, title, avg_rate_nm, open_duration):
    try:
        fig, axs = plt.subplots(3, 1, figsize=(10, 12))
        graph_title = f"{title} (Avg Rate: {avg_rate_nm:.2f} nm/s, Shutter Open: {open_duration:.1f} sec)"
        fig.suptitle(graph_title, fontsize=16)

        axs[0].plot(time, rate, color='blue')
        axs[0].set_title('Rate vs Time')
        axs[0].set_xlabel('Time [sec]')
        axs[0].set_ylabel('Rate [Å/S]')

        axs[1].plot(time, thick, color='green')
        axs[1].set_title('Thickness vs Time')
        axs[1].set_xlabel('Time [sec]')
        axs[1].set_ylabel('Thickness [Å]')

        axs[2].plot(time, frequency, color='red')
        axs[2].set_title('Frequency vs Time')
        axs[2].set_xlabel('Time [sec]')
        axs[2].set_ylabel('Frequency [Hz]')

        plt.tight_layout(rect=[0, 0, 1, 0.96])
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", f"Error plotting all graphs: {e}")

def select_file_and_plot():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(title="Select log file", filetypes=[('Log Files', '*.log')])
    if file_path:
        time, rate, thick, frequency, avg_rate_nm, open_duration = read_log_file(file_path)

        if not time:  # Check if read_log_file encountered an error
            return

        graph_title = simpledialog.askstring("Graph Title", "Enter graph title:")

        if graph_title:
            # Display each graph in a separate window
            plot_graph(time, rate, graph_title + ' (Rate vs Time)', 'Time [sec]', 'Rate [Å/S]', color='blue')
            plot_graph(time, thick, graph_title + ' (Thickness vs Time)', 'Time [sec]', 'Thickness [Å]', color='green')
            plot_graph(time, frequency, graph_title + ' (Frequency vs Time)', 'Time [sec]', 'Frequency [Hz]', color='red')

            # Three graphs in one window
            plot_all_graphs_in_one_window(time, rate, thick, frequency, graph_title, avg_rate_nm, open_duration)

if __name__ == '__main__':
    select_file_and_plot()

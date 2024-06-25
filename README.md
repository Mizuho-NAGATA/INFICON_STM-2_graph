# INFICON STM-2 Log Graphing

This Python program is designed to graph the log files of the INFICON STM-2 USB Thin Film Rate/Thickness Monitor. One of the key features of this program is its ability to display the average rate in the graph title, providing a quick and easy way to understand the data.  
このPythonプログラムはINFICON STM-2 USB薄膜レート/膜厚モニターのログファイルをグラフ化するためにデザインされています。このプログラムの主な特徴の1つは、グラフタイトルに平均レートを表示する機能で、素早く簡単にデータを理解することができます。
![240624 Cu rate thick freq_](https://github.com/Mizuho-NAGATA/INFICON_STM-2_graph/assets/139824384/7514e6f2-7d17-48c8-8f14-cca761639884)
![240624 Cu rate_](https://github.com/Mizuho-NAGATA/INFICON_STM-2_graph/assets/139824384/24cf5922-6362-4954-b1f5-521b89c14790)
## Features

- Reads log files from the INFICON STM-2 USB Thin Film Rate/Thickness Monitor.
- Plots the rate, thickness, and frequency over time.
- Displays each graph in a separate window.
- Also combines all three graphs into one window for easy comparison.
- Calculates and displays the average rate in the graph title.

## Usage

1. Run the program: `python INFICON_STM-2_graph.py`
2. A dialog box will appear. Select the log file you want to graph.
3. Enter a title for the graph when prompted.
4. The program will display the graphs.

## Requirements

- Python 3
- tkinter
- matplotlib
- numpy

## License

This program was developed with the assistance of ChatGPT. Copyright (c) 2023 NAGATA Mizuho, 永田 みず穂, Institute of Laser Engineering, Osaka University.


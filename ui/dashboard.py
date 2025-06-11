import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class PredictiveMaintenanceDashboard:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Predictive Maintenance Dashboard")
        self.root.geometry("900x600")
        
        self.setup_ui()
    
    def setup_ui(self):
        # grid layout
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.rowconfigure(1, weight=1)

        # top left block: Sensor data
        sensor_frame = ttk.LabelFrame(self.root, text="Sensor Data", padding=10)
        sensor_frame.grid(row=0, column=0, columnspan=2, sticky='nsew', padx=10, pady=10)

        self.vibration_label = ttk.Label(sensor_frame, text="Vibration: --")
        self.vibration_label.pack(anchor='w', pady=5)

        self.temp_label = ttk.Label(sensor_frame, text="Temperature; --")
        self.temp_label.pack(anchor='w', pady=5)

        # top right block: Device details
        device_frame = ttk.LabelFrame(self.root, text="Device Details", padding=10)
        device_frame.grid(row=0, column=2, sticky='nsew', padx=10, pady=10)
        
        self.device_name_label = ttk.Label(device_frame, text="Device Name: --")
        self.device_name_label.pack(anchor='w', pady=5)
        
        self.device_id_label = ttk.Label(device_frame, text="Device ID: --")
        self.device_id_label.pack(anchor='w', pady=5)
        
        self.status_label = ttk.Label(device_frame, text="Status: --",
                                      font=('Helvetica', 12, 'bold'))
        self.status_label.pack(anchor='w', pady=5)

        # Bottom block: Plot area
        plot_frame = ttk.LabelFrame(self.root, text="graph", padding=10)
        plot_frame.grid(row=1, column=0, columnspan=2, sticky='nsew', padx=10, pady=10)

        self.fig, self.ax = plt.subplots(figsize=(7, 3))
        self.ax.set_title("palceholder")
        self.ax.set_xlabel("Time Step")
        self.ax.set_ylabel("Vibration")
        self.canvas = FigureCanvasTkAgg(self.fig, master=plot_frame)
        self.canvas.get_tk_widget().pack(fill='both', expand=True)

        # health block
        health_frame = ttk.LabelFrame(self.root, text="Health Indicator", padding=10)
        health_frame.grid(row=1, column=2, sticky='nsew', padx=10, pady=10)

        self.fig, self.ax = plt.subplots(figsize=(5, 3))
        self.ax.set_title("palceholder")
        self.ax.set_xlabel("Time Step")
        self.ax.set_ylabel("Vibration")
        self.canvas = FigureCanvasTkAgg(self.fig, master=health_frame)
        self.canvas.get_tk_widget().pack(fill='both', expand=True)

        button_frame = ttk.Frame(self.root)
        button_frame.grid(row=2, column=0, columnspan=2, pady=10)
        
        self.start_btn = ttk.Button(button_frame, text="Start Monitoring")
        self.start_btn.pack(side='left', padx=10)
        
        self.stop_btn = ttk.Button(button_frame, text="Stop Monitoring")
        self.stop_btn.pack(side='left', padx=10)
    
    def run(self):
        self.root.mainloop()

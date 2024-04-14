import tkinter
import os
import csv
from tkinter import ttk
from tkinter import messagebox
import sv_ttk
import re
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.cm as cm

# Defining global variables
script_dir = os.path.dirname(os.path.abspath(__file__))

def open_file(filename):
    if os.path.isfile(filename):
        os.system(f'start {filename}')
    else:
        tkinter.messagebox.showerror("Error", f"File {filename} not found")

def find_least_cycles():
    csv_dest_path = os.path.join(script_dir, 'combined_benchmarks/combined_csv_benchmarks.csv')
    try:
        with open(csv_dest_path, 'r') as file:
            reader = csv.reader(file)
            min_value = float('inf')
            min_algorithm = None
            min_variant = None
            process_lines = False
            for row in reader:
                if not row:  # Skip empty rows
                    continue
                if row[0] == "Speed Evaluation":
                    process_lines = True
                    continue
                if row[0] == "Memory Evaluation":
                    break
                if process_lines:
                    try:
                        numbers = list(map(int, row[2:]))
                        if len(numbers) != 9:
                            continue
                        total_row_value = sum(numbers)
                        if total_row_value < min_value:
                            min_value = total_row_value
                            min_algorithm = row[0]
                            min_variant = row[1]
                    except ValueError:
                        continue
            # Remove text between parentheses
            min_algorithm = re.sub(r'\(.*\)', '', min_algorithm)
            return f"{min_algorithm.strip()} - {min_variant.strip()}"
    except:
        return "Error - No Schemes Found"
    
def find_least_memory():
    csv_dest_path = os.path.join(script_dir, 'combined_benchmarks/combined_csv_benchmarks.csv')
    try:
        with open(csv_dest_path, 'r') as file:
            reader = csv.reader(file)
            min_value = float('inf')
            min_algorithm = None
            min_variant = None
            process_lines = False
            for row in reader:
                if not row:  # Skip empty rows
                    continue
                if row[0] == "Speed Evaluation":
                    continue
                if row[0] == "Memory Evaluation":
                    process_lines = True
                    continue
                if row[0] == "Hashing Evaluation":
                    break
                if process_lines:
                    try:
                        numbers = list(map(int, row[2:5]))  # Only consider the first 3 numbers
                        total_memory = sum(numbers)
                        if total_memory < min_value:
                            min_value = total_memory
                            min_algorithm = row[0]
                            min_variant = row[1]
                    except ValueError:
                        continue
            # Remove text between parentheses
            if min_algorithm is not None:
                min_algorithm = re.sub(r'\(.*\)', '', min_algorithm)
                return f"{min_algorithm.strip()} - {min_variant.strip()}"
            else:
                return "No data available"
    except:
        return "Error - No Schemes Found"


def find_least_hashing():
    csv_dest_path = os.path.join(script_dir, 'combined_benchmarks/combined_csv_benchmarks.csv')
    try:
        with open(csv_dest_path, 'r') as file:
            reader = csv.reader(file)
            min_value = float('inf')
            min_algorithm = None
            min_variant = None
            process_lines = False
            for row in reader:
                if not row:  # Skip empty rows
                    continue
                if row[0] == "Memory Evaluation":
                    continue
                if row[0] == "Hashing Evaluation":
                    process_lines = True
                    continue
                if row[0] == "Size Evaluation":
                    break
                if process_lines:
                    try:
                        numbers = list(map(float, row[2:5]))  # Only consider the first 3 numbers
                        total_hashing = sum(numbers)
                        if total_hashing < min_value:
                            min_value = total_hashing
                            min_algorithm = row[0]
                            min_variant = row[1]
                    except ValueError:
                        continue
            # Remove text between parentheses
            if min_algorithm is not None:
                min_algorithm = re.sub(r'\(.*\)', '', min_algorithm)
                return f"{min_algorithm.strip()} - {min_variant.strip()}"
            else:
                return "No data available"
    except:
        return "Error - No Schemes Found"


def find_smallest_size():
    csv_dest_path = os.path.join(script_dir, 'combined_benchmarks/combined_csv_benchmarks.csv')
    try:
        with open(csv_dest_path, 'r') as file:
            reader = csv.reader(file)
            min_value = float('inf')
            min_algorithm = None
            min_variant = None
            process_lines = False
            for row in reader:
                if not row:  # Skip empty rows
                    continue
                if row[0] == "Size Evaluation":
                    process_lines = True
                    continue
                if process_lines:
                    try:
                        numbers = list(map(float, row[2:6]))  # Only consider the first 4 numbers
                        total_size = sum(numbers)
                        if total_size < min_value:
                            min_value = total_size
                            min_algorithm = row[0]
                            min_variant = row[1]
                    except ValueError:
                        continue
            # Remove text between parentheses
            if min_algorithm is not None:
                min_algorithm = re.sub(r'\(.*\)', '', min_algorithm)
                return f"{min_algorithm.strip()} - {min_variant.strip()}"
            else:
                return "No data available"
    except:
        return "Error - No Schemes Found"

        
def plot_cycles():
    csv_dest_path = os.path.join(script_dir, 'combined_benchmarks/combined_csv_benchmarks.csv')
    data = {}
    try:  
        with open(csv_dest_path, 'r') as file:
            reader = csv.reader(file)
            process_lines = False
            for row in reader:
                if not row:  # Skip empty rows
                    continue
                if row[0] == "Speed Evaluation":
                    process_lines = True
                    continue
                if row[0] == "Memory Evaluation":
                    break
                if process_lines:
                    try:
                        numbers = list(map(int, row[2:]))
                        if len(numbers) != 9:
                            continue
                        key_gen = numbers[0]
                        encapsulation = numbers[3]
                        decapsulation = numbers[6]
                        algorithm = re.sub(r'\(.*\)', '', row[0]).strip()
                        variant = row[1].strip()
                        data[f"{algorithm} - {variant}"] = [key_gen, encapsulation, decapsulation]
                    except ValueError:
                        continue

        # Create a new Toplevel window
        chart_window = tkinter.Toplevel()
        chart_window.title("Speed Evaluation Bar Chart")
        chart_window.iconbitmap(script_dir + '/resources/benchmark_icon.ico')
        chart_window.geometry("1200x500")

        # Create a new figure and a subplot
        fig = Figure(figsize=(12, 6), dpi=100)
        ax = fig.add_subplot(111)

        # Create stacked bar chart
        labels = list(data.keys())
        key_gen = [data[label][0] for label in labels]
        encapsulation = [data[label][1] for label in labels]
        decapsulation = [data[label][2] for label in labels]

        ax.barh(labels, key_gen, label='Key Generation')
        ax.barh(labels, encapsulation, left=key_gen, label='Encapsulation')
        ax.barh(labels, decapsulation, left=[i+j for i,j in zip(key_gen, encapsulation)], label='Decapsulation')

        ax.set_xlabel('Cycles Used (x10^6)')
        ax.set_title('Average Cycles for Key Generation, Encapsulation, and Decapsulation')
        ax.legend()

        # Set y-ticks
        ax.set_yticks(range(len(labels)))
        ax.set_yticklabels(labels)

        # Add horizontal grid lines
        ax.grid(axis='x')

        # Adjust the layout
        fig.tight_layout(pad = 3)

        # Add the figure to the window
        canvas = FigureCanvasTkAgg(fig, master=chart_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tkinter.BOTH, expand=1)
    except:
        tkinter.messagebox.showerror("Error", "Error - No Schemes Found")


def plot_memory():
    csv_dest_path = os.path.join(script_dir, 'combined_benchmarks/combined_csv_benchmarks.csv')
    data = {}
    try:
        with open(csv_dest_path, 'r') as file:
            reader = csv.reader(file)
            process_lines = False
            for row in reader:
                if not row:  # Skip empty rows
                    continue
                if row[0] == "Memory Evaluation":
                    process_lines = True
                    continue
                if row[0] == "Hashing Evaluation":
                    break
                if process_lines:
                    try:
                        numbers = list(map(int, row[2:5]))
                        if len(numbers) != 3:
                            continue
                        key_gen = numbers[0]
                        encapsulation = numbers[1]
                        decapsulation = numbers[2]
                        algorithm = re.sub(r'\(.*\)', '', row[0]).strip()
                        variant = row[1].strip()
                        data[f"{algorithm} - {variant}"] = [key_gen, encapsulation, decapsulation]
                    except ValueError:
                        continue

        # Create a new Toplevel window
        chart_window = tkinter.Toplevel()
        chart_window.title("Memory Evaluation Bar Chart")
        chart_window.geometry("1200x500")
        chart_window.iconbitmap(script_dir + '/resources/benchmark_icon.ico')

        # Create a new figure and a subplot
        fig = Figure(figsize=(12, 6), dpi=100)
        ax = fig.add_subplot(111)

        # Create stacked bar chart
        labels = list(data.keys())
        key_gen = [data[label][0] for label in labels]
        encapsulation = [data[label][1] for label in labels]
        decapsulation = [data[label][2] for label in labels]

        ax.barh(labels, key_gen, label='Key Generation')
        ax.barh(labels, encapsulation, left=key_gen, label='Encapsulation')
        ax.barh(labels, decapsulation, left=[i+j for i,j in zip(key_gen, encapsulation)], label='Decapsulation')

        ax.set_xlabel('Memory Usage (bytes)')
        ax.set_title('Average Memory Usage for Key Generation, Encapsulation, and Decapsulation')
        ax.legend()

        # Set y-ticks
        ax.set_yticks(range(len(labels)))
        ax.set_yticklabels(labels)

        # Add horizontal grid lines
        ax.grid(axis='x')

        # Adjust the layout
        fig.tight_layout(pad = 3)

        # Add the figure to the window
        canvas = FigureCanvasTkAgg(fig, master=chart_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tkinter.BOTH, expand=1)
    except:
        tkinter.messagebox.showerror("Error", "Error - No Schemes Found")

def plot_size():
    csv_dest_path = os.path.join(script_dir, 'combined_benchmarks/combined_csv_benchmarks.csv')
    data = {}
    try:
        with open(csv_dest_path, 'r') as file:
            reader = csv.reader(file)
            process_lines = False
            for row in reader:
                if not row:  # Skip empty rows
                    continue
                if row[0] == "Size Evaluation":
                    process_lines = True
                    continue
                if process_lines:
                    try:
                        numbers = list(map(float, row[2:6]))  # Only consider the first 4 numbers
                        total_size = sum(numbers)
                        algorithm = re.sub(r'\(.*\)', '', row[0]).strip()
                        variant = row[1].strip()
                        data[f"{algorithm} - {variant}"] = total_size
                    except ValueError:
                        continue

        # Create a new Toplevel window
        chart_window = tkinter.Toplevel()
        chart_window.title("Size Evaluation Bar Chart")
        chart_window.geometry("1200x500")
        chart_window.iconbitmap(script_dir + '/resources/benchmark_icon.ico')

        # Create a new figure and a subplot
        fig = Figure(figsize=(12, 6), dpi=100)
        ax = fig.add_subplot(111)

        # Create bar chart
        labels = list(data.keys())
        sizes = [data[label] for label in labels]

        # Create a color map
        colors = cm.rainbow(np.linspace(0, 1, len(labels)//3))

        # Repeat each color 3 times
        colors = np.repeat(colors, 3, axis=0)

        ax.barh(labels, sizes, color=colors)
        ax.set_xlabel('Implementation size (bytes)')
        ax.set_title('Size Evaluation for each Algorithm and Variant')

        # Set y-ticks
        ax.set_yticks(range(len(labels)))
        ax.set_yticklabels(labels)

        # Add horizontal grid lines
        ax.grid(axis='x')

        # Adjust the layout
        fig.tight_layout(pad = 3)

        # Add the figure to the window
        canvas = FigureCanvasTkAgg(fig, master=chart_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tkinter.BOTH, expand=1)
    except:
        tkinter.messagebox.showerror("Error", "Error - No Schemes Found")

def plot_hashing():
    csv_dest_path = os.path.join(script_dir, 'combined_benchmarks/combined_csv_benchmarks.csv')
    data = {}
    try:
        with open(csv_dest_path, 'r') as file:
            reader = csv.reader(file)
            process_lines = False
            for row in reader:
                if not row:  # Skip empty rows
                    continue
                if row[0] == "Hashing Evaluation":
                    process_lines = True
                    continue
                if row[0] == "Size Evaluation":
                    break
                if process_lines:
                    try:
                        numbers = list(map(float, row[2:5]))  # Only consider the first 3 numbers
                        algorithm = re.sub(r'\(.*\)', '', row[0]).strip()
                        variant = row[1].strip()
                        data[f"{algorithm} - {variant}"] = numbers
                    except ValueError:
                        continue

        # Create a new Toplevel window
        chart_window = tkinter.Toplevel()
        chart_window.title("Hashing Evaluation Bar Chart")
        chart_window.geometry("1200x500")
        chart_window.iconbitmap(script_dir + '/resources/benchmark_icon.ico')

        # Create a new figure and a subplot
        fig = Figure(figsize=(12, 6), dpi=100)
        ax = fig.add_subplot(111)

        # Create stacked bar chart
        labels = list(data.keys())
        key_gen = [data[label][0] for label in labels]
        encapsulation = [data[label][1] for label in labels]
        decapsulation = [data[label][2] for label in labels]

        ax.barh(labels, key_gen, label='Key Generation')
        ax.barh(labels, encapsulation, left=key_gen, label='Encapsulation')
        ax.barh(labels, decapsulation, left=[i+j for i,j in zip(key_gen, encapsulation)], label='Decapsulation')

        ax.set_xlabel('Cumulative Percentage of Clock Cycles spent in Hashing')
        ax.set_title('Proportion of Clock Cycles spent in Hashing for each Algorithm and Variant')
        ax.set_yticks(range(len(labels)))
        ax.set_yticklabels(labels)

        # Add horizontal grid lines
        ax.grid(axis='x')

        # Adjust the layout
        fig.tight_layout(pad = 3)

        # Add the legend
        ax.legend()

        # Add the figure to the window
        canvas = FigureCanvasTkAgg(fig, master=chart_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tkinter.BOTH, expand=1)
    except:
        tkinter.messagebox.showerror("Error", "Error - No Schemes Found")

def open_chart_window(root):
    chart_window = tkinter.Toplevel(root)
    chart_window.title("Bar Charts")
    chart_window.geometry("500x500")
    chart_window.iconbitmap(script_dir + '/resources/benchmark_icon.ico')

    # Create a frame to hold the buttons
    frame = tkinter.Frame(chart_window)
    frame.pack(expand=True)

    # Create the buttons and add them to the frame
    button1 = ttk.Button(frame, text="Speed Evaluation" , command=plot_cycles)
    button1.grid(row=0, column=0, padx=5, pady=5, sticky='ew')

    button2 = ttk.Button(frame, text="Memory Evaluation", command=plot_memory)
    button2.grid(row=0, column=1, padx=5, pady=5, sticky='ew')

    button3 = ttk.Button(frame, text="Hash Proportion", command=plot_hashing)
    button3.grid(row=1, column=0, padx=5, pady=5, sticky='ew')

    button4 = ttk.Button(frame, text="Size Evaluation", command=plot_size)
    button4.grid(row=1, column=1, padx=5, pady=5, sticky='ew')

    # Set the relative sizes of the grid cells
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_rowconfigure(1, weight=1)

    # Center the frame in the window
    frame.place(relx=0.5, rely=0.5, anchor='center')

def open_benchmark_window(root):
    # Check if the window is already open
    if not hasattr(open_benchmark_window, "window_open") or not open_benchmark_window.window_open:
        # Create a new Toplevel window
        benchmark_window = tkinter.Toplevel(root)

        # Set the size and title of the window
        benchmark_window.geometry("900x600")
        benchmark_window.title("Kyber with Ascon Benchmark Viewer")
        benchmark_window.iconbitmap(script_dir + '/resources/benchmark_icon.ico')

        # Apply the same style and theme
        sv_ttk.use_dark_theme()
        style = ttk.Style()
        style.configure("TLabel", font=("Helvetica", 18))
        style.configure("TButton", font=("Helvetica", 16), padding=20)

        label = ttk.Label(benchmark_window, text="View Benchmarks", font=("Helvetica", 30))
        label.pack(pady=70)

        csv_dest_path = os.path.join(script_dir, 'combined_benchmarks/combined_csv_benchmarks.csv')
        md_dest_path = os.path.join(script_dir, 'combined_benchmarks/combined_md_benchmarks.md')
        
        # Create the buttons
        button1 = ttk.Button(benchmark_window, text="View raw CSV data", command=lambda: open_file(csv_dest_path))
        button2 = ttk.Button(benchmark_window, text="View bar charts", command=lambda: open_chart_window(root))
        button3 = ttk.Button(benchmark_window, text="View raw MD data", command=lambda: open_file(md_dest_path))

        # Place the buttons
        button1.place(relx=0.2, rely=0.25, relwidth=0.3, anchor='n')
        button2.place(relx=0.5, rely=0.25, relwidth=0.25, anchor='n')
        button3.place(relx=0.8, rely=0.25, relwidth=0.3, anchor='n')

        label5 = ttk.Label(benchmark_window, text="Brief summary of results", font=("Helvetica", 20, 'underline'))
        label5.place(relx=0.5, rely=0.5, anchor='center')

        label1 = ttk.Label(benchmark_window, text="Least clock cycles used: ")
        label1.place(relx=0.5, rely=0.6, anchor='center')
        label1.config(text=f"Least clock cycles used: {find_least_cycles()}")

        label2 = ttk.Label(benchmark_window, text="Least memory used: ")
        label2.place(relx=0.5, rely=0.7, anchor='center')
        label2.config(text=f"Least memory used: {find_least_memory()}")

        label3 = ttk.Label(benchmark_window, text="Lowest proportion of clock cycles spent in hashing:")
        label3.place(relx=0.5, rely=0.8, anchor='center')
        label3.config(text=f"Lowest proportion of clock cycles spent in hashing: {find_least_hashing()}")

        label4 = ttk.Label(benchmark_window, text="Smallest size: ")
        label4.place(relx=0.5, rely=0.9, anchor='center')
        label4.config(text=f"Smallest size: {find_smallest_size()}")

        # Set window_open to True
        open_benchmark_window.window_open = True

        # Set window_open to False when the window is destroyed
        benchmark_window.bind("<Destroy>", lambda e: setattr(open_benchmark_window, "window_open", False))
import tkinter
import webbrowser
import os
from tkinter import ttk
import sv_ttk
from benchmark_importer import open_import_window
from benchmark_display import open_benchmark_window

# Defining global variables
script_dir = os.path.dirname(os.path.abspath(__file__))

# Create the main window
root = tkinter.Tk()
root.geometry("800x600")
root.title("Kyber with Ascon Benchmark Viewer")
root.iconbitmap(script_dir + '/resources/benchmark_icon.ico')
sv_ttk.use_dark_theme()

# Configure the style of the widgets
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 18))
style.configure("TButton", font=("Helvetica", 16), padding=20)

def show_main_screen():
    # Destroy the current widgets
    for widget in root.winfo_children():
        widget.destroy()

    # Create widgets for the main screen
    main_screen_label = ttk.Label(root, text="Kyber with Ascon Hash Benchmark Viewer", font=("Helvetica", 30), wraplength=600, anchor='center', justify='center')    
    main_screen_label.pack(pady=70)

    # Create the buttons
    import_button = ttk.Button(root, text="Import/Refresh Benchmarks", command=lambda: open_import_window(root))
    import_button.pack(side="top", pady=20)  # Add some vertical padding between the buttons

    view_button = ttk.Button(root, text="View Benchmarks", command=lambda: open_benchmark_window(root))    
    view_button.pack(side="top", pady=10)  # Add some vertical padding between the buttons

    # Create a label with the webpage URL
    info_link = ttk.Label(root, text="Project README", cursor="hand2", font=("Helvetica", 15, "italic"))    
    info_link.pack(side="left", anchor='sw')  # Place it in the bottom left corner of the window
    info_link.bind("<Button-1>", open_webpage)  # Bind the function to the label

def open_webpage(event):
    webbrowser.open_new_tab('https://gitlab.eeecs.qub.ac.uk/40284751/a-light-weight-quantum-resistant-public-key-encryption-scheme-on-an-arm-processor/-/blob/main/README.md?ref_type=heads')

# Initialize window_open to False
open_import_window.window_open = False

show_main_screen()

root.mainloop()
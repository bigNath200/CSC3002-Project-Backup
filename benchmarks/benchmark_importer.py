import tkinter
import csv
import os
from collections import defaultdict
from datetime import datetime
from tkinter import ttk
import sv_ttk
import json

# Defining global variables
script_dir = os.path.dirname(os.path.abspath(__file__))

def open_import_window(root):
    # List of algorithms
    algorithms = ['kyber512reference', 'kyber512speed', 'kyber512small', 'kyber512lowsize', 'kyber512bi32speed', 'kyber512bi32small']
    # Check if the window is already open
    if hasattr(open_import_window, "window_open") and open_import_window.window_open:
        return
    open_import_window.window_open = True

    # Create a new window
    import_window = tkinter.Toplevel(root)
    import_window.geometry("800x600")
    import_window.title("Kyber with Ascon Hash Benchmark Viewer")
    import_window.iconbitmap(script_dir + '/resources/benchmark_icon.ico')
    sv_ttk.use_dark_theme(import_window)

    # Read the timestamp from a file
    try:
        with open(os.path.join(script_dir, "resources/timestamp.txt"), "r") as file:
            timestamp = file.read().strip()
    except FileNotFoundError:
        timestamp = "Never"

    # Create a label with the timestamp
    timestamp_label = ttk.Label(import_window, text="Last refreshed: " + timestamp, font=("Helvetica", 30), wraplength=400, anchor='center', justify='center')
    timestamp_label.pack(pady=70)

    # Create a table with the algorithm names and status
    status_table = ttk.Treeview(import_window, columns=("Algorithm name", "CSV Status", "MD Status"), show="headings")
    status_table.heading("Algorithm name", text="Algorithm name")
    status_table.heading("CSV Status", text="CSV Status")
    status_table.heading("MD Status", text="MD Status")


    # Place the table in the window
    status_table.place(relx=0.5, rely=0.5, anchor='center', relwidth=0.8)
    for algorithm in algorithms:
            status_table.insert("", "end", values=(algorithm, "", ""))
    try:
        with open(os.path.join(script_dir,"resources/status_table_values.json"), 'r') as f:
            status_dict = json.load(f)
    except FileNotFoundError:
        for algorithm in algorithms:
            status_table.insert("", "end", values=(algorithm, "Not imported", "Not imported"))
    
    for child in status_table.get_children():
        algorithm = status_table.item(child)["values"][0]
        if algorithm in status_dict:
            status_table.set(child, "CSV Status", status_dict[algorithm]["csv"])
            status_table.set(child, "MD Status", status_dict[algorithm]["md"])

    
    def refresh_benchmarks():
        # Destination files
        csv_dest_path = os.path.join(script_dir, 'combined_benchmarks/combined_csv_benchmarks.csv')
        md_dest_path = os.path.join(script_dir, 'combined_benchmarks/combined_md_benchmarks.md')

        # Initialize the status dictionary
        status_dict = {algorithm: {"csv": "Error importing", "md": "Error importing"} for algorithm in algorithms}


        # Dictionary to store rows by type
        rows_by_type = defaultdict(list)

        # Initialize a dictionary to store the combined markdown tables
        combined_tables = {
            "# Speed Evaluation": ["| scheme | implementation | key generation [cycles] | encapsulation [cycles] | decapsulation [cycles] |", "| ------ | -------------- | ----------------------- | ---------------------- | ---------------------- |"],
            "# Memory Evaluation": ["| Scheme | Implementation | Key Generation [bytes] | Encapsulation [bytes] | Decapsulation [bytes] |", "| ------ | -------------- | ---------------------- | --------------------- | --------------------- |"],
            "# Hashing Evaluation": ["| Scheme | Implementation | Key Generation [%] | Encapsulation [%] | Decapsulation [%] |", "| ------ | -------------- | ------------------ | ----------------- | ----------------- |"],
            "# Size Evaluation": ["| Scheme | Implementation | .text [bytes] | .data [bytes] | .bss [bytes] | Total [bytes] |", "| ------ | -------------- | ------------- | ------------- | ------------ | ------------- |"]
        }

        # Iterate over the algorithms
        for algorithm in algorithms:
            # Construct the source file paths
            csv_source_path = os.path.join(script_dir, '../' + algorithm + '/results.csv')
            md_source_path = os.path.join(script_dir, '../' + algorithm + '/results.md')

            try:
                # Open the CSV source file
                with open(csv_source_path, 'r') as csv_source_file:
                    reader = csv.reader(csv_source_file)

                    # Current type
                    current_type = None

                    # Read the rows
                    for row in reader:
                        if row and row[0].startswith('kyber512'):
                            # Append the algorithm name after "kyber512"
                            row[0] = row[0] + " " + algorithm.split('kyber512')[1]
                            rows_by_type[current_type].append(row)
                        elif row and row[0] in ['Speed Evaluation', 'Memory Evaluation', 'Hashing Evaluation', 'Size Evaluation']:
                            # Update the current type
                            current_type = row[0]
                # If no exceptions were raised, update the CSV status to "Imported"
                status_dict[algorithm]["csv"] = "Imported"
            except Exception as e:
                print(f"Error importing CSV for {algorithm}: {e}")

            try:
                # Open the markdown source file
                with open(md_source_path, 'r') as md_source_file:
                    # Current type
                    current_type = None

                    # Read the lines
                    for line in md_source_file:
                        if line.startswith('# '):
                            current_type = line.strip()
                        elif line.startswith('| kyber512'):
                            # Append the algorithm name after "kyber512"
                            line = line.replace('| kyber512', '| kyber512 ' + algorithm.split('kyber512')[1])
                            combined_tables[current_type].append(line.strip())
                # If no exceptions were raised, update the MD status to "Imported"
                status_dict[algorithm]["md"] = "Imported"
            except Exception as e:
                print(f"Error importing MD for {algorithm}: {e}")

        # Combine the markdown tables
        for evaluation_type, lines in combined_tables.items():
            combined_tables[evaluation_type] = '\n'.join(lines)

        # Write the combined markdown tables to the destination file
        with open(md_dest_path, 'w') as md_dest_file:
            for evaluation_type, table in combined_tables.items():
                md_dest_file.write(evaluation_type + '\n')
                md_dest_file.write(table + '\n\n')

        # Write the combined CSV rows to the destination file
        with open(csv_dest_path, 'w', newline='') as csv_dest_file:
            writer = csv.writer(csv_dest_file)
            for evaluation_type, rows in rows_by_type.items():
                writer.writerow([evaluation_type])
                writer.writerows(rows)
                writer.writerow([])
        # Update the table in the GUI
        for child in status_table.get_children():
            # Get the algorithm name from the item
            algorithm = status_table.item(child)["values"][0]

            # If the algorithm is in the status dictionary, update the CSV and MD statuses
            if algorithm in status_dict:
                status_table.set(child, "CSV Status", status_dict[algorithm]["csv"])
                status_table.set(child, "MD Status", status_dict[algorithm]["md"])

                # Write the status_dict to a file
        with open(os.path.join(script_dir,"resources/status_table_values.json"), 'w') as f:
            json.dump(status_dict, f)

        # Update the timestamp
        with open(os.path.join(script_dir, "resources/timestamp.txt"), "w") as file:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            file.write(timestamp)
        # Update the label
        timestamp_label.config(text="Last refreshed: " + timestamp)

    # Create a button to refresh the benchmarks
    refresh_button = ttk.Button(import_window, text="Import/Refresh Benchmarks", command=refresh_benchmarks)
    refresh_button.place(relx=0.5, rely=0.8, anchor='center')

    # Update closed window variable
    def on_close():
        open_import_window.window_open = False
        import_window.destroy()

    import_window.protocol("WM_DELETE_WINDOW", on_close)

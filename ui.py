import tkinter as tk
from tkinter import messagebox
from process import Process  # Assuming you have defined this elsewhere
from fcfs import fcfs_scheduling  # Assuming you have defined this elsewhere
from sjn import sjn_scheduling  # Assuming you have defined this elsewhere
from priority import priority_scheduling  # Assuming you have defined this elsewhere
from round_robin import round_robin_scheduling  # Assuming you have defined this elsewhere
from utils import print_processes, calculate_avg_times  # Assuming you have defined this elsewhere

class CPUSchedulerUI:
    def __init__(self, root):
        self.root = root
        self.root.title("CPU Scheduling Algorithms")

        self.processes = []

        # Configure the window's background color
        self.root.configure(bg='#99e6e6')

        # Make the window resizable and maximized
        self.root.state('zoomed')
        self.root.resizable(True, True)

        # UI elements
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="PID", bg='#99e6e6').grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self.root, text="Arrival Time", bg='#99e6e6').grid(row=0, column=1, padx=5, pady=5)
        tk.Label(self.root, text="Burst Time", bg='#99e6e6').grid(row=0, column=2, padx=5, pady=5)
        tk.Label(self.root, text="Priority", bg='#99e6e6').grid(row=0, column=3, padx=5, pady=5)

        self.pid_entry = tk.Entry(self.root)
        self.pid_entry.grid(row=1, column=0, padx=5, pady=5, sticky='ew')

        self.arrival_entry = tk.Entry(self.root)
        self.arrival_entry.grid(row=1, column=1, padx=5, pady=5, sticky='ew')

        self.burst_entry = tk.Entry(self.root)
        self.burst_entry.grid(row=1, column=2, padx=5, pady=5, sticky='ew')

        self.priority_entry = tk.Entry(self.root)
        self.priority_entry.grid(row=1, column=3, padx=5, pady=5, sticky='ew')

        self.add_button = tk.Button(self.root, text="Add Process", command=self.add_process, bg='#4ddbff')
        self.add_button.grid(row=1, column=4, padx=5, pady=5, sticky='ew')

        self.fcfs_button = tk.Button(self.root, text="FCFS", command=self.run_fcfs, bg='#4ddbff')
        self.fcfs_button.grid(row=2, column=0, padx=5, pady=5, sticky='ew')

        self.sjn_button = tk.Button(self.root, text="SJN", command=self.run_sjn, bg='#4ddbff')
        self.sjn_button.grid(row=2, column=1, padx=5, pady=5, sticky='ew')

        self.priority_button = tk.Button(self.root, text="Priority", command=self.run_priority, bg='#4ddbff')
        self.priority_button.grid(row=2, column=2, padx=5, pady=5, sticky='ew')

        self.rr_button = tk.Button(self.root, text="Round Robin", command=self.run_rr, bg='#4ddbff')
        self.rr_button.grid(row=2, column=3, padx=5, pady=5, sticky='ew')

        tk.Label(self.root, text="Time Quantum for RR:", bg='#99e6e6').grid(row=3, column=0, padx=5, pady=5, sticky='w')
        self.quantum_entry = tk.Entry(self.root)
        self.quantum_entry.grid(row=3, column=1, padx=5, pady=5, sticky='ew')

        self.output_text = tk.Text(self.root, height=10, width=80)
        self.output_text.grid(row=4, column=0, columnspan=5, padx=5, pady=5, sticky='nsew')

        # Configure grid resizing
        for i in range(5):
            self.root.grid_columnconfigure(i, weight=1)
        self.root.grid_rowconfigure(4, weight=1)

    def add_process(self):
        try:
            pid = int(self.pid_entry.get())
            arrival_time = int(self.arrival_entry.get())
            burst_time = int(self.burst_entry.get())
            priority = int(self.priority_entry.get())
            process = Process(pid, arrival_time, burst_time, priority)
            self.processes.append(process)
            self.output_text.insert(tk.END, f"Added: {process}\n")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid integers for all fields.")

    def run_fcfs(self):
        self.run_algorithm(fcfs_scheduling)

    def run_sjn(self):
        self.run_algorithm(sjn_scheduling)

    def run_priority(self):
        self.run_algorithm(priority_scheduling)

    def run_rr(self):
        try:
            time_quantum = int(self.quantum_entry.get())
            self.run_algorithm(round_robin_scheduling, time_quantum)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid integer for time quantum.")

    def run_algorithm(self, algorithm, *args):
        if not self.processes:
            messagebox.showerror("No Processes", "Please add some processes first.")
            return
        processes_copy = [Process(p.pid, p.arrival_time, p.burst_time, p.priority) for p in self.processes]
        result = algorithm(processes_copy, *args) if args else algorithm(processes_copy)
        self.output_text.insert(tk.END, f"Results for {algorithm.__name__}:\n")
        for process in result:
            self.output_text.insert(tk.END, f"{process}\n")
        self.output_text.insert(tk.END, "\n")
        calculate_avg_times(result)

def main():
    root = tk.Tk()
    app = CPUSchedulerUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

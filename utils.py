# utils.py

def print_processes(processes):
    for process in processes:
        print(process)

def calculate_avg_times(processes):
    if len(processes) == 0:
        print("No processes to calculate average times.")
        return

    total_waiting_time = sum(p.waiting_time for p in processes)
    total_turnaround_time = sum(p.turnaround_time for p in processes)
    avg_waiting_time = total_waiting_time / len(processes)
    avg_turnaround_time = total_turnaround_time / len(processes)
    print(f"Average Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")

# main.py

import sys
from ui import main as ui_main
from process import Process
from fcfs import fcfs_scheduling
from sjn import sjn_scheduling
from priority import priority_scheduling
from round_robin import round_robin_scheduling
from utils import print_processes, calculate_avg_times

def cli_main():
    processes = [
        Process(pid=1, arrival_time=0, burst_time=5, priority=2),
        Process(pid=2, arrival_time=2, burst_time=3, priority=1),
        Process(pid=3, arrival_time=4, burst_time=1, priority=4),
        Process(pid=4, arrival_time=6, burst_time=7, priority=3),
    ]

    # FCFS
    fcfs_result = fcfs_scheduling(processes.copy())
    print("FCFS Scheduling:")
    print_processes(fcfs_result)
    calculate_avg_times(fcfs_result)
    print()

    # SJN
    sjn_result = sjn_scheduling(processes.copy())
    print("SJN Scheduling:")
    print_processes(sjn_result)
    calculate_avg_times(sjn_result)
    print()

    # Priority
    priority_result = priority_scheduling(processes.copy())
    print("Priority Scheduling:")
    print_processes(priority_result)
    calculate_avg_times(priority_result)
    print()

    # Round Robin
    time_quantum = 2
    rr_result = round_robin_scheduling(processes.copy(), time_quantum)
    print("Round Robin Scheduling:")
    print_processes(rr_result)
    calculate_avg_times(rr_result)
    print()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'cli':
        cli_main()
    else:
        ui_main()

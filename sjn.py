# sjn.py

def sjn_scheduling(processes):
    processes.sort(key=lambda x: (x.arrival_time, x.burst_time))
    current_time = 0
    result = []
    while processes:
        available_processes = [p for p in processes if p.arrival_time <= current_time]
        if available_processes:
            next_process = min(available_processes, key=lambda x: x.burst_time)
            processes.remove(next_process)
            if current_time < next_process.arrival_time:
                current_time = next_process.arrival_time
            next_process.completion_time = current_time + next_process.burst_time
            next_process.turnaround_time = next_process.completion_time - next_process.arrival_time
            next_process.waiting_time = next_process.turnaround_time - next_process.burst_time
            current_time += next_process.burst_time
            result.append(next_process)
        else:
            current_time += 1

    return result

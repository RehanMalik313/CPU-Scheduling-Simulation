# round_robin.py

def round_robin_scheduling(processes, time_quantum):
    queue = []
    current_time = 0
    result = []
    while processes or queue:
        while processes and processes[0].arrival_time <= current_time:
            queue.append(processes.pop(0))

        if queue:
            process = queue.pop(0)
            if process.remaining_time > time_quantum:
                current_time += time_quantum
                process.remaining_time -= time_quantum
                while processes and processes[0].arrival_time <= current_time:
                    queue.append(processes.pop(0))
                queue.append(process)
            else:
                current_time += process.remaining_time
                process.remaining_time = 0
                process.completion_time = current_time
                process.turnaround_time = process.completion_time - process.arrival_time
                process.waiting_time = process.turnaround_time - process.burst_time
                result.append(process)
        else:
            current_time += 1

    return result

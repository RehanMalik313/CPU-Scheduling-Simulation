# process.py

class Process:
    def __init__(self, pid, arrival_time, burst_time, priority=0):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.priority = priority
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0

    def __str__(self):
        return (f"PID: {self.pid}, Arrival: {self.arrival_time}, Burst: {self.burst_time}, "
                f"Priority: {self.priority}, Completion: {self.completion_time}, "
                f"Waiting: {self.waiting_time}, Turnaround: {self.turnaround_time}")

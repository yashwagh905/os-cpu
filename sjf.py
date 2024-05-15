def preemptive_sjf(processes):
    n = len(processes)
    finish_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n
    completion_time = [0] * n
    remaining_time = [process[1] for process in processes]
    processed = [False] * n
    current_time = 0
    completed_processes = 0

    while completed_processes < n:
        min_burst = float('inf')
        min_index = -1

        # Find the process with the shortest remaining burst time
        for i in range(n):
            if not processed[i] and processes[i][0] <= current_time and remaining_time[i] < min_burst:
                min_burst = remaining_time[i]
                min_index = i

        if min_index == -1:
            current_time += 1
            continue

        remaining_time[min_index] -= 1
        current_time += 1

        # Check if the current process is completed
        if remaining_time[min_index] == 0:
            finish_time[min_index] = current_time
            turnaround_time[min_index] = finish_time[min_index] - processes[min_index][0]
            waiting_time[min_index] = turnaround_time[min_index] - processes[min_index][1]
            completion_time[min_index] = finish_time[min_index]  # Calculating completion time
            processed[min_index] = True
            completed_processes += 1

    return finish_time, turnaround_time, waiting_time, completion_time


def print_table(processes, finish_time, turnaround_time, waiting_time, completion_time):
    print("\nProcess\tArrival Time\tBurst Time\tCompletion Time\tTurnaround Time\tWaiting Time")
    for i, process in enumerate(processes):
        print(f"{i+1}\t{process[0]}\t\t{process[1]}\t\t{completion_time[i]}\t\t{turnaround_time[i]}\t\t{waiting_time[i]}")

def print_averages(turnaround_time, waiting_time, completion_time):
    avg_turnaround_time = sum(turnaround_time) / len(turnaround_time)
    avg_waiting_time = sum(waiting_time) / len(waiting_time)
    avg_completion_time = sum(completion_time) / len(completion_time)
    print("\nAverage Turnaround Time:", avg_turnaround_time)
    print("Average Waiting Time:", avg_waiting_time)
    print("Average Completion Time:", avg_completion_time)

def main():
    processes = []
    n = int(input("Enter the number of processes: "))

    for i in range(n):
        arrival_time = int(input(f"Enter arrival time for process {i+1}: "))
        burst_time = int(input(f"Enter burst time for process {i+1}: "))
        processes.append((arrival_time, burst_time))

    print("Non-Preemptive Shortest Job First:")
    finish_time, turnaround_time, waiting_time, completion_time = preemptive_sjf(processes)
    print_table(processes, finish_time, turnaround_time, waiting_time, completion_time)
    print_averages(turnaround_time, waiting_time, completion_time)

if __name__ == "__main__":
    main()
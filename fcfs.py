def first_come_first_serve(processes):
    n = len(processes)
    finish_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n
    completion_time = [0] * n

    # Calculate finish time for each process
    for i in range(n):
        if i == 0:
            finish_time[i] = processes[i][1]
        else:
            finish_time[i] = finish_time[i-1] + processes[i][1]

    # Calculate turnaround time, waiting time, and completion time
    for i in range(n):
        turnaround_time[i] = finish_time[i] - processes[i][0]
        waiting_time[i] = turnaround_time[i] - processes[i][1]
        completion_time[i] = finish_time[i]

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

    print("First Come First Serve:")
    finish_time, turnaround_time, waiting_time, completion_time = first_come_first_serve(processes)
    print_table(processes, finish_time, turnaround_time, waiting_time, completion_time)
    print_averages(turnaround_time, waiting_time, completion_time)

if __name__ == "__main__":
    main()

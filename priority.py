def preemptive_priority_scheduling(processes):
    n = len(processes)
    finish_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n
    completion_time = [0] * n
    remaining_time = [process[1] for process in processes]
    executed = [False] * n
    current_time = 0

    while True:
        min_priority = float('inf')
        min_index = -1
        for i in range(n):
            if not executed[i] and processes[i][0] <= current_time and processes[i][2] < min_priority:
                min_priority = processes[i][2]
                min_index = i

        if min_index == -1:
            break

        remaining_time[min_index] -= 1
        current_time += 1

        if remaining_time[min_index] == 0:
            finish_time[min_index] = current_time
            completion_time[min_index] = current_time
            executed[min_index] = True

    for i in range(n):
        turnaround_time[i] = finish_time[i] - processes[i][0]
        waiting_time[i] = turnaround_time[i] - processes[i][1]

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
        priority = int(input(f"Enter priority for process {i+1}: "))
        processes.append((arrival_time, burst_time, priority))

    print("Preemptive Priority Scheduling:")

   
    finish_time, turnaround_time, waiting_time, completion_time = preemptive_priority_scheduling(processes)
    print_table(processes, finish_time, turnaround_time, waiting_time, completion_time)
    print_averages(turnaround_time, waiting_time, completion_time)

if __name__ == "__main__":
    main()

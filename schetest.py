def first_come_first_serve(processes):
    n = len(processes)
    finish_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n

    # Calculate finish time for each process
    for i in range(n):
        if i == 0:
            finish_time[i] = processes[i][1]
        else:
            finish_time[i] = finish_time[i-1] + processes[i][1]

    # Calculate turnaround time and waiting time
    for i in range(n):
        turnaround_time[i] = finish_time[i] - processes[i][0]
        waiting_time[i] = turnaround_time[i] - processes[i][1]

    return finish_time, turnaround_time, waiting_time

def non_preemptive_sjf(processes):
    n = len(processes)
    finish_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n
    remaining_time = [process[1] for process in processes]
    processed = [False] * n
    current_time = 0

    while True:
        min_burst = float('inf')
        min_index = -1
        for i in range(n):
            if not processed[i] and processes[i][0] <= current_time and processes[i][1] < min_burst:
                min_burst = processes[i][1]
                min_index = i

        if min_index == -1:
            break

        current_time += processes[min_index][1]
        finish_time[min_index] = current_time
        turnaround_time[min_index] = finish_time[min_index] - processes[min_index][0]
        waiting_time[min_index] = turnaround_time[min_index] - processes[min_index][1]
        processed[min_index] = True

    return finish_time, turnaround_time, waiting_time

def preemptive_sjf(processes):
    n = len(processes)
    finish_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n
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
            processed[min_index] = True
            completed_processes += 1

    return finish_time, turnaround_time, waiting_time

def round_robin(processes, quantum):
    n = len(processes)
    finish_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n
    remaining_time = [process[1] for process in processes]
    current_time = 0

    while True:
        done = True
        for i in range(n):
            if remaining_time[i] > 0:
                done = False
                if remaining_time[i] > quantum:
                    current_time += quantum
                    remaining_time[i] -= quantum
                else:
                    current_time += remaining_time[i]
                    waiting_time[i] = max(0, current_time - processes[i][0] - processes[i][1])  # Corrected waiting time calculation
                    remaining_time[i] = 0
                    finish_time[i] = current_time

        if done:
            break

    for i in range(n):
        turnaround_time[i] = finish_time[i] - processes[i][0]

    return finish_time, turnaround_time, waiting_time


def non_preemptive_priority_scheduling(processes):
    n = len(processes)
    finish_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n
    processed = [False] * n

    current_time = 0
    while True:
        min_priority = float('inf')
        min_index = -1
        for i in range(n):
            if not processed[i] and processes[i][0] <= current_time and processes[i][2] < min_priority:
                min_priority = processes[i][2]
                min_index = i

        if min_index == -1:
            break

        waiting_time[min_index] = current_time - processes[min_index][0]
        current_time += processes[min_index][1]
        finish_time[min_index] = current_time
        turnaround_time[min_index] = finish_time[min_index] - processes[min_index][0]
        processed[min_index] = True

    return finish_time, turnaround_time, waiting_time

def preemptive_priority_scheduling(processes):
    n = len(processes)
    finish_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n
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
            executed[min_index] = True

    for i in range(n):
        turnaround_time[i] = finish_time[i] - processes[i][0]
        waiting_time[i] = turnaround_time[i] - processes[i][1]

    return finish_time, turnaround_time, waiting_time


def print_table(processes, finish_time, turnaround_time, waiting_time):
    print("\nProcess\tFinish Time\tTurnaround Time\tWaiting Time")
    for i, process in enumerate(processes):
        print(f"{i+1}\t{finish_time[i]}\t\t{turnaround_time[i]}\t\t{waiting_time[i]}")

def print_averages(turnaround_time, waiting_time):
    avg_turnaround_time = sum(turnaround_time) / len(turnaround_time)
    avg_waiting_time = sum(waiting_time) / len(waiting_time)
    print("\nAverage Turnaround Time:", avg_turnaround_time)
    print("Average Waiting Time:", avg_waiting_time)

def main():
    processes = []
    n = int(input("Enter the number of processes: "))

    for i in range(n):
        arrival_time = int(input(f"Enter arrival time for process {i+1}: "))
        burst_time = int(input(f"Enter burst time for process {i+1}: "))
        processes.append((arrival_time, burst_time))

    while True:
        print("\nSelect Scheduling Algorithm:")
        print("1. First Come First Serve")
        print("2. Shortest Job First (Non-Preemptive)")
        print("3. Shortest Job First (Preemptive)")
        print("4. Priority Scheduling (Non-Preemptive)")
        print("5. Priority Scheduling (Preemptive)")
        print("6. Round Robin")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("First Come First Serve:")
            finish_time, turnaround_time, waiting_time = first_come_first_serve(processes)
            print_table(processes, finish_time, turnaround_time, waiting_time)
            print_averages(turnaround_time, waiting_time)
        elif choice == 2:
            print("Shortest Job First (Non-Preemptive):")
            finish_time, turnaround_time, waiting_time = non_preemptive_sjf(processes)
            print_table(processes, finish_time, turnaround_time, waiting_time)
            print_averages(turnaround_time, waiting_time)
        elif choice == 3:
            print("Shortest Job First (Preemptive):")
            finish_time, turnaround_time, waiting_time = preemptive_sjf(processes)
            print_table(processes, finish_time, turnaround_time, waiting_time)
            print_averages(turnaround_time, waiting_time)
        elif choice == 4:
            print("Priority Scheduling (Non-Preemptive):")
            for i in range(n):
                priority = int(input(f"Enter priority for process {i+1}: "))
                processes[i] += (priority,)
            finish_time, turnaround_time, waiting_time = non_preemptive_priority_scheduling(processes)
            print_table(processes, finish_time, turnaround_time, waiting_time)
            print_averages(turnaround_time, waiting_time)
        elif choice == 5:
            print("Priority Scheduling (Preemptive):")
            for i in range(n):
                priority = int(input(f"Enter priority for process {i+1}: "))
                processes[i] += (priority,)
            finish_time, turnaround_time, waiting_time = preemptive_priority_scheduling(processes)
            print_table(processes, finish_time, turnaround_time, waiting_time)
            print_averages(turnaround_time, waiting_time)
        elif choice == 6:
            print("Round Robin:")
            quantum = int(input("Enter the time quantum for Round Robin scheduling: "))
            finish_time, turnaround_time, waiting_time = round_robin(processes, quantum)
            print_table(processes, finish_time, turnaround_time, waiting_time)
            print_averages(turnaround_time, waiting_time)
        elif choice == 7:
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please select again.")


if __name__ == "__main__":
    main()

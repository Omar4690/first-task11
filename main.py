import time


def run_sync_tasks():
    start_time = time.perf_counter()

    for task_number in range(1, 9):  # 8 tasks
        delay = task_number

        print(f"Task {task_number}: Start")
        time.sleep(delay)
        print(f"Task {task_number}: Finish after {delay} seconds")

    total_time = time.perf_counter() - start_time
    print(f"Total execution time: {total_time:.2f} seconds")


run_sync_tasks()

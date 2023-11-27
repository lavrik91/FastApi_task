import time
from multiprocessing import Process, Pool

# task 1
def worker(task_id):
    print(f'Start process {task_id}')
    time.sleep(2)
    print(f'End process {task_id}')


if __name__ == '__main__':
    processes = []

    for i in range(4):
        process = Process(target=worker, args=(i,))
        processes.append(process)

    for process in processes:
        process.start()

    for process in processes:
        process.join()

# task 2
def worker2(task_id):
    print(f'Start process {task_id}')
    time.sleep(2)
    print(f'End process {task_id}')


if __name__ == '__main__':
    with Pool(processes=4) as pool:
        pool.map(worker2, range(4))




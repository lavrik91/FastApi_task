import concurrent.futures
import threading


# task  # 1
count = 0

mutex = threading.Lock()


def func():
    global count
    for _ in range(100):
        with mutex:
            count += 1


treads = []

for i in range(3):
    tread = threading.Thread(target=func)
    treads.append(tread)

for tread in treads:
    tread.start()

for tread in treads:
    tread.join()

print(count)


# task #2
def worker(task_id):
    print(f'task with id {task_id} done')


if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        futures = []
        for i in range(4):
            future = executor.submit(worker, i)
            futures.append(future)

        concurrent.futures.wait(futures)

    print("All async_tasks completed")

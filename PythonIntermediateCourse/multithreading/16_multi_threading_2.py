from threading import Lock, Thread
from time import sleep

database_value = 0


def increase(lock):
    global database_value

    # lock.acquire()

    # local_copy = database_value

    # #processing
    # local_copy+=1
    # sleep(0.1)
    # database_value =  local_copy

    # lock.release()

    # Alternate Way

    with lock:
        local_copy = database_value
        # processing
        local_copy += 1
        sleep(0.1)
        database_value = local_copy


if __name__ == "__main__":

    lock = Lock()

    print(f"Start Value: {database_value}")

    thread1 = Thread(target=increase, args=[lock])
    thread2 = Thread(target=increase, args=[lock])

    # Race Condition --> When 2 or more thread tries to do same operation at the same time on same variable

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(f"End Value: {database_value}")

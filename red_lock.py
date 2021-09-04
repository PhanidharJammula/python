from redlock import Redlock
import gevent

redis_lock = Redlock([{"host": "localhost", "port": 6379, "db": 0}, ])

def lock_acquire():
    while True:
        lock_acquired = redis_lock.lock("contest_register", 1000)
        if not lock_acquired:
            gevent.sleep(0.01)
            continue
        gevent.sleep(20)
        return lock_acquired

def lock_release(lock_acquired):
    redis_lock.unlock(lock_acquired)

if __name__ == '__main__':
    lock = lock_acquire()
    lock_release(lock)

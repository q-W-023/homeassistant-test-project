import time

def wait_until(func, expected, timeout=10, interval=0.5):
    deadline = time.time() + timeout
    last = None
    while time.time() < deadline:
        last = func()
        if last == expected:
            return last
        time.sleep(interval)
    raise AssertionError(f"等待超时：期望 {expected}，最后实际 {last}")

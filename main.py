import time
from run import Run


executor = Run()

if __name__ == "__main__":
    executor.setup()
    try:
        executor.iterate()
    finally:
        executor.teardown()
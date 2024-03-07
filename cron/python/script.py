import time
import sys

print("Python is started.")
sys.stdout.flush()  # Flush the output buffer

while True:
    print("Hello from Python!")
    sys.stdout.flush()  # Flush the output buffer
    time.sleep(5)  # Sleep for 5 seconds

import psutil
import time
# While loop to check CPU usage every 10 seconds
while True:
    try:
        cpu_useage = psutil.cpu_percent(interval=10) # Every 10 seconds it will check the CPU usage
        if cpu_useage >= 85: # If CPU usage is greater than 85% then it will print an alert
            print("Alert! CPU usage exceeds threshold:", cpu_useage ,"%") # Print the CPU usage with Alert grater or equal to 85%
        else:
            print("CPU usage is normal:", cpu_useage ,"%") # Print CPU usage is normal
    except Exception as e:
        print("An error occurred:", e)
        break
    time.sleep(10) # Sleep for 10 seconds
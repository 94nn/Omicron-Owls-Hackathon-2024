import psutil
import time
import datetime

def monitor_network():
    previous_sent = 0
    previous_recv = 0

    while True:
        net_io_counters = psutil.net_io_counters()
        current_sent = net_io_counters.bytes_sent
        current_recv = net_io_counters.bytes_recv

        sent_diff = current_sent - previous_sent
        recv_diff = current_recv - previous_recv

        print(f"Network Usage: {sent_diff / 1024:.2f} KB sent, {recv_diff / 1024:.2f} KB received")

        previous_sent = current_sent
        previous_recv = current_recv

        time.sleep(1)

if __name__ == "__main__":
    monitor_network()
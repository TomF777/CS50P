"""
This is final project for course CS50P - Introduction to Python Programming
"""

import tkinter as tk
from tkinter import ttk
import queue
import threading
import time
import psutil

# Data exchange between background thread and main thread GUI
queue_data_collect = queue.Queue(400)


class SystemUtilMonitorApp(tk.Tk):
    """ Main TKinter GUI application class """
    QUEUE_POLLING_MS = 2500  # refresh time in milliseconds

    def __init__(self):
        super().__init__()

        self.geometry('800x600')
        self.title('CS50P Final Project - System Utilization Monitoring')


        self.cpu_var = tk.StringVar(value="CPU: ...")
        self.mem_var = tk.StringVar(value="Memory: ...")
        self.swap_var = tk.StringVar(value="Swap: ...")
        self.disk_number_var = tk.StringVar(value="Total Disks Number: ...")
        self.disk_util_var = tk.StringVar(value="")

        self.tasks_var = tk.StringVar(value="Tasks: --")
        self.system_load = tk.StringVar(value="Average system Load: ...")
        self.cpu_freq = tk.StringVar(value="CPU frequency: ...")

        self.pb_memory_usage_percent = ttk.Progressbar()
        self.pb_swap_usage_percent = ttk.Progressbar()

        self.pb_memory_usage_var = 0
        self.pb_swap_usage_var = 0

        self._build_widgets()

        # check for new results in queue
        self.after(SystemUtilMonitorApp.QUEUE_POLLING_MS, self._check_queue)

    def _check_queue(self):
        """
        Runs on the main thread via `after`. Safely pulls results out
        of the queue and updates the GUI - this is the only place
        that's allowed to touch tkinter variables/widgets.
        """
        try:
            while True:
                kind, payload = queue_data_collect.get_nowait()
                if kind == "OK":
                    self._update_widgets(payload)
                    self.app_status_var.set("Updated")
                else:
                    self.app_status_var.set(f"Error: {payload}")
        except queue.Empty:
            pass
        finally:
            self.after(200, self._check_queue)


    def _build_widgets(self):
        pad = {"padx": 10, "pady": 6, "sticky": "w"}
        frame = ttk.Frame(self, padding=10)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="System Monitor by Tomasz Frydek. August 2026",
                  font=("Arial", 14, "bold"),
                  relief="solid",
                  borderwidth=2,
                  padding=5,
                  foreground="blue") \
            .grid(row=0, column=0, columnspan=2, pady=(0, 10), sticky="w")


        for i, var in enumerate(
            [self.cpu_var, self.mem_var, self.swap_var,
             self.disk_number_var, self.disk_util_var, self.tasks_var,
             self.system_load, self.cpu_freq ],
            start=1,
        ):
            tk.Label(frame, textvariable=var,
                     font=("Arial", 16, "bold"),
                     relief="solid",
                     borderwidth=1,
                     justify="left", foreground="#2ECC71").grid(row=i, column=0, **pad)

        self.app_status_var = tk.StringVar(value="polling data")

        ttk.Label(frame, textvariable=self.app_status_var, foreground="gray") \
            .grid(row=9, column=0, pady=(15, 0), sticky="w")


    def _update_widgets(self, data):
        cpu, mem, swap, disk, tasks, load, freq = (
            data["cpu"], data["mem"], data["swap"],
            data["disk"], data["tasks"], data["load"],
            data["cpu_freq"]
        )
        self.cpu_var.set(
            f"CPU ({cpu['count']} cores): user {cpu['user']:.1f}% | "
            f"sys {cpu['system']:.1f}% | idle {cpu['idle']:.1f}%"
        )
        self.mem_var.set(f"Memory: used {mem['used']} / total {mem['total']} (MB)")
        self.swap_var.set(f"Swap: used {swap['used']} / total {swap['total']} (MB)")

        self.pb_memory_usage_percent['value'] = (mem['used'] / mem['total']) * 100
        self.pb_swap_usage_percent['value'] = (swap['used'] / swap['total']) * 100


        disk_number_txt = f"Total Disks Number: {len(disk["partitions"])}"
        self.disk_number_var.set(disk_number_txt)

        disk_txt = ''
        for idx, partition in enumerate(disk["disk_usage"]):
            # single parition letter
            disk_txt += str(disk["partitions"][idx].device + " " * 5)

            disk_txt += f"Total: {round(partition["total"]/(1024*1024*1024), 1)} GB   {partition['percent']}% used"
            if idx < len(disk["disk_usage"])-1:
                disk_txt += "\n"

        self.disk_util_var.set(str(disk_txt))


        self.system_load.set(f"System load: 1 Min :{load[0]:.1f}%  5 Min:{load[1]:.1f}%  15 Min: {load[2]:.1f}%")
        self.cpu_freq.set(f"CPU frequency: current: {freq[0]:.0f} Mhz | min: {freq[1]:.0f} | max: {freq[2]:.0f}")

        self.tasks_var.set(
            f"Tasks: {tasks['total']} total | {tasks['running']} running | "
            f"{tasks['sleeping']} sleeping | {tasks['stopped']} stopped | "
            f"{tasks['zombie']} zombie"
        )



def main():
    threading.Thread(target=backend, daemon=True).start()

    app = SystemUtilMonitorApp()
    app.mainloop()

def get_tasks():
    """
    Return numbers of all running processes on the local machine
    """
    total_procs = 0
    zombie_procs = 0
    sleeping_procs = 0
    running_procs = 0
    stopped_procs = 0

    for proc in psutil.process_iter(['pid', 'name', 'status']):
        total_procs += 1
        if proc.info['status'] == 'zombie':
            zombie_procs += 1
        elif proc.info['status'] == 'sleeping':
            sleeping_procs += 1
        elif proc.info['status'] == 'running':
            running_procs += 1
        elif proc.info['status'] == 'stopped':
            stopped_procs += 1

    return total_procs, \
            running_procs, \
            sleeping_procs, \
            stopped_procs, \
            zombie_procs


def get_cpu_count():
    """
    Return number of physical CPU cores only.
    """
    return psutil.cpu_count(logical=False)


def get_cpu_util():
    """
    Return utilization percentages for each specific CPU time
    - user: time spent by normal processes executing in user mode; 
                on Linux this also includes guest time
    - system: time spent by processes executing in kernel mode
    - idle: time spent doing nothing
    """
    cpu_times_percnt = psutil.cpu_times_percent(interval=None, percpu=False)
    return cpu_times_percnt.user, \
            cpu_times_percnt.system, \
            cpu_times_percnt.idle


def get_memory_util():
    """
    Return statistics about system memory usage in mega bytes
    """
    mem = psutil.virtual_memory()
    return int(mem.total/(1024*1024)), \
            int(mem.free/(1024*1024)), \
            int(mem.used/(1024*1024))

def get_swap_util():
    """
    Return system swap memory statistics in  mega bytes
    """
    mem = psutil.swap_memory()
    return int(mem.total/(1024*1024)), \
            int(mem.free/(1024*1024)), \
            int(mem.used/(1024*1024))

def get_disk_usage():
    """
    Return disk stats in bytes
    """

    partitions_stats = []
    partitions = get_disk_partitions()
    # get number of disk partitions
    if len(partitions) > 0:
        for idx in range(len(partitions)):
            disk_usage = psutil.disk_usage(partitions[idx].device)

            partitions_stats.append({"total": disk_usage.total,
                                    "used": disk_usage.used,
                                    "free": disk_usage.free,
                                    "percent": disk_usage.percent})
        return partitions_stats
    return None


def get_disk_partitions():
    """
    return all mounted disk partitions
    """
    disk_partitions = psutil.disk_partitions()
    return disk_partitions



def get_system_load():
    """
    Return the average system load over the last 1, 5 and 15 minutes
    as percentage representation.
    The numbers returned by `getloadavg` only make sense 
    if related to the number of CPU cores installed on the system
    """
    avg_load = [(x / psutil.cpu_count()) * 100 for x in psutil.getloadavg()]
    return avg_load

def get_cpu_freq():
    """
    Return current, min and max CPU frequency expressed in Mhz
    """
    cpu_freq = psutil.cpu_freq()
    return cpu_freq.current, cpu_freq.min, cpu_freq.max


def collect_monitor_data():
    """
    One function that gathers everything the GUI needs in single function call.
    This is the function we'll call on a timer / in a thread.
    Returns a plain dict - easy to pass across threads, easy to test
    without any GUI involved at all.
    """
    total, running, sleeping, stopped, zombie = get_tasks()
    cpu_time_user, cpu_time_system, cpu_time_idle = get_cpu_util()
    mem_total, mem_free, mem_used = get_memory_util()
    swap_total, swap_free, swap_used = get_swap_util()
    disk_usage = get_disk_usage()
    system_load = get_system_load()
    cpu_freq = get_cpu_freq()

    result =  {
        "tasks": {
            "total": total, "running": running, "sleeping": sleeping,
            "stopped": stopped, "zombie": zombie,
        },
        "cpu": {
            "count": get_cpu_count(), 
            "user": cpu_time_user, 
            "system": cpu_time_system, 
            "idle": cpu_time_idle,
        },
        "mem": {"total": mem_total, "free": mem_free, "used": mem_used},
        "swap": {"total": swap_total, "free": swap_free, "used": swap_used},
        "disk": {
            "disk_usage": disk_usage,
            "partitions": get_disk_partitions(),
                },
        "load": system_load,
        "cpu_freq": cpu_freq
    }

    return result

def backend():
    """
    Runs in a background thread.
    Poll monitor data and insert them into queue
    """
    while True:
        try:
            data = collect_monitor_data()
            if not queue_data_collect.full():
                queue_data_collect.put(("OK", data))
        except Exception as e:
            queue_data_collect.put(("ERROR", str(e)))
        time.sleep(1)

if __name__ == "__main__":
    main()

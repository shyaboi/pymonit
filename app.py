from tkinter import *
import time
import psutil
import platform
import cpuinfo
import multiprocessing 
cppu = cpuinfo.get_cpu_info()['brand_raw']

print(platform.node())
#tk root function
root = Tk()
root.title("clocks and such")
root.iconbitmap("ha.ico")
root.geometry("800x800")
#GUI functions
def clock():
    #vars to be shown in the app
    hour = time.strftime("%H")
    minn = time.strftime("%M")
    sec = time.strftime("%S")
    cores = str(psutil.cpu_percent(interval=None, percpu=True))
    mem = str(psutil.virtual_memory())
    coreCount = "pysical cores: " + str(psutil.cpu_count(logical=False))
    hyperCores= str(psutil.cpu_count())
    disks = "all disks: " + str(psutil.disk_partitions())
    cpu = platform.processor()
    rootDiskU = "root disk usage: "+str(psutil.disk_usage('/'))
    diskRR = "Root disk read/write: "+str(psutil.disk_io_counters(perdisk=False, nowrap=True))
    cpuFr = "freeq"+str(psutil.cpu_freq(percpu=True)[0])
    batt ="Battery: "+ str(psutil.sensors_battery())
    #updating labels
    thing.config(text="Time: "+hour + ":"+minn+";"+sec)
    thing2.config(text="CPU Core utilization: "+cores)
    thing3.config(text="Memory Utilization: "+mem)
    thing4.config(text=coreCount + " HyperCores: " +hyperCores)
    thing5.config(text=disks)
    thing6.config(text=cppu)
    thing7.config(text=rootDiskU)
    thing8.config(text=diskRR)
    thing9.config(text=batt)

#clock infor replacement loop
    thing.after(500, clock)
#things to put on screen
thing=Label(root, text="clock", font=("Helvetica", 48), fg="green", bg="black")
thing6=Label(root, text="cpu type")
thing2=Label(root, text="cores")
thing3=Label(root, text="memory")
thing4=Label(root, text="core count")
thing5=Label(root, text="disks", wraplength=600, justify="center")
thing7=Label(root, text="disk usage")
thing8=Label(root, text="disk read write", wraplength=200, justify="center")
thing9=Label(root, text="cpu freq ")

thing.pack(pady=20)
thing6.pack(pady=20)
thing4.pack(pady=20)
thing2.pack(pady=20)
thing3.pack(pady=20)
thing5.pack(pady=20)
thing7.pack(pady=20)
thing8.pack(pady=20)
thing9.pack(pady=20)

#putting on screen functions

clock()
#main loop
root.mainloop()





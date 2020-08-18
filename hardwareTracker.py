import psutil
import datetime
import threading
# mainly for creating time instance
p = psutil.Process()


# processsss function import
# from processTracker import donus

# threading set interval timer
# def setInterval(func, time):
#     e = threading.Event()
#     while not e.wait(time):
#         func()
# interval set funtion
dateF = datetime.datetime.fromtimestamp(p.create_time()).strftime("%Y-%m-%d %H:%M:%S")

# def foo():
#     mem = psutil.virtual_memory()
#     date = datetime.datetime.fromtimestamp(
#         p.create_time()).strftime("%Y-%m-%d %H:%M:%S")
#     print('\033[94m'+date)
# all cpu cores including hyperthreads
    # print('\033[92m'"cpu cores: "+str(psutil.cpu_count()))

# logical/pysical core
    # print("pysical cores: " + str(psutil.cpu_count(logical=False)))

# percent CPU utilization
    # print("percent cores utilized: " + str(psutil.cpu_percent(interval=None, percpu=True)))

# memory utilization
    # print('\033[95m'"memory utilization: "+str(mem))

# disks
    # check disk parts
    # print('\033[93m'"all disks" + str(psutil.disk_partitions()))
    # pulling individual disks from diskpart above
    # print("F disk usage: " + str(psutil.disk_usage('F:\\')))
    # disk usage
    # print(psutil.disk_usage('/'))

    # read write counters
    # print(psutil.disk_io_counters(perdisk=False, nowrap=True))

# battery only applicable on battery operated things
    # borked temp monit with open hardware monitor
    # import wmi

    # w = wmi.WMI(namespace="root\OpenHardwareMonitor")
    # temperature_infos = w.Sensor()
    # for sensor in temperature_infos:
    #     if sensor.SensorType==u'Temperature':
    #         if sensor.Name=='CPU Package':
    #             print( sensor )
    #             print( sensor.Value )

# processsss function
    # print(donus())


# setInterval(foo, 1)

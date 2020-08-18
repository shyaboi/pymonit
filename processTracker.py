import psutil


def donus():
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        print(proc.info)

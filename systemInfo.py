import platform
import subprocess
import psutil
import cpuinfo

def get_system_information():
    system_info = {}

    # System platform and version
    system_info['Platform'] = platform.system()
    system_info['System Version'] = platform.release()

    # Architecture
    system_info['Architecture'] = platform.machine()

    # CPU information
    cpu_info = cpuinfo.get_cpu_info()
    system_info['CPU'] = cpu_info['brand_raw']

    # CPU cores
    system_info['CPU Cores'] = psutil.cpu_count(logical=False)
    system_info['CPU Threads'] = psutil.cpu_count(logical=True)

    # Memory information
    memory_info = psutil.virtual_memory()
    system_info['Memory (Total, Available)'] = f'{memory_info.total / (1024**3):.2f} GB, {memory_info.available / (1024**3):.2f} GB'

    # GPU information for Windows
    try:
        gpu_info = subprocess.check_output(["wmic", "path", "win32_videocontroller", "get", "caption"]).decode("utf-8")
        system_info['GPU'] = gpu_info
    except Exception as e:
        system_info['GPU'] = 'N/A (GPU info not available)'

    # Write system information to a text file
    with open('system_info.txt', 'w') as file:
        for key, value in system_info.items():
            file.write(f'{key}: {value}\n')

if __name__ == "__main__":
    get_system_information()

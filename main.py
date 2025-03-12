import customtkinter as ctk
import psutil
import time
import threading
import GPUtil

# Function to monitor CPU, Disk, and GPU usage
def monitor_usage(cpu_label, disk_label, gpu_label):
    def update_usage():
        while True:
            # Get CPU usage as a percentage over a 1-second interval
            cpu_usage = psutil.cpu_percent(interval=1)
            cpu_label.configure(text=f"CPU Usage: {cpu_usage}%")

            # Get disk usage for the C: drive (can be customized for other drives)
            disk_usage = psutil.disk_usage(path='C:\\')  # Change path as needed
            disk_label.configure(text=f"Disk Usage: {disk_usage.percent}%")

            # Get GPU usage (this assumes you have a GPU available and GPUUtil is installed)
            gpus = GPUtil.getGPUs()
            if gpus:
                gpu_usage = gpus[0].memoryUtil * 100  # Using the first GPU in the list
                gpu_label.configure(text=f"GPU Usage: {gpu_usage:.2f}%")
            else:
                gpu_label.configure(text="GPU Usage: Not Available")

            time.sleep(1)
    
    # Start a new thread to update the usage stats in the background
    threading.Thread(target=update_usage, daemon=True).start()

# Setup the main GUI
def setup_gui():
    # Create the main window
    root = ctk.CTk()
    root.title("System Usage Monitor")

    # Enable dark mode for the customtkinter window
    ctk.set_appearance_mode("dark")

    # Set window size and layout
    root.geometry("400x350")
    root.resizable(False, False)

    # Create labels to display CPU, Disk, and GPU usage
    cpu_usage_label = ctk.CTkLabel(root, text="CPU Usage: 0%", font=("Arial", 16))
    cpu_usage_label.pack(pady=20)

    disk_usage_label = ctk.CTkLabel(root, text="Disk Usage: 0%", font=("Arial", 16))
    disk_usage_label.pack(pady=20)

    gpu_usage_label = ctk.CTkLabel(root, text="GPU Usage: 0%", font=("Arial", 16))
    gpu_usage_label.pack(pady=20)

    # Start monitoring CPU, Disk, and GPU usage
    monitor_usage(cpu_usage_label, disk_usage_label, gpu_usage_label)

    # Start the Tkinter event loop
    root.mainloop()

# Run the GUI
if __name__ == "__main__":
    setup_gui()

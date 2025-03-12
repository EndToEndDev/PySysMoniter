import GPUtil
import psutil
import time
import customtkinter as ctk

# Function to get GPU usage (NVIDIA only)
def get_gpu_usage():
    try:
        # Check for NVIDIA GPUs using GPUtil
        gpus = GPUtil.getGPUs()
        if gpus:
            gpu_usage = []
            for gpu in gpus:
                usage = gpu.memoryUtil * 100  # GPU memory utilization as percentage
                gpu_usage.append(f"NVIDIA GPU {gpu.id}: {usage}%")
            return '\n'.join(gpu_usage)
        else:
            return "No NVIDIA GPUs found."
    except Exception as e:
        return "Error retrieving NVIDIA GPU usage."

# Function to update CPU, Disk, and GPU usage
def monitor_usage():
    # Get CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    
    # Get Disk usage for C drive (or modify as needed)
    disk_usage = psutil.disk_usage('C:\\')
    
    # Get GPU usage (NVIDIA only)
    gpu_usage = get_gpu_usage()
    
    # Return formatted usage details
    return f"CPU Usage: {cpu_usage}%\nDisk Usage: {disk_usage.percent}%\nGPU Usage:\n{gpu_usage}"

# Function to update the display in the CustomTkinter window
def update_display(status_label):
    usage = monitor_usage()  # Get the updated usage info
    status_label.configure(text=usage)
    status_label.after(1000, update_display, status_label)  # Update every 1 second

# Creating the CustomTkinter window
def create_gui():
    # Initialize the window
    root = ctk.CTk()
    root.title("System Usage Monitor")
    
    # Set dark mode appearance
    ctk.set_appearance_mode("dark")
    
    # Create a label to display system usage
    status_label = ctk.CTkLabel(root, text="Loading system usage...", anchor="w")
    status_label.pack(pady=10, padx=20, fill="x", anchor="w")
    
    # Start the display update loop
    update_display(status_label)
    
    # Run the Tkinter main loop
    root.mainloop()

if __name__ == "__main__":
    create_gui()

# PySysMoniter
A little gui to see system metrics

This Python script is designed to monitor and display **CPU**, **Disk**, and **NVIDIA GPU usage** in real time. It uses the **`psutil`** library to track CPU and disk usage, and **`GPUtil`** to monitor the GPU usage specifically for NVIDIA GPUs. The results are displayed in a **CustomTkinter** GUI, which is a modern and visually appealing alternative to the standard Tkinter library.

## Libraries Used

- **`psutil`**: Used to retrieve system information such as CPU usage and disk usage.
- **`GPUtil`**: A Python library used to interact with NVIDIA GPUs and retrieve GPU usage information.
- **`customtkinter`**: An extension of the Tkinter library that provides a modern and customizable GUI with a dark mode.

## Key Functions

### 1. **`get_gpu_usage()`**
This function checks for NVIDIA GPUs using the **`GPUtil.getGPUs()`** method and retrieves their memory usage as a percentage. If no NVIDIA GPUs are found, it returns a message indicating that.

```python
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
```

### 2. **`monitor_usage()`**
This function collects real-time system information:
- **CPU Usage** using **`psutil.cpu_percent()`**
- **Disk Usage** for the C drive using **`psutil.disk_usage()`**
- **GPU Usage** using the **`get_gpu_usage()`** function

It formats these values into a readable string that displays the current system usage.

```python
def monitor_usage():
    # Get CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    
    # Get Disk usage for C drive (or modify as needed)
    disk_usage = psutil.disk_usage('C:\\')
    
    # Get GPU usage (NVIDIA only)
    gpu_usage = get_gpu_usage()
    
    # Return formatted usage details
    return f"CPU Usage: {cpu_usage}%\nDisk Usage: {disk_usage.percent}%\nGPU Usage:\n{gpu_usage}"
```

### 3. **`update_display(status_label)`**
This function updates the **CustomTkinter** window with the current system usage information every second. It continuously calls the **`monitor_usage()`** function and updates the text of the label on the GUI.

```python
def update_display(status_label):
    usage = monitor_usage()  # Get the updated usage info
    status_label.configure(text=usage)
    status_label.after(1000, update_display, status_label)  # Update every 1 second
```

### 4. **`create_gui()`**
This function sets up the **CustomTkinter** window. It initializes the window, sets the dark mode theme, creates a label to display system usage, and starts the update loop that continuously refreshes the displayed information.

```python
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
```

### 5. **`__main__` Block**
The **`if __name__ == "__main__":`** block ensures that the **`create_gui()`** function is called when the script is executed directly.

```python
if __name__ == "__main__":  
    create_gui()
```

## How It Works

- The **`get_gpu_usage()`** function checks for available NVIDIA GPUs and fetches their memory utilization.
- **CPU** usage is updated every second using **`psutil.cpu_percent(interval=1)`**.
- **Disk** usage is fetched using **`psutil.disk_usage()`**, which returns the disk usage for a given path (the script checks the C drive by default).
- **GPU** usage is retrieved using **`GPUtil.getGPUs()`**, which accesses the NVIDIA GPUs on the system and reports their memory usage.
- The GUI is created using **`customtkinter`** in **dark mode**, and the system usage information is displayed in real-time on the GUI.

## Requirements

Make sure to install the required libraries before running the script:

```bash
pip install psutil GPUtil customtkinter
```

## Running the Script

Once the dependencies are installed, simply run the script and a GUI window will appear displaying your system's real-time **CPU**, **Disk**, and **GPU** usage.

### Example Output in the GUI:

```
CPU Usage: 45%
Disk Usage: 72%
GPU Usage:
NVIDIA GPU 0: 38%
```

### Error Handling

- If no **NVIDIA GPU** is found on the system, the script will display the message: "No NVIDIA GPUs found."
- If there’s an error when retrieving GPU usage (e.g., if **`GPUtil`** encounters an issue), it will display: "Error retrieving NVIDIA GPU usage."

## Conclusion

This application provides a simple and intuitive way to monitor system resources, specifically **CPU**, **Disk**, and **NVIDIA GPU** usage, all through a clean, modern GUI built with **CustomTkinter**.
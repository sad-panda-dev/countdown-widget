import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
from timer.countdown_timer import CountdownTimer


class CountdownApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Widget")
        
        self.timer = None
        
        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Helvetica", 24))
        
        self.create_widgets()
    
    def create_widgets(self):
        self.target_date_label = ttk.Label(self.root, text="Enter target date (YYYY-MM-DD HH:MM:SS):")
        self.target_date_label.pack(pady=10)

        self.target_date_entry = ttk.Entry(self.root, width=30)
        self.target_date_entry.pack(pady=10)
        
        self.timer_title_label = ttk.Label(self.root, text="Enter timer title:")
        self.timer_title_label.pack(pady=10)
        
        self.timer_title_entry = ttk.Entry(self.root, width=30)
        self.timer_title_entry.pack(pady=10)
        
        self.set_date_button = ttk.Button(self.root, text="Create Timer", command=self.create_timer)
        self.set_date_button.pack(pady=10)
    
    def create_timer(self):
        date_str = self.target_date_entry.get()
        timer_title = self.timer_title_entry.get()
        
        if not date_str or not timer_title:
            messagebox.showerror("Error", "Please enter both the target date and timer title.")
            return
        
        try:
            target_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            messagebox.showerror("Invalid Date Format", "Please enter the date in the format YYYY-MM-DD HH:MM:SS")
            return
        
        self.timer = CountdownTimer(target_date, timer_title)
        
        self.display_timer_window()
    
    def display_timer_window(self):
        if self.timer:
            new_window = tk.Toplevel(self.root)
            new_window.title("Countdown Timer")
            
            title_label = ttk.Label(new_window, text=f"Timer Title: {self.timer.title}", font=("Helvetica", 18))
            title_label.pack(pady=10)
            
            countdown_label = ttk.Label(new_window, text="", font=("Helvetica", 24))
            countdown_label.pack(pady=20)
            
            def update_countdown_display():
                countdown_str = self.timer.get_time_remaining()
                countdown_label.config(text=countdown_str)
                if countdown_str != "Time's up!":
                    new_window.after(1000, update_countdown_display)
            
            update_countdown_display()
            
            def on_close():
                new_window.destroy()  
                self.root.destroy()  
            
            close_button = ttk.Button(new_window, text="Close", command=on_close)
            close_button.pack(pady=10)
            
            new_window.protocol("WM_DELETE_WINDOW", on_close)  
            
            
            self.root.withdraw()

def main():
    root = tk.Tk()
    app = CountdownApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
import json
import os
from datetime import datetime

class eFootballAnalyzer:
    def __init__(self, master):
        self.master = master
        master.title("⚽ eFootball Iconic Player Analyzer")
        master.geometry("900x700")
        master.configure(bg="#1a1a1a")
        
        self.stats_file = "stats.json"
        
        # Title
        title = tk.Label(master, text="⚽ eFootball Iconic Player Analyzer", 
                        font=("Arial", 20, "bold"), fg="#00ff00", bg="#1a1a1a")
        title.pack(pady=15)
        
        # Input Frame
        input_frame = tk.Frame(master, bg="#1a1a1a")
        input_frame.pack(pady=10)
        
        tk.Label(input_frame, text="Total Players:", fg="white", bg="#1a1a1a").pack(side=tk.LEFT, padx=5)
        self.total_players = tk.Entry(input_frame, width=10)
        self.total_players.insert(0, "150")
        self.total_players.pack(side=tk.LEFT, padx=5)
        
        tk.Label(input_frame, text="Iconic Players:", fg="white", bg="#1a1a1a").pack(side=tk.LEFT, padx=5)
        self.iconic_count = tk.Entry(input_frame, width=10)
        self.iconic_count.insert(0, "3")
        self.iconic_count.pack(side=tk.LEFT, padx=5)
        
        # Calculation Frame
        calc_frame = tk.Frame(master, bg="#1a1a1a")
        calc_frame.pack(pady=10)
        
        tk.Label(calc_frame, text="Attempts:", fg="white", bg="#1a1a1a").pack(side=tk.LEFT, padx=5)
        self.attempts = tk.Entry(calc_frame, width=10)
        self.attempts.insert(0, "10")
        self.attempts.pack(side=tk.LEFT, padx=5)
        
        self.calculate_btn = tk.Button(calc_frame, text="Calculate", command=self.calculate, 
                                       bg="#00ff00", fg="black", font=("Arial", 10, "bold"))
        self.calculate_btn.pack(side=tk.LEFT, padx=5)
        
        # Results
        self.results_text = tk.Text(master, height=12, width=100, bg="#2a2a2a", fg="#00ff00", font=("Courier", 10))
        self.results_text.pack(pady=10, padx=10)
        
        # Buttons
        button_frame = tk.Frame(master, bg="#1a1a1a")
        button_frame.pack(pady=10)
        
        tk.Button(button_frame, text="📊 Graph", command=self.show_graph, 
                 bg="#0066ff", fg="white", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="📈 Stats", command=self.show_stats, 
                 bg="#0066ff", fg="white", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
    
    def calculate(self):
        try:
            total = int(self.total_players.get())
            iconic = int(self.iconic_count.get())
            attempts = int(self.attempts.get())
            
            if total <= 0 or iconic <= 0 or attempts <= 0:
                messagebox.showerror("Error", "All values must be positive!")
                return
            
            single_prob = iconic / total
            prob_at_least_one = 1 - (1 - single_prob) ** attempts
            expected_attempts = 1 / single_prob
            
            results = f"""
╔═══════════════════════════════════════════════════════════╗
║     eFootball Iconic Player Analysis                      ║
╚═══════════════════════════════════════════════════════════╝

📊 Input:
   Total Players: {total}
   Iconic Players: {iconic}
   Attempts: {attempts}

🎯 Probability:
   Single Pull: {single_prob*100:.2f}%
   At Least One in {attempts}: {prob_at_least_one*100:.2f}%
   Expected Attempts: {expected_attempts:.0f}

💰 Cost (100 coins per pull):
   Total Cost: {attempts * 100} coins
   Expected Cost: {int(expected_attempts * 100)} coins

✅ Recommendation:
   Pull {int(expected_attempts * 1.5):.0f} times for best chances!
"""
            
            self.results_text.delete(1.0, tk.END)
            self.results_text.insert(1.0, results)
            
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers!")
    
    def show_graph(self):
        try:
            total = int(self.total_players.get())
            iconic = int(self.iconic_count.get())
            
            single_prob = iconic / total
            attempts_range = np.arange(1, 101)
            probabilities = 1 - (1 - single_prob) ** attempts_range
            
            plt.figure(figsize=(10, 6))
            plt.plot(attempts_range, probabilities * 100, linewidth=2, color='#00ff00')
            plt.xlabel('Attempts', fontsize=12)
            plt.ylabel('Probability (%)', fontsize=12)
            plt.title('eFootball: Probability vs Attempts', fontsize=14, fontweight='bold')
            plt.grid(True, alpha=0.3)
            plt.show()
            
        except ValueError:
            messagebox.showerror("Error", "Invalid input!")
    
    def show_stats(self):
        messagebox.showinfo("Statistics", "Stats feature coming soon!")

if __name__ == '__main__':
    root = tk.Tk()
    app = eFootballAnalyzer(root)
    root.mainloop()

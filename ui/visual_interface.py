import tkinter as tk
from tkinter import ttk

class TradingInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Trading Dashboard")
        self.activity_frame = ttk.Frame(self.root, padding="10")
        self.activity_frame.grid(row=0, column=0, sticky="nsew")
        self.wallet_frame = ttk.Frame(self.root, padding="10")
        self.wallet_frame.grid(row=1, column=0, sticky="nsew")

        self.activity_label = ttk.Label(self.activity_frame, text="Activity", font=("Arial", 16))
        self.activity_label.grid(row=0, column=0, sticky="w")
        self.activity_text = tk.Text(self.activity_frame, height=10, width=50)
        self.activity_text.grid(row=1, column=0, sticky="nsew")

        self.wallet_label = ttk.Label(self.wallet_frame, text="Wallet", font=("Arial", 16))
        self.wallet_label.grid(row=0, column=0, sticky="w")
        self.wallet_text = tk.Text(self.wallet_frame, height=5, width=50)
        self.wallet_text.grid(row=1, column=0, sticky="nsew")

    def update_activity(self, asset_type, market_data, decision):
        self.activity_text.insert(tk.END, f"{asset_type} Market Data: {market_data}\n")
        self.activity_text.insert(tk.END, f"Decision: {decision}\n")
        self.activity_text.insert(tk.END, "-" * 50 + "\n")

    def update_wallet(self, wallet_data):
        self.wallet_text.delete(1.0, tk.END)
        self.wallet_text.insert(tk.END, f"Wallet: {wallet_data}\n")

    def run(self):
        self.root.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox
from typing import Callable

class AppView(tk.Tk):
    """Main UI Window."""
    def __init__(self):
        super().__init__()
        self.title("TechStore Inventory Management")
        self.geometry("500x400")

        # Callbacks (Injected by Controller)
        self.on_refresh: Callable = None
        self.on_transaction: Callable = None

        self._build_ui()

    def _build_ui(self):
        # Inventory Display
        tk.Label(self, text="Inventory", font=("Arial", 14, "bold")).pack(pady=5)
        
        columns = ("id", "name", "price", "stock")
        self.tree = ttk.Treeview(self, columns=columns, show="headings", height=5)
        for col in columns:
            self.tree.heading(col, text=col.capitalize())
            self.tree.column(col, width=100)
        self.tree.pack(pady=5)

        tk.Button(self, text="Refresh Inventory", command=lambda: self.on_refresh()).pack(pady=5)

        # -- Transaction Form --
        frame = tk.LabelFrame(self, text="Process Sale")
        frame.pack(pady=10, padx=20, fill="x")

        tk.Label(frame, text="Cust ID:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_cust = tk.Entry(frame, width=10)
        self.entry_cust.grid(row=0, column=1)

        tk.Label(frame, text="Prod ID:").grid(row=0, column=2, padx=5, pady=5)
        self.entry_prod = tk.Entry(frame, width=10)
        self.entry_prod.grid(row=0, column=3)

        tk.Label(frame, text="Qty:").grid(row=0, column=4, padx=5, pady=5)
        self.entry_qty = tk.Entry(frame, width=10)
        self.entry_qty.grid(row=0, column=5)

        tk.Button(frame, text="Submit", command=self._handle_submit).grid(row=1, column=0, columnspan=6, pady=10)

    def update_inventory_list(self, products: list):
        """Clears and repopulates the Treeview."""
        for item in self.tree.get_children():
            self.tree.delete(item)
        for p in products:
            self.tree.insert("", tk.END, values=(p.id, p.name, p.price, p.stock))

    def _handle_submit(self):
        if self.on_transaction:
            try:
                c_id = int(self.entry_cust.get())
                p_id = int(self.entry_prod.get())
                qty = int(self.entry_qty.get())
                self.on_transaction(c_id, p_id, qty)
            except ValueError:
                self.show_error("Please enter valid integers.")

    def show_message(self, title: str, msg: str):
        messagebox.showinfo(title, msg)

    def show_error(self, msg: str):
        messagebox.showerror("Error", msg)
import customtkinter as ctk
from tkinter import messagebox
import sqlite3 as pysql

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# Database
conn = pysql.connect("fds.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS items (
    item_name TEXT,
    price REAL
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS cart (
    item_name TEXT,
    item_price REAL
)
""")

conn.commit()

# Main window
root = ctk.CTk()
root.title("Login")
root.geometry("400x300")

ctk.CTkLabel(root, text="Login", font=("Verdana", 22, "bold")).pack(pady=20)

uid = ctk.CTkEntry(root, placeholder_text="User ID")
uid.pack(pady=10)

upd = ctk.CTkEntry(root, placeholder_text="Password", show="*")
upd.pack(pady=10)

def open_app():
    if uid.get() == "admin" and upd.get() == "admin123":
        root.destroy()
        admin_window()
    elif uid.get() == "u" and upd.get() == "u":
        root.destroy()
        user_window()

ctk.CTkButton(root, text="Login", command=open_app).pack(pady=20)

# User Window
def user_window():
    win = ctk.CTk()
    win.title("FoodFly")
    win.geometry("400x300")

    ctk.CTkLabel(win, text="Welcome to FoodFly", font=("Helvetica", 18, "bold")).pack(pady=10)
    ctk.CTkLabel(win, text="Choose your meal").pack(pady=10)

    ctk.CTkButton(win, text="Next >>", command=menu_sys).pack(pady=20)
    win.mainloop()

# Admin Window
def admin_window():
    win = ctk.CTk()
    win.title("Admin Panel")
    win.geometry("400x300")

    entryitem_name = ctk.CTkEntry(win, placeholder_text="Item Name")
    entryitem_name.pack(pady=10)

    entryitem_price = ctk.CTkEntry(win, placeholder_text="Item Price")
    entryitem_price.pack(pady=10)

    def add_item():
        item_name = entryitem_name.get()
        item_price = entryitem_price.get()
        if item_name and item_price:
            query = "INSERT INTO items (item_name, price) VALUES (?, ?)"
            cur.execute(query, (item_name, item_price))
            conn.commit()
            messagebox.showinfo("Success", "Item Added")

    def delete_item():
        item_name = entryitem_name.get()
        query = "DELETE FROM items WHERE item_name = ?"
        cur.execute(query, (item_name,))
        conn.commit()
        messagebox.showinfo("Deleted", "Item Deleted")

    ctk.CTkButton(win, text="Add Item", command=add_item).pack(pady=10)
    ctk.CTkButton(win, text="Delete Item", command=delete_item).pack(pady=10)
    ctk.CTkButton(win, text="View Menu", command=item_menu).pack(pady=10)

    win.mainloop()

# View Items
def item_menu():
    i = ctk.CTk()
    i.title("Menu")
    i.geometry("300x400")

    cur.execute("select * from items")
    re = cur.fetchall()

    for item_name, item_price in re:
        ctk.CTkLabel(i, text=f"{item_name} - ₹{item_price}").pack(pady=5)

    i.mainloop()

# Menu System
def menu_sys():
    menu = ctk.CTk()
    menu.title("Menu")
    menu.geometry("300x400")

    cur.execute("select * from items")
    re = cur.fetchall()

    for item_name, item_price in re:
        ctk.CTkButton(menu,
                      text=f"{item_name} - ₹{item_price}",
                      command=lambda name=item_name, price=item_price: cart(name, price)
                      ).pack(pady=5)

    ctk.CTkButton(menu, text="Checkout", command=checkout).pack(pady=20)
    menu.mainloop()

# Cart
def cart(item_name, item_price):
    query = "INSERT INTO cart (item_name, item_price) VALUES (?, ?)"
    cur.execute(query, (item_name, item_price))
    conn.commit()

# Checkout
def checkout():
    window = ctk.CTk()
    window.title("Checkout")
    window.geometry("350x400")

    ctk.CTkLabel(window, text="Order Summary", font=("Arial", 18)).pack(pady=10)

    cur.execute("select * from cart")
    re = cur.fetchall()

    total = 0
    for item_name, item_price in re:
        ctk.CTkLabel(window, text=f"{item_name} - ₹{item_price}").pack()
        total += item_price

    cur.execute("delete from cart")
    conn.commit()

    ctk.CTkLabel(window, text=f"Total = ₹{total}", font=("Arial", 16, "bold")).pack(pady=20)
    ctk.CTkButton(window, text="Order Now", command=thks).pack(pady=10)

    window.mainloop()

def thks():
    win = ctk.CTk()
    win.title("Done")
    win.geometry("300x200")
    ctk.CTkLabel(win, text="Order Placed Successfully!").pack(pady=40)
    win.mainloop()

root.mainloop()

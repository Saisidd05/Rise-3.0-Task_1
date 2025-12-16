import tkinter as tk
from tkinter import ttk
import requests
import winsound
import threading
import time

currency_names = {
    "USD": "United States Dollar", "INR": "Indian Rupee", "EUR": "Euro",
    "GBP": "British Pound", "JPY": "Japanese Yen", "AUD": "Australian Dollar",
    "CAD": "Canadian Dollar", "CHF": "Swiss Franc", "CNY": "Chinese Yuan",
    "SGD": "Singapore Dollar", "VND": "Vietnamese Dong", "UAH": "Ukrainian Hryvnia",
    "TZS": "Tanzanian Shilling", "UGX": "Ugandan Shilling", "TWD": "New Taiwan Dollar",
    "UYU": "Uruguayan Peso", "UZS": "Uzbekistani Som", "VES": "Venezuelan Bolívar"
}

def fetch_currencies():
    data = requests.get("https://open.er-api.com/v6/latest/USD").json()
    codes = sorted(data["rates"].keys())
    return [f"{c} – {currency_names.get(c,'Name not available')}" for c in codes]

def play_sound():
    winsound.Beep(900, 200)

def animate_result():
    colors = ["#86efac", "#4ade80", "#22c55e"]
    for _ in range(2):
        for c in colors:
            result_box.config(bg=c)
            time.sleep(0.12)
    result_box.config(bg="#e0f2fe")

def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_code = from_cb.get().split(" – ")[0]
        to_code = to_cb.get().split(" – ")[0]

        data = requests.get(f"https://open.er-api.com/v6/latest/{from_code}").json()
        rate = data["rates"][to_code]
        result = amount * rate

        result_box.config(
            text=f"🎉 {amount} {from_code}\n⬇️\n{result:.2f} {to_code}",
            fg="#065f46"
        )

        threading.Thread(target=play_sound).start()
        threading.Thread(target=animate_result).start()

    except:
        result_box.config(
            text="❌ ERROR\nCheck input",
            bg="#fecaca",
            fg="#7f1d1d"
        )

def swap_currency():
    a, b = from_cb.get(), to_cb.get()
    from_cb.set(b)
    to_cb.set(a)

def filter_combo(event, combo, full_list):
    value = combo.get().lower()
    combo["values"] = [c for c in full_list if value in c.lower()]

# ---------------- UI ----------------
root = tk.Tk()
root.title("🌈 Currency Converter")
root.geometry("600x600")
root.configure(bg="#e0f2fe")
root.resizable(False, False)

# Header
header = tk.Frame(root, bg="#60a5fa", height=70)
header.pack(fill="x")
tk.Label(
    header,
    text="💱 Currency Converter",
    font=("Segoe UI", 20, "bold"),
    bg="#60a5fa",
    fg="white"
).pack(pady=15)

# Main Card
card = tk.Frame(root, bg="white")
card.pack(padx=20, pady=20, fill="both", expand=True)

tk.Label(card, text="💰 Enter Amount",
         font=("Segoe UI", 12),
         bg="white", fg="#1e3a8a").pack(pady=(15, 5))

amount_entry = tk.Entry(card, font=("Segoe UI", 14),
                        justify="center",
                        bg="#f8fafc")
amount_entry.pack(ipady=6)

currencies = fetch_currencies()

tk.Label(card, text="🔍 From Currency",
         bg="white", fg="#2563eb").pack(pady=(15, 5))
from_cb = ttk.Combobox(card, values=currencies, width=50)
from_cb.set("USD – United States Dollar")
from_cb.pack()
from_cb.bind("<KeyRelease>",
             lambda e: filter_combo(e, from_cb, currencies))

swap_btn = tk.Button(card, text="🔁 SWAP",
                     command=swap_currency,
                     bg="#fde047",
                     font=("Segoe UI", 10, "bold"))
swap_btn.pack(pady=10)

tk.Label(card, text="🔍 To Currency",
         bg="white", fg="#2563eb").pack(pady=(5, 5))
to_cb = ttk.Combobox(card, values=currencies, width=50)
to_cb.set("INR – Indian Rupee")
to_cb.pack()
to_cb.bind("<KeyRelease>",
           lambda e: filter_combo(e, to_cb, currencies))

tk.Button(
    card,
    text="🚀 CONVERT",
    command=convert_currency,
    font=("Segoe UI", 13, "bold"),
    bg="#22c55e",
    fg="black",
    width=20
).pack(pady=18)

result_box = tk.Label(
    card,
    text="🎯 RESULT WILL APPEAR HERE",
    font=("Segoe UI", 15, "bold"),
    bg="#e0f2fe",
    fg="#1e3a8a",
    height=5,
    width=42,
    relief="ridge"
)
result_box.pack(pady=10)

# Footer
footer = tk.Frame(root, bg="#bfdbfe", height=35)
footer.pack(fill="x")

tk.Label(
    footer,
    text="Developed with ❤️ using Python & Tkinter | © 2025 Sai Siddharth Nanda Gopal",
    font=("Segoe UI", 9),
    bg="#bfdbfe",
    fg="#1e3a8a"
).pack(pady=8)

root.mainloop()

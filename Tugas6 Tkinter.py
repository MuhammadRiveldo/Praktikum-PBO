# Muhammad Riveldo Hermawan Putra
# 122140037
# Tugas 6 Tkinter

import tkinter as tk
from tkinter import messagebox

# Dictionary untuk menyimpan data user, format: {username: password}
users = {}

# Dictionary untuk menyimpan daftar tugas masing-masing user, format: {username: [daftar_tugas]}
user_tasks = {}

# Fungsi untuk menampilkan frame tertentu (mengangkat ke atas)
def show_frame(frame):
    frame.tkraise()

# Fungsi untuk proses login user
def login():
    username = login_username.get()
    password = login_password.get()

    # Cek apakah username dan password cocok
    if username in users and users[username] == password:
        todo_username.set(username)  # Simpan nama user aktif
        update_task_list()           # Perbarui daftar tugas di tampilan
        show_frame(todo_frame)       # Pindah ke tampilan to-do list
    else:
        messagebox.showerror("Login Gagal", "Username atau password salah")

# Fungsi untuk registrasi akun baru
def register():
    username = reg_username.get()
    password = reg_password.get()

    # Validasi agar semua field diisi
    if not username or not password:
        messagebox.showwarning("Peringatan", "Semua field wajib diisi")
        return

    # Cek apakah username sudah terdaftar
    if username in users:
        messagebox.showerror("Gagal", "Username sudah ada")
    else:
        users[username] = password           # Simpan username dan password
        user_tasks[username] = []            # Inisialisasi daftar tugas user
        messagebox.showinfo("Berhasil", "Registrasi berhasil")
        show_frame(login_frame)              # Kembali ke halaman login

# Fungsi untuk logout
def logout():
    todo_username.set("")                   # Kosongkan user aktif
    task_listbox.delete(0, tk.END)          # Kosongkan tampilan tugas
    show_frame(login_frame)                 # Kembali ke halaman login

# Fungsi untuk menambah tugas ke daftar
def add_task():
    task = task_entry.get()
    username = todo_username.get()
    if task:
        user_tasks[username].append(task)   # Tambahkan ke list
        update_task_list()                  # Refresh tampilan list
        task_entry.delete(0, tk.END)        # Kosongkan field input

# Fungsi untuk menghapus tugas yang dipilih
def delete_task():
    username = todo_username.get()
    selection = task_listbox.curselection()  # Ambil indeks tugas yang dipilih
    if selection:
        index = selection[0]
        del user_tasks[username][index]      # Hapus dari data
        update_task_list()                   # Perbarui tampilan

# Fungsi untuk memperbarui tampilan listbox tugas
def update_task_list():
    task_listbox.delete(0, tk.END)                 # Bersihkan listbox
    username = todo_username.get()
    for task in user_tasks.get(username, []):      # Tambahkan tugas user
        task_listbox.insert(tk.END, task)

# ---------- PENGATURAN UI AWAL ----------
root = tk.Tk()
root.title("To-Do App with Login")
root.geometry("400x300")

# Variabel global untuk menyimpan username aktif
todo_username = tk.StringVar()

# ============ Frame Login ============
login_frame = tk.Frame(root)
login_frame.grid(row=0, column=0, sticky='news')

tk.Label(login_frame, text="Login", font=('Arial', 16)).pack(pady=10)
login_username = tk.StringVar()
login_password = tk.StringVar()

tk.Label(login_frame, text="Username").pack()
tk.Entry(login_frame, textvariable=login_username).pack()
tk.Label(login_frame, text="Password").pack()
tk.Entry(login_frame, textvariable=login_password, show="*").pack()

tk.Button(login_frame, text="Login", command=login).pack(pady=10)
tk.Button(login_frame, text="Register", command=lambda: show_frame(register_frame)).pack()

# ============ Frame Register ============
register_frame = tk.Frame(root)
register_frame.grid(row=0, column=0, sticky='news')

tk.Label(register_frame, text="Register", font=('Arial', 16)).pack(pady=10)
reg_username = tk.StringVar()
reg_password = tk.StringVar()

tk.Label(register_frame, text="Username").pack()
tk.Entry(register_frame, textvariable=reg_username).pack()
tk.Label(register_frame, text="Password").pack()
tk.Entry(register_frame, textvariable=reg_password, show="*").pack()

tk.Button(register_frame, text="Daftar", command=register).pack(pady=10)
tk.Button(register_frame, text="Kembali", command=lambda: show_frame(login_frame)).pack()

# ============ Frame To-Do List ============
todo_frame = tk.Frame(root)
todo_frame.grid(row=0, column=0, sticky='news')

tk.Label(todo_frame, text="To-Do List", font=('Arial', 16)).pack(pady=10)
task_entry = tk.Entry(todo_frame, width=30)
task_entry.pack()

tk.Button(todo_frame, text="Tambah Tugas", command=add_task).pack(pady=5)
tk.Button(todo_frame, text="Hapus Tugas", command=delete_task).pack()

task_listbox = tk.Listbox(todo_frame, width=40)
task_listbox.pack(pady=10)

tk.Button(todo_frame, text="Logout", command=logout).pack()

# Tampilkan frame login saat program pertama dijalankan
show_frame(login_frame)

# Jalankan aplikasi utama Tkinter
root.mainloop()

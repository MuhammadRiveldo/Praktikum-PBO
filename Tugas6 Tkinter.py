import tkinter as tk
from tkinter import messagebox  # Untuk menampilkan pesan pop-up

# Dictionary untuk menyimpan data user (username: password)
users = {}

# Fungsi untuk membuka jendela registrasi
def open_register_window():
    reg_win = tk.Toplevel(root)  # Membuat jendela baru (popup)
    reg_win.title("Register")  # Judul jendela
    reg_win.geometry("300x150")  # Ukuran jendela

    # Label dan Entry untuk username
    tk.Label(reg_win, text="Username:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
    username_entry = tk.Entry(reg_win)
    username_entry.grid(row=0, column=1)

    # Label dan Entry untuk password
    tk.Label(reg_win, text="Password:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
    password_entry = tk.Entry(reg_win, show="*")
    password_entry.grid(row=1, column=1)

    # Fungsi untuk mendaftarkan user baru
    def register_user():
        username = username_entry.get()
        password = password_entry.get()
        if username and password:  # Cek jika field tidak kosong
            if username in users:  # Cek jika username sudah terdaftar
                messagebox.showerror("Error", "Username sudah terdaftar")
            else:
                users[username] = password  # Simpan user baru
                messagebox.showinfo("Registrasi berhasil", "Kamu telah terdaftar")
                reg_win.destroy()  # Tutup jendela registrasi
        else:
            messagebox.showwarning("Warning", "Tolong isi semua field")

    # Tombol Register
    tk.Button(reg_win, text="Register", command=register_user).grid(row=2, columnspan=2, pady=10)


# Fungsi untuk membuka jendela to-do list setelah login berhasil
def open_todolist(username):
    todo_win = tk.Toplevel(root)
    todo_win.title("To-Do List - " + username)
    todo_win.geometry("400x300")

    tasks = []  # List untuk menyimpan tugas

    # Entry untuk input tugas baru
    task_entry = tk.Entry(todo_win, width=30)
    task_entry.pack(pady=10)

    # Listbox untuk menampilkan daftar tugas
    task_listbox = tk.Listbox(todo_win, width=50)
    task_listbox.pack()

    # Fungsi untuk menambahkan tugas
    def add_task():
        task = task_entry.get()
        if task:
            tasks.append(task)  # Tambahkan ke list
            task_listbox.insert(tk.END, task)  # Tampilkan di Listbox
            task_entry.delete(0, tk.END)  # Bersihkan Entry

    # Fungsi untuk menghapus tugas yang dipilih
    def remove_task():
        selected = task_listbox.curselection()  # Ambil indeks tugas yang dipilih
        if selected:
            index = selected[0]
            task_listbox.delete(index)  # Hapus dari Listbox
            tasks.pop(index)  # Hapus dari list asli

    # Tombol untuk menambah dan menghapus tugas
    tk.Button(todo_win, text="Tambah tugas", command=add_task).pack(pady=5)
    tk.Button(todo_win, text="Hapus tugas", command=remove_task).pack()


# Fungsi untuk login user
def login_user():
    username = username_var.get()
    password = password_var.get()
    if username in users and users[username] == password:
        messagebox.showinfo("Login Berhasil", f"Selamat Datang, {username}!")
        open_todolist(username)  # Buka jendela to-do list
    else:
        messagebox.showerror("Login Gagal", "Username atau password salah")


# ---------- GUI Utama ----------
root = tk.Tk()
root.title("Login")
root.geometry("300x150")

# Label dan Entry untuk username
tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
username_var = tk.StringVar()
tk.Entry(root, textvariable=username_var).grid(row=0, column=1)

# Label dan Entry untuk password
tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
password_var = tk.StringVar()
tk.Entry(root, textvariable=password_var, show="*").grid(row=1, column=1)

# Tombol Login dan Register
tk.Button(root, text="Login", command=login_user).grid(row=2, column=0, pady=10)
tk.Button(root, text="Register", command=open_register_window).grid(row=2, column=1)

# Jalankan GUI utama
root.mainloop()

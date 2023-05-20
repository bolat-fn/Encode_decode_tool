import os
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import filedialog, messagebox
import base64

def encrypt_folder(folder_path, key):
    f = Fernet(key)
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, "rb") as file_to_encrypt:
                data = file_to_encrypt.read()
            encrypted_data = f.encrypt(data)
            with open(file_path, "wb") as encrypted_file:
                encrypted_file.write(encrypted_data)

def decrypt_folder(folder_path, key):
    f = Fernet(key)
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, "rb") as encrypted_file:
                encrypted_data = encrypted_file.read()
            decrypted_data = f.decrypt(encrypted_data)
            with open(file_path, "wb") as decrypted_file:
                decrypted_file.write(decrypted_data)

def generate_key():
    key = Fernet.generate_key()
    print("Oluşturulan Anahtar:", key.decode())
    return key

def encrypt_decrypt_folder():
    selected_option = option_var.get()
    folder_path = filedialog.askdirectory()
    if folder_path:
        if selected_option == 1:
            key = generate_key()
            encrypt_folder(folder_path, key)
            messagebox.showinfo("Şifreleme Tamamlandı", "Klasör başarıyla şifrelendi!")
        elif selected_option == 0:
            key = key_entry.get()
            decrypt_folder(folder_path, key)
            messagebox.showinfo("Deşifre Etme Tamamlandı", "Klasör başarıyla deşifre edildi!")
    else:
        messagebox.showerror("Hata", "Klasör seçilmedi!")

# Ana pencere oluştur
window = tk.Tk()
window.title("Klasör Şifreleme ve Deşifreleme Aracı")
window.configure(bg="#f0f0f0")

# Başlık etiketi
title_label = tk.Label(window, text="Klasör Şifreleme ve Deşifreleme Aracı", font=("Arial", 14, "bold"), bg="#f0f0f0")
title_label.pack(pady=20)

# İşlem seçenekleri çerçevesi
option_frame = tk.LabelFrame(window, text="İşlem Seçin", font=("Arial", 12), bg="#f0f0f0")
option_frame.pack(pady=10)

# İşlem seçenekleri
option_var = tk.IntVar()
encrypt_radio = tk.Radiobutton(option_frame, text="Klasörü Şifrele", variable=option_var, value=1, font=("Arial", 12), bg="#f0f0f0")
encrypt_radio.pack(pady=5)
decrypt_radio = tk.Radiobutton(option_frame, text="Klasörü Deşifre Et", variable=option_var, value=0, font=("Arial", 12), bg="#f0f0f0")
decrypt_radio.pack(pady=5)

# Anahtar girişi çerçevesi
key_frame = tk.LabelFrame(window, text="Anahtar", font=("Arial", 12), bg="#f0f0f0")
key_frame.pack(pady=10)


# Anahtar giriş etiketi ve giriş kutusu
key_label = tk.Label(key_frame, text="Anahtar:", font=("Arial", 12), bg="#f0f0f0")
key_label.pack(side="left", padx=10)

key_entry = tk.Entry(key_frame, show="*", font=("Arial", 12))
key_entry.pack(side="left")

# Klasör seçme düğmesi
folder_button = tk.Button(window, text="Klasör Seç", command=encrypt_decrypt_folder, font=("Arial", 12))
folder_button.pack(pady=10)

# Ana döngüyü başlat
window.mainloop()
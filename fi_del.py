import os
import tkinter as tk
from tkinter import filedialog

def delete_files_by_extension():
    folder_path = folder_path_var.get()
    extension = extension_var.get()

    try:
        # Проверяем, существует ли указанная папка
        if not os.path.exists(folder_path):
            status_label.config(text=f"Папка {folder_path} не существует.", fg="red")
            return

        # Получаем список файлов в папке
        files = os.listdir(folder_path)

        # Фильтруем файлы по расширению
        target_files = [file for file in files if file.endswith(extension)]

        if not target_files:
            status_label.config(text=f"В папке {folder_path} нет файлов с расширением {extension}.", fg="red")
            return

        # Удаление файлов
        for file_name in target_files:
            file_path = os.path.join(folder_path, file_name)
            os.remove(file_path)

        status_label.config(text=f"Удалено {len(target_files)} файлов с расширением {extension} из папки {folder_path}.", fg="green")

    except Exception as e:
        status_label.config(text=f"Произошла ошибка: {e}", fg="red")

def browse_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_path_var.set(folder_path)

# Создание главного окна приложения
root = tk.Tk()
root.title("Удаление файлов по типу")

# Переменные для хранения пути к папке и расширению файла
folder_path_var = tk.StringVar()
extension_var = tk.StringVar()

# Создание элементов интерфейса
folder_label = tk.Label(root, text="Выберите папку:")
folder_label.pack()

folder_entry = tk.Entry(root, textvariable=folder_path_var, width=50)
folder_entry.pack()

browse_button = tk.Button(root, text="Обзор", command=browse_folder)
browse_button.pack()

extension_label = tk.Label(root, text="Введите расширение файла:")
extension_label.pack()

extension_entry = tk.Entry(root, textvariable=extension_var, width=10)
extension_entry.pack()

delete_button = tk.Button(root, text="Удалить файлы", command=delete_files_by_extension)
delete_button.pack()

status_label = tk.Label(root, text="", fg="green")
status_label.pack()

root.mainloop()
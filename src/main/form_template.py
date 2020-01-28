import tkinter as tk


def show(width, height):
    root = tk.Tk()
    root.title("Мониторинг IP-адресов")
    
    # Вычисление середины экрана монитора
    screen_width = root.winfo_screenwidth()  # ширина экрана
    screen_height = root.winfo_screenheight()  # высота экрана

    # Левая верхняя точка окна
    screen_width = screen_width // 2
    screen_height = screen_height // 2

    # Смещение от середины по ширине и высоте
    screen_width = screen_width - (width // 2)
    screen_height = screen_height - (height // 2)

    # Размещение
    root.geometry('{}x{}+{}+{}'.format(width, height, screen_width, screen_height))

    root.mainloop()


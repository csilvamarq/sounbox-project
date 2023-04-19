import os
import time

def main():
    folder_name = "spanish"

    while True:
        message = input("Escribe tu mensaje: ")
        filename = f'{time.strftime("%Y%m%d-%H%M%S")}.txt'
        file_path = os.path.join(folder_name, filename)
        with open(file_path, "w") as f:
            f.write(message)

        print(f"El mensaje ha sido guardado en el archivo {filename}.")

if __name__ == "__main__":
    main()
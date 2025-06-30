
import numpy as np
import matplotlib.pyplot as plt

def main():
    print("=== Aplikasi Pertumbuhan Bakteri - Regresi Polinomial ===")
    print("Masukkan data waktu (jam) dan jumlah bakteri (pisahkan dengan koma)\n")

    # Input data dari user
    waktu_input = input("Waktu (contoh: 0,1,2,3,4): ")
    bakteri_input = input("Jumlah Bakteri (contoh: 100,150,210,250,190): ")

    try:
        waktu = np.array([float(x) for x in waktu_input.split(',')])
        bakteri = np.array([float(x) for x in bakteri_input.split(',')])

        if len(waktu) != len(bakteri):
            print("Jumlah elemen waktu dan bakteri harus sama!")
            return

        # Regresi polinomial derajat 2
        koef = np.polyfit(waktu, bakteri, deg=2)
        model = np.poly1d(koef)

        print(f"\nPersamaan: y = {koef[0]:.2f}x² + {koef[1]:.2f}x + {koef[2]:.2f}")

        # Grafik
        x_line = np.linspace(min(waktu), max(waktu), 100)
        y_line = model(x_line)

        plt.scatter(waktu, bakteri, color='blue', label='Data Asli')
        plt.plot(x_line, y_line, color='red', label=f'Regresi: {model}')
        plt.title('Pertumbuhan Bakteri')
        plt.xlabel('Waktu (jam)')
        plt.ylabel('Jumlah Bakteri')
        plt.grid(True)
        plt.legend()
        plt.show()

    except Exception as e:
        print(f"Terjadi error: {e}")

if __name__ == "__main__":
    main()































































































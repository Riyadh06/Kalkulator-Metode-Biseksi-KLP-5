"""
Ujian Tengah Semester
Kelompok 5
Anggota: Andre Alfaridzi (2408107010011)
        Muhammad Riyadh (2408107010015)
        Hani Huriyah Ahmad (2408107010020)
        Meurahmah Nushsharie (2408107010035)
        Urfan (2408107010038)
"""
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QFormLayout, QLabel, 
                             QLineEdit, QPushButton, QTableWidget, 
                             QTableWidgetItem, QDesktopWidget, QMessageBox,
                             QHeaderView)
from sympy import symbols, sympify, SympifyError

class BisectionCalculator(QWidget):
    """
    Kelas utama untuk aplikasi Kalkulator Metode Biseksi.
    Mengelola semua elemen UI dan logika aplikasi.
    """
    def __init__(self):
        super().__init__()
        self._initialize_ui()

    def _initialize_ui(self):
        """Menginisialisasi seluruh antarmuka pengguna (UI)."""
        self._setup_window()
        self._create_widgets()
        self._setup_layout()
        self._apply_styles()
        self._connect_signals()
        self.center_window()

    def _setup_window(self):
        """Mengatur properti dasar jendela aplikasi."""
        self.setGeometry(0, 0, 900, 550)
        self.setWindowTitle('Kalkulator Metode Biseksi ')

    def center_window(self):
        """Memposisikan jendela aplikasi di tengah layar."""
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def _create_widgets(self):
        """Membuat semua widget yang dibutuhkan untuk UI."""

        self.pers_label = QLabel("Masukkan persamaan:")
        self.input_pers = QLineEdit()
        self.input_pers.setPlaceholderText("Contoh: x**3 + 2*x**2 + 3*x - 4 ")

        self.a_label = QLabel("Nilai tebakan a:")
        self.input_a = QLineEdit()

        self.b_label = QLabel("Nilai tebakan b:")
        self.input_b = QLineEdit()

        self.tolerance_label = QLabel("Nilai toleransi error (e):")
        self.input_tolerance = QLineEdit()

        self.iterations_label = QLabel("Jumlah maksimum iterasi (N):")
        self.input_iterasi = QLineEdit()

        # --- Buttons ---
        self.tombol_hitung = QPushButton("Hitung")
        self.tombol_hapus = QPushButton("Hapus")
        self.tombol_hapus.setObjectName("tombol_hapus")

        # --- Results Table ---
        self.table = QTableWidget()
        self.table.setColumnCount(9)
        self.table.setHorizontalHeaderLabels(['Iterasi', 'a', 'b', 'f(a)', 'f(b)', 'x', 'f(x)', 'f(x) * f(a)', '|b - a|'])
        # Mengatur agar lebar kolom menyesuaikan isi
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    
    def _setup_layout(self):
        """Mengatur tata letak widget dalam form layout."""
        layout = QFormLayout(self)
        layout.setSpacing(10)
        
        layout.addRow(self.pers_label, self.input_pers)
        layout.addRow(self.a_label, self.input_a)
        layout.addRow(self.b_label, self.input_b)
        layout.addRow(self.tolerance_label, self.input_tolerance)
        layout.addRow(self.iterations_label, self.input_iterasi)
        layout.addRow(self.tombol_hapus, self.tombol_hitung)
        layout.addRow(self.table)
        
        self.setLayout(layout)

    def _connect_signals(self):
        """Menghubungkan sinyal (seperti klik tombol) ke slot (metode)."""
        self.tombol_hitung.clicked.connect(self._handle_calculation)
        self.tombol_hapus.clicked.connect(self._clear_table)

    def _apply_styles(self):
        stylesheet = """
            QWidget {
                background-color: #2E3B4E;
                color: #F0F0F0;
                font-family: Arial, sans-serif;
            }
            QLabel { font-size: 14px; padding-top: 5px; }
            QLineEdit {
                background-color: #455364; border: 1px solid #566573;
                border-radius: 5px; padding: 6px; font-size: 14px;
            }
            QPushButton {
                background-color: #50A8E0; color: white; border: none;
                border-radius: 5px; padding: 8px 16px;
                font-size: 14px; font-weight: bold;
            }
            QPushButton:hover { background-color: #60B8F0; }
            #tombol_hapus { background-color: #E74C3C; }
            #tombol_hapus:hover { background-color: #F75C4C; }
            QTableWidget {
                background-color: #455364; gridline-color: #566573;
                border-radius: 5px; font-size: 13px;
            }
            QHeaderView::section {
                background-color: #566573; color: white; padding: 5px;
                border: 1px solid #2E3B4E; font-weight: bold;
            }
        """
        self.setStyleSheet(stylesheet)

    # --- Event Handlers and Logic ---

    def _clear_table(self):
        """Membersihkan isi tabel hasil."""
        self.table.setRowCount(0)

    def _handle_calculation(self):
        """
        Menangani event klik tombol "Hitung".
        Mengambil input, memvalidasi, memanggil kalkulasi, dan menampilkan hasil.
        """
        try:
            # 1. Mengambil dan memvalidasi input
            fungsi_str = self.input_pers.text()
            a = float(self.input_a.text())
            b = float(self.input_b.text())
            e = float(self.input_tolerance.text())
            n = int(self.input_iterasi.text())

            if not fungsi_str:
                raise ValueError("Persamaan tidak boleh kosong.")

            # 2. Mem-parsing fungsi
            x = symbols('x')
            rumus = sympify(fungsi_str.replace('^', '**'))
            f = lambda val: float(rumus.subs(x, val))

            # 3. Menjalankan algoritma biseksi
            data = self._perform_bisection(f, a, b, e, n)
            
            # 4. Menampilkan data ke tabel
            self._populate_table(data)
            
            # 5. Menampilkan pesan hasil akhir
            self._show_final_result(data, e)

        except (ValueError, TypeError) as ve:
            QMessageBox.critical(self, "Input Error", f"Terjadi kesalahan pada input: {ve}")
        except SympifyError:
            QMessageBox.critical(self, "Input Error", "Format persamaan tidak valid.")
        except Exception as ex:
            QMessageBox.critical(self, "Error", str(ex))

    def _perform_bisection(self, f, a, b, e, n):
        """
        Logika inti dari Metode Biseksi.
        Fungsi ini hanya melakukan perhitungan, tidak berinteraksi dengan UI.
        """
        if f(a) * f(b) > 0:
            raise ValueError("Tidak ada akar pada selang ini (f(a) * f(b) > 0).")

        data = []
        i = 1
        while i <= n:
            xr = (a + b) / 2.0
            fa = f(a)
            fxr = f(xr)

            data.append([i, a, b, fa, f(b), xr, fxr, fxr * fa, abs(b - a)])

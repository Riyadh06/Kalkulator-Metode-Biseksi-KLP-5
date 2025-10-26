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

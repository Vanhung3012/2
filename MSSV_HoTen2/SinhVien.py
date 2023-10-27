class SinhVien:
    def __init__(self, mssv: int = None, hoTen: str = None, lop: str = None, diemTB: float = None):
        self.mssv = mssv
        self.hoTen = hoTen
        self.lop = lop
        self.diemTB = diemTB

    def __str__(self) -> str:
        return "{0} {1} {2} {3}".format(self.mssv, self.hoTen, self.lop, self.diemTB)

    def Xuat(self):
        print(self)

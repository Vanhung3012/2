from SinhVien import SinhVien
import pandas as pd


class DanhSachSinhVien:
    def __init__(self):
        self.danhSach = []

    def Them(self, sinhVien: SinhVien) -> None:
        self.danhSach.append(sinhVien)

    def Xoa(self, mssv: str) -> None:
        self.danhSach = [sv for sv in self.danhSach if sv.mssv != mssv]

    def CapNhat(self, sinhVien: SinhVien) -> None:
        for i, sv in enumerate(self.danhSach):
            if sv.mssv == sinhVien.mssv:
                self.danhSach[i].hoTen = sinhVien.hoTen
                self.danhSach[i].lop = sinhVien.lop
                self.danhSach[i].diemTB = sinhVien.diemTB

    def Chen(self, sinhVien: SinhVien, i: int) -> None:
        self.danhSach = self.danhSach[:i+1] + [sinhVien] + self.danhSach[i+1:]

    def TimKiemTheoMaSV(self, mssv: int) -> SinhVien:
        return [sv for sv in self.danhSach if sv.maSo == mssv]

    def SapXep(self) -> None:
        self.danhSach = self.danhSach.sort(
            key=lambda sv: sv.maSo, reverse=False)

    def DocTuFileText(self):
        with open('data.csv', 'r') as f:
            for i, line in enumerate(f.readlines()):
                if i > 0:
                    sv = SinhVien()
                    arr = line.split(',')
                    sv.maSo = arr[0]
                    sv.hoTen = arr[1]
                    sv.lop = arr[2]
                    sv.diemTB = arr[3]
                    self.Them(sv)

    def DocTuExcel(self):
        df = pd.read_excel(
            r'E:\Máy tính\HỌC KỲ I NĂM 3\LẬP TRÌNH PYTHON\Ôn tập Ktra\MSSV_HoTen2\data.xlsx')
        for i in range(len(df)):
            sv = SinhVien()
            row = df.iloc[i]
            sv.mssv = row['maSo']
            sv.hoTen = row['hoTen']
            sv.lop = row['lop']
            sv.diemTB = row['diemTB']
            self.Them(sv)

    def DocTuJson(self):
        df = pd.read_json('data.json')
        for i in range(len(df)):
            sv = SinhVien()
            row = df.iloc[i]
            sv.maSo = row['maSo']
            sv.hoTen = row['hoTen']
            sv.lop = row['lop']
            sv.diemTB = row['diemTB']
            self.Them(sv)

    def __str__(self) -> str:
        kq = ''
        for sv in self.danhSach:
            kq += f'{sv}\n'
        return kq

    def Xuat(self):
        print(self)

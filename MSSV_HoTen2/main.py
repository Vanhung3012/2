# Import các thư viện và modules cần thiết
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import matplotlib
import matplotlib.pyplot as plt
import pandas
# Import class DanhSachSinhVien từ module DanhSachSinhVien
from DanhSachSinhVien import DanhSachSinhVien
from SinhVien import SinhVien

# Khởi tạo một đối tượng DanhSachSinhVien và đọc dữ liệu từ file Excel
dssv = DanhSachSinhVien()
dssv.DocTuExcel()

# Hàm xử lý sự kiện khi nút "Đọc File" được nhấn


def btnClick():
    HienThiTreeView()  # Hiển thị danh sách sinh viên trong Treeview
    # tk.messagebox.showerror(title='Lỗi!', message='Đọc thất bại!')  # Hiển thị thông báo lỗi

# Hàm để hiển thị danh sách sinh viên trong Treeview


def HienThiTreeView():
    for row in tree.get_children():
        tree.delete(row)
    for sv in dssv.danhSach:
            tree.insert("", "end", values=(sv.mssv, sv.hoTen, sv.lop, sv.diemTB))


def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        txt_MaSo.delete(0, END)
        txt_HoTen.delete(0, END)
        txt_Lop.delete(0, END)
        txt_DiemTB.delete(0,END)


        txt_MaSo.insert(0, item['values'][0])
        txt_HoTen.insert(0,item['values'][1])
        txt_Lop.insert(0,item['values'][2])
        txt_DiemTB.insert(0,item['values'][3])

def btnThemClick():
    mssv = txt_MaSo.get()
    hoTen = txt_HoTen.get()
    lop = txt_Lop.get()
    diemTB = txt_DiemTB.get()
    dssv.Them(SinhVien(mssv, hoTen, lop, diemTB))
    HienThiTreeView()

def btnCapNhatClick():
    mssv = txt_MaSo.get()
    hoTen = txt_HoTen.get()
    lop = txt_Lop.get()
    diemTB = txt_DiemTB.get()
    dssv.CapNhat(SinhVien(mssv, hoTen, lop, diemTB))
    HienThiTreeView()

def btnXoaClick():
    mssv = txt_MaSo.get()
    dssv.Xoa(mssv)
    HienThiTreeView()

# Hàm để vẽ biểu đồ cột dựa trên điểm trung bình của sinh viên


def VeDiemTB():
    x = [sv.hoTen for sv in dssv.danhSach]
    y = [sv.diemTB for sv in dssv.danhSach]
    plt.bar(x, y)
    plt.show()

# Hàm để vẽ biểu đồ đường


def VeBieuDoDuong():
    x = [sv.hoTen for sv in dssv.danhSach]
    y = [sv.diemTB for sv in dssv.danhSach]
    plt.plot(x, y, marker='o')
    plt.xlabel('X Label')
    plt.ylabel('Y Label')
    plt.title('Biểu đồ đường')
    plt.grid()
    plt.show()

# Hàm để vẽ biểu đồ phân tán (scatter plot)


def VeBieuDoPhanTan():
    x = [sv.hoTen for sv in dssv.danhSach]
    y = [sv.diemTB for sv in dssv.danhSach]
    plt.scatter(x, y, c='r', label='Dữ liệu')
    plt.xlabel('X Label')
    plt.ylabel('Y Label')
    plt.title('Biểu đồ phân tán')
    plt.legend()
    plt.grid()
    plt.show()


# Tạo cửa sổ giao diện chính
root = tk.Tk()
root.title("Form Sinh Viên")

# Tạo label, ô nhập và nút "Đọc File"
lbl = tk.Label(root, text='Nhập Đường Dẫn')
txt = tk.Entry(root)
btn = tk.Button(root, text='Đọc File', command=btnClick)
btn_Line = tk.Button(root, text='Biểu Đồ Cột', command=VeDiemTB)

tree = ttk.Treeview(root, columns=(
    "mssv", "hoTen", "lop", "diemTB"), show='headings')
tree.heading('mssv', text="Mã Số")
tree.heading('hoTen', text="Họ tên")
tree.heading('lop', text="Lớp")
tree.heading('diemTB', text="Điểm TB")
tree.bind('<<TreeviewSelect>>', item_selected)

# Tạo nút để vẽ biểu đồ đường
btn_BieuDoDuong = tk.Button(root, text='Biểu Đồ Đường', command=VeBieuDoDuong)

# Tạo nút để vẽ biểu đồ phân tán
btn_BieuDoPhanTan = tk.Button(
    root, text='Biểu Đồ Phân Tán', command=VeBieuDoPhanTan)

# Bổ sung Label và ô nhập cho Mã Số, Họ Tên, Lớp, Điểm TB
lbl_MaSo = tk.Label(root, text='Mã Số')
txt_MaSo = tk.Entry(root)
lbl_HoTen = tk.Label(root, text='Họ Tên')
txt_HoTen = tk.Entry(root)
lbl_Lop = tk.Label(root, text='Lớp')
txt_Lop = tk.Entry(root)
lbl_DiemTB = tk.Label(root, text='Điểm TB')
txt_DiemTB = tk.Entry(root)

# Bổ sung các nút Thêm, Xóa, Cập Nhật, Sắp Xếp
btn_Them = tk.Button(root, text='Thêm', command=btnThemClick)
btn_Xoa = tk.Button(root, text='Xóa', command=btnXoaClick)
btn_CapNhat = tk.Button(root, text='Cập Nhật', command=btnCapNhatClick)
btn_SapXep = tk.Button(root, text='Sắp Xếp', command=dssv.CapNhat)

# Đặt các phần tử GUI vào cửa sổ giao diện
lbl.grid(row=0, column=0)
txt.grid(row=0, column=1)
btn.grid(row=0, column=2)
btn_Line.grid(row=1, column=0)
btn_BieuDoDuong.grid(row=1, column=1)
btn_BieuDoPhanTan.grid(row=1, column=2)
tree.grid(row=2, columnspan=3)

# Đặt các phần tử GUI mới vào vị trí tương ứng
lbl_MaSo.grid(row=4, column=0)
txt_MaSo.grid(row=4, column=1)
lbl_HoTen.grid(row=5, column=0)
txt_HoTen.grid(row=5, column=1)
lbl_Lop.grid(row=6, column=0)
txt_Lop.grid(row=6, column=1)
lbl_DiemTB.grid(row=7, column=0)
txt_DiemTB.grid(row=7, column=1)

btn_Them.grid(row=4, column=2)
btn_Xoa.grid(row=5, column=2)
btn_CapNhat.grid(row=6, column=2)
btn_SapXep.grid(row=7, column=2)

# Khởi chạy ứng dụng
root.mainloop()

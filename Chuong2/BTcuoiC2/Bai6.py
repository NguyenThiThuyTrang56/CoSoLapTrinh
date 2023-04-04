Ho_ten=input("Ho ten: ")
Ngay_cong=int(input("So ngay cong: "))
Don_gia_ngay_cong=int(input("Don gia ngay cong: "))
He_so_phu_cap=float(input("He so phu cap: "))
Tien_tam_ung=int(input("Tam ung: "))
Luong=(Don_gia_ngay_cong*Ngay_cong*He_so_phu_cap)
Thuc_linh=(Luong-Tien_tam_ung)
print("Nhan vien ",Ho_ten,", Co tien luong=",Luong,", Tam ung=",Tien_tam_ung," va Thuc linh=",Thuc_linh,sep="")
                    
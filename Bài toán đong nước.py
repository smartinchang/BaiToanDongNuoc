DungTich = [3, 5, 9]
TrangThai = [[0, 0, 0, 0, 0]]

# Hàm kiểm tra xem trạng thái đã có chưa
def TimKiem(TrangThaiCanTim):
    KetQua = False
    for i in range (0, len(TrangThai)):
        if (TrangThaiCanTim == TrangThai[i][2 : 5]):
            KetQua = True
    return KetQua

# Hàm kiểm tra bài toán đã được giải chưa
def BaiToan(TrangThaiCanKiemTra):
    if (TrangThaiCanKiemTra[0] == 1) and (TrangThaiCanKiemTra[2] == 7):
    #if (TrangThaiCanKiemTra[2] == 9):
        return True
    else:
        return False

ViTriHienTai = 0
TiepTuc = True
GiaiDuoc = False

while (TiepTuc == True):
    TrangThaiHienTai = TrangThai[ViTriHienTai][2 : 5]
    # Hành động 01: Đổ nước đầy bình 1
    if (TiepTuc == True):
        TrangThaiMoi = [DungTich[0], TrangThaiHienTai[1], TrangThaiHienTai[2]]
        if (TimKiem(TrangThaiMoi) == False):
            TrangThai.append([ViTriHienTai, 1, TrangThaiMoi[0], TrangThaiMoi[1], TrangThaiMoi[2]])
            if (BaiToan(TrangThaiMoi) == True):
                TiepTuc = False
                GiaiDuoc = True
    # Hành động 02: Đổ hết nước trong bình 1
    if (TiepTuc == True):
        TrangThaiMoi = [0, TrangThaiHienTai[1], TrangThaiHienTai[2]]
        if (TimKiem(TrangThaiMoi) == False):
            TrangThai.append([ViTriHienTai, 2, TrangThaiMoi[0], TrangThaiMoi[1], TrangThaiMoi[2]])
            if (BaiToan(TrangThaiMoi) == True):
                TiepTuc = False
                GiaiDuoc = True
    # Hành động 03: Đổ nước từ bình 1 qua bình 2
    if (TiepTuc == True):
        if ((TrangThaiHienTai[0] > 0) and (DungTich[1] - TrangThaiHienTai[1] > 0)):
            if (TrangThaiHienTai[0] > (DungTich[1] - TrangThaiHienTai[1])):
                TrangThaiMoi = [TrangThaiHienTai[0] - DungTich[1] + TrangThaiHienTai[1], DungTich[1], TrangThaiHienTai[2]]
            else:
                TrangThaiMoi = [0, TrangThaiHienTai[1] + TrangThaiHienTai[0], TrangThaiHienTai[2]]
        if (TimKiem(TrangThaiMoi) == False):
            TrangThai.append([ViTriHienTai, 3, TrangThaiMoi[0], TrangThaiMoi[1], TrangThaiMoi[2]])
            if (BaiToan(TrangThaiMoi) == True):
                TiepTuc = False
                GiaiDuoc = True
    # Hành động 05: Đổ nước đầy bình 2
    if (TiepTuc == True):
        TrangThaiMoi = [TrangThaiHienTai[0], DungTich[1], TrangThaiHienTai[2]]
        if (TimKiem(TrangThaiMoi) == False):
            TrangThai.append([ViTriHienTai, 5, TrangThaiMoi[0], TrangThaiMoi[1], TrangThaiMoi[2]])
            if (BaiToan(TrangThaiMoi) == True):
                TiepTuc = False
                GiaiDuoc = True
    # Hành động 06: Đổ hết nước trong bình 2
    if (TiepTuc == True):
        TrangThaiMoi = [TrangThaiHienTai[0], 0, TrangThaiHienTai[2]]
        if (TimKiem(TrangThaiMoi) == False):
            TrangThai.append([ViTriHienTai, 6, TrangThaiMoi[0], TrangThaiMoi[1], TrangThaiMoi[2]])
            if (BaiToan(TrangThaiMoi) == True):
                TiepTuc = False
                GiaiDuoc = True
    # Hành động 07: Đổ nước từ bình 2 qua bình 1
    if (TiepTuc == True):
        if ((TrangThaiHienTai[1] > 0) and (DungTich[0] - TrangThaiHienTai[0] > 0)):
            if (TrangThaiHienTai[1] > (DungTich[0] - TrangThaiHienTai[0])):
                TrangThaiMoi = [DungTich[0], TrangThaiHienTai[1] - DungTich[0] + TrangThaiHienTai[0], TrangThaiHienTai[2]]
            else:
                TrangThaiMoi = [TrangThaiHienTai[0] + TrangThaiHienTai[1], 0, TrangThaiHienTai[2]]
        if (TimKiem(TrangThaiMoi) == False):
            TrangThai.append([ViTriHienTai, 7, TrangThaiMoi[0], TrangThaiMoi[1], TrangThaiMoi[2]])
            if (BaiToan(TrangThaiMoi) == True):
                TiepTuc = False
                GiaiDuoc = True
    # Hành động 08: Đổ nước từ bình 2 qua bình 3
    if (TiepTuc == True):
        if ((TrangThaiHienTai[1] > 0) and (DungTich[2] - TrangThaiHienTai[2] > 0)):
            if (TrangThaiHienTai[1] > (DungTich[2] - TrangThaiHienTai[2])):
                TrangThaiMoi = [TrangThaiHienTai[0], TrangThaiHienTai[1] - DungTich[2] + TrangThaiHienTai[2], DungTich[2]]
            else:
                TrangThaiMoi = [TrangThaiHienTai[0], 0, TrangThaiHienTai[2] + TrangThaiHienTai[1]]
        if (TimKiem(TrangThaiMoi) == False):
            TrangThai.append([ViTriHienTai, 8, TrangThaiMoi[0], TrangThaiMoi[1], TrangThaiMoi[2]])
            if (BaiToan(TrangThaiMoi) == True):
                TiepTuc = False
                GiaiDuoc = True
    # Hành động 09: Đổ nước đầy bình 3
    if (TiepTuc == True):
        TrangThaiMoi = [TrangThaiHienTai[0], TrangThaiHienTai[1], DungTich[2]]
        if (TimKiem(TrangThaiMoi) == False):
            TrangThai.append([ViTriHienTai, 9, TrangThaiMoi[0], TrangThaiMoi[1], TrangThaiMoi[2]])
            if (BaiToan(TrangThaiMoi) == True):
                TiepTuc = False
                GiaiDuoc = True
    # Hành động 10: Đổ hết nước trong bình 3
    if (TiepTuc == True):
        TrangThaiMoi = [TrangThaiHienTai[0], TrangThaiHienTai[1], 0]
        if (TimKiem(TrangThaiMoi) == False):
            TrangThai.append([ViTriHienTai, 10, TrangThaiMoi[0], TrangThaiMoi[1], TrangThaiMoi[2]])
            if (BaiToan(TrangThaiMoi) == True):
                TiepTuc = False
                GiaiDuoc = True
    # Hành động 11: Đổ nước từ bình 3 qua bình 1
    if (TiepTuc == True):
        if ((TrangThaiHienTai[2] > 0) and (DungTich[0] - TrangThaiHienTai[0] > 0)):
            if (TrangThaiHienTai[2] > (DungTich[0] - TrangThaiHienTai[0])):
                TrangThaiMoi = [DungTich[0], TrangThaiHienTai[1], TrangThaiHienTai[2] - DungTich[0] + TrangThaiHienTai[0]]
            else:
                TrangThaiMoi = [TrangThaiHienTai[0] + TrangThaiHienTai[2], TrangThaiHienTai[1], 0]
        if (TimKiem(TrangThaiMoi) == False):
            TrangThai.append([ViTriHienTai, 11, TrangThaiMoi[0], TrangThaiMoi[1], TrangThaiMoi[2]])
            if (BaiToan(TrangThaiMoi) == True):
                TiepTuc = False
                GiaiDuoc = True
    # Hành động 12: Đổ nước từ bình 3 qua bình 2
    if (TiepTuc == True):
        if ((TrangThaiHienTai[2] > 0) and (DungTich[1] - TrangThaiHienTai[1] > 0)):
            if (TrangThaiHienTai[2] > (DungTich[1] - TrangThaiHienTai[1])):
                TrangThaiMoi = [TrangThaiHienTai[0], DungTich[1], TrangThaiHienTai[2] - DungTich[1] + TrangThaiHienTai[1]]
            else:
                TrangThaiMoi = [TrangThaiHienTai[0], TrangThaiHienTai[1] + TrangThaiHienTai[2], 0]
        if (TimKiem(TrangThaiMoi) == False):
            TrangThai.append([ViTriHienTai, 12, TrangThaiMoi[0], TrangThaiMoi[1], TrangThaiMoi[2]])
            if (BaiToan(TrangThaiMoi) == True):
                TiepTuc = False
                GiaiDuoc = True
    if (TiepTuc == True):
        ViTriHienTai += 1
        if (ViTriHienTai > len(TrangThai)):
            TiepTuc = False

if (GiaiDuoc == True):
    print("Tìm được lời giải như sau:")
    TiepTuc = True
    ViTriHienTai = len(TrangThai) - 1
    LoiGiai = []
    while (TiepTuc == True):
        TrangThaiHienTai = TrangThai[ViTriHienTai]
        LoiGiai.insert(0, TrangThaiHienTai)
        ViTriHienTai = TrangThaiHienTai[0]
        if (ViTriHienTai == 0):
            TiepTuc = False
    for i in range (0, len(LoiGiai)):
        if (LoiGiai[i][1] == 1):
            print("- Đổ đầy nước vào bình 1, ta được      ", LoiGiai[i][2],LoiGiai[i][3],LoiGiai[i][4])
        elif (LoiGiai[i][1] == 2):
            print("- Đổ hết nước khỏi bình 1, ta được     ", LoiGiai[i][2],LoiGiai[i][3],LoiGiai[i][4])
        elif (LoiGiai[i][1] == 3):
            print("- Đổ nước từ bình 1 vào bình 2, ta được", LoiGiai[i][2],LoiGiai[i][3],LoiGiai[i][4])
        elif (LoiGiai[i][1] == 4):
            print("- Đổ nước từ bình 1 vào bình 3, ta được", LoiGiai[i][2],LoiGiai[i][3],LoiGiai[i][4])
        elif (LoiGiai[i][1] == 5):
            print("- Đổ đầy nước vào bình 2, ta được      ", LoiGiai[i][2],LoiGiai[i][3],LoiGiai[i][4])
        elif (LoiGiai[i][1] == 6):
            print("- Đổ hết nước khỏi bình 2, ta được     ", LoiGiai[i][2],LoiGiai[i][3],LoiGiai[i][4])
        elif (LoiGiai[i][1] == 7):
            print("- Đổ nước từ bình 2 vào bình 1, ta được", LoiGiai[i][2],LoiGiai[i][3],LoiGiai[i][4])
        elif (LoiGiai[i][1] == 8):
            print("- Đổ nước từ bình 2 vào bình 3, ta được", LoiGiai[i][2],LoiGiai[i][3],LoiGiai[i][4])
        elif (LoiGiai[i][1] == 9):
            print("- Đổ đầy nước vào bình 3, ta được      ", LoiGiai[i][2],LoiGiai[i][3],LoiGiai[i][4])
        elif (LoiGiai[i][1] == 10):
            print("- Đổ hết nước khỏi bình 3, ta được     ", LoiGiai[i][2],LoiGiai[i][3],LoiGiai[i][4])
        elif (LoiGiai[i][1] == 11):
            print("- Đổ nước từ bình 3 vào bình 1, ta được", LoiGiai[i][2],LoiGiai[i][3],LoiGiai[i][4])
        else:
            print("- Đổ nước từ bình 3 vào bình 2, ta được", LoiGiai[i][2],LoiGiai[i][3],LoiGiai[i][4])
else:
    print("Không tìm được lời giải")

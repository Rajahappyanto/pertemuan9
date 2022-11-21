NAMA = []
NIM = []
TUGAS = []
UTS = []
UAS = []
TOTAL = []

while True:
    Nama = input("NAMA :") 
    NAMA.append(Nama)
    Nim = int(input("NIM :"))
    NIM.append(Nim)
    dTugas = float(input("Nilai Tugas :"))
    TUGAS.append(dTugas)
    uts = float(input("Nilai UTS :"))
    UTS.append(uts)
    uas = float(input("Nilai UAS :"))
    UAS.append(uas)

    nAkhir = (int(dTugas) * .3) + (int(uts) * .35) +(int(uas) * .35)
    TOTAL.append(nAkhir)

    lagi =""
    while lagi !="y" and lagi != "t":
        lagi = input("Tambah Data (y/t)?")
    if lagi == "t":
        print("="*70)
        print("|No |\tnama\t  | NIM | TUGAS | UTS | UAS | Akhir |")
        print("="*70)

        for i in range(len(NIM)):
            nm = "| %d. |\t%s\t" % (i+1, NAMA[i])
            im = "    | %d" % NIM[1]
            tg = "    | %.2f" % TUGAS[i]
            ut = "    | %.2f" % UTS[i]
            ua = "    | %.2f" % UAS[i]
            ah = "    | %.2f" % TOTAL[i]
            In = "    |"

            join = nm + im + tg + ut + ua + ah +In 
            print(join)
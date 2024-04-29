gp=int(input("masukan gaji pokok : "))
jk=int(input("masukan jam kerja  :"))

tjg=(20/100)*gp
if jk >200 :
    lembur=20000*(jk-200)
else :
    lembur=0
tunjangan=tjg

pj=(10/100)*gp
total_gj=(gp+lembur)-pj

total_gaji=total_gj
print("-----------------------")
print("gaji pokok : Rp.",gp)
print("jam kerja  : Rp.",jk)
print("tunjangan  : Rp.",tunjangan)
print("lembur     : Rp.",int(lembur))
print("             --------------- +")
print("total gaji : Rp.",int(total_gaji))

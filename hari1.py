uts = {"Ismi","Samanta","Jihan","Nadia","Alya"}
uas = {"Ismi","Samanta","Ode","Marsanda","Nurul"}
print("Yang Memiliki Nilai UTS Diatas 80:", uts)
print("Yang Memiliki Nilai UAS Diatas 80:", uas)
print("_"*100)
#operasi
# Fungsi Fungsi Python Untuk Membuat Program Himpunan

# union() Mengembalikan himpunan yang berisi semua item dari himpunan asli dan semua himpunan yang ditentukan
union_set = uts.union(uas) #gabungan himpunan

#intersection() Mengembalikan himpunan yang berisi kesamaan antara dua himpunan atau lebih
intersection_set = uts.intersection(uas) #irisan himpunan

#Mengembalikan perbedaan simetris dari dua himpunan
symmetric_difference = uts.symmetric_difference(uas) #selisih simetris

#hasil
print('Gabungan Punya Nilai Diatas 80:', union_set)
print('Keduanya diatas 80:', intersection_set)
print('Hanya Salah Satu Diatas 80 :', symmetric_difference)
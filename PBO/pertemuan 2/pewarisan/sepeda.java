package pewarisan;

class sepeda {
    int kecepatan = 0;
    int gir = 0;
    
    void ubahgir(int pertambahangir) {
        gir=gir+pertambahangir;
        System.out.println("Gir : "+gir);
    }
    void tambahkecepatan(int PertambahanKecepatan) {
        kecepatan=kecepatan+PertambahanKecepatan;
        System.out.println("Kecepatan : "+kecepatan);
    }
}

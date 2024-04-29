package mobil;
public class Mobil {
    String warna="Merah";
    String merk="Juke";
    
    void maju(){
        System.out.println("Mobil " + merk + " Warna " + " Bergerak Maju");
    }
    void mundur(){
        System.out.println("Mobil "+ merk + " Warna " + " Bergerak Muundur");
    }
public static void main (String[] args) {
    Mobil mobilsaya = new Mobil();
    mobilsaya.maju();
    mobilsaya.mundur();
    
}
}

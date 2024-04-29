package polymorphism;

class mhs {
    public void tugas() {
        System.out.println("TUgas Mahasiswa Adalah : ");
    }
    
}
class belajar extends mhs {
    public void tugas() {
        System.out.println("1. Belajar");
    }
}
class Tugas extends mhs {
    public void tugas(){
        System.out.println("2. Mengerjakan Tugas");
    }

}

public class Mahasiswa {
    public static void main(String[] args) {
      
        mhs MAHASISWA = new mhs();
        belajar BELAJAR = new belajar();
        Tugas Tugas= new Tugas();

        MAHASISWA.tugas();

        MAHASISWA=BELAJAR;
        MAHASISWA.tugas();

        MAHASISWA=Tugas;
        MAHASISWA.tugas();
    }
}
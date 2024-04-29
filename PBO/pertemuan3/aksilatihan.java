package pertemuan3;

public class aksilatihan {
    public static void main(String[] args) {
        latihan scan = new latihan();

        scan.inputtampilan();
        System.out.println("\n");
        System.out.println("PROGRAM NILAI MAHASISWA");
        System.out.println("--------------------------");
        System.out.println("NIM                 : "+scan.getnim());
        System.out.println("Nama Mahasiswa      : "+scan.getnama());
        System.out.println("Nilai Absen         : "+scan.getabsen());
        System.out.println("Nilai Tugas         : "+scan.gettugas());
        System.out.println("Nilai UTS           : "+scan.getuts());
        System.out.println("Nilai UAS           : "+scan.getuas());
        System.out.println("--------------------------");
        System.out.println("Rata-rata           : "+scan.rata_rata());
    }    
}

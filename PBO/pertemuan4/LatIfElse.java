package pertemuan4;

import java.util.Scanner;

public class LatIfElse {
    public static void main(String[] args) {
        try (Scanner input = new Scanner (System.in)) {
            String Keterangan, nama;
            int nilai;
            
            System.out.print("Masukan nama Siwa : ");
            nama = input.nextLine();
            System.out.print("Masukan Nilai Akhir : ");
            nilai = input.nextInt();
                if(nilai > 70 ){
                    //perintah jika kondisi true
                    Keterangan="Lulus";
                }
                else{
                    Keterangan="Gagal";
                }
            
                System.out.println("Hasil Akhir");
                System.out.println("==========================================");
                System.out.println("Nama Siswa                    :"+nama);
                System.out.println("Nama Nilai akhir yang didapat :"+nilai);
                System.out.println("Keterangan                    :"+Keterangan);
        }
        System.out.println("==========================================");
    }
}

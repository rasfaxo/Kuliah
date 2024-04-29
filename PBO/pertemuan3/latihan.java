package pertemuan3;

import java.util.Scanner;

public class latihan {
    public String nama;
    public int nim;
    public int nilai_absen;
    public int nilai_tugas;
    public int nilai_uts;
    public int nilai_uas;

    Scanner input = new Scanner(System.in);

    public String getnama(){
        return nama;

    }
    public int getnim(){
        return nim;
    }
    public int getabsen(){
        return nilai_absen;
    }
    public int gettugas(){
        return nilai_tugas;
    }
    public int getuts(){
        return nilai_uts;
    }
    public int getuas(){
        return nilai_uas;
    }
    public void inputtampilan() {
        System.out.print("Masukan Nama anda   : ");
        nama=input.nextLine();

        System.out.print("Masukan NIM         : ");
        nim=input.nextInt();

        System.out.print("Masukan Nilai Absen : ");
        nilai_absen=input.nextInt();

        System.out.print("Masukan Nilai Tugas : ");
        nilai_tugas=input.nextInt();

        System.out.print("Masukan Nilai UTS   : ");
        nilai_uts=input.nextInt();

        System.out.print("Masukan Nilai Uas   : ");
        nilai_uas=input.nextInt();
        
    }
    public double rata_rata(){
        return (0.1 * nilai_absen + 0.2 * nilai_tugas + 0.3 * nilai_uas + 0.4 * nilai_uts);
    }

}

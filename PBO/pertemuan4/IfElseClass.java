package pertemuan4;

import java.util.Scanner;

public class IfElseClass {
    public String nama,ket;
    public int nilAkhir;
    Scanner input= new Scanner(System.in);
    public String getKeterangan;

    public void setInputData() {
        System.out.print("Masukan nama Siwa : ");
        nama = input.nextLine();
        System.out.print("Masukan Nilai Akhir : ");
        nilAkhir = input.nextInt();
            if(nilAkhir> 70 ){
                //perintah jika kondisi true
                ket="Lulus";
            }
            //pertintah jika gagal
            else{
                ket="Gagal";
            }
        
    }

    public void getKeterangan() {
    }
}

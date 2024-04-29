package pertemuan3;

import java.util.Scanner;

public class LatScanner {
    public static void main(String[] args) {
        
    
    try (//membuat object baru
    Scanner input = new Scanner(System.in)) {
        String nama;
        int n2;
        double n1, n3;

        System.out.print("Masukan Nama Anda : ");
        nama=input.nextLine();
        
        System.out.print("Masukan Nilai 1 : ");
        n1=input.nextDouble();
        
        System.out.print("Masukan Nilai 2 : ");
        n2=input.nextInt();
        n3=n1+n2;
        
        System.out.print("\nNama Anda   : " + nama);
        
        //deklarasi variabel
        
        System.out.print("\nNilai anda : "+ n3);
    }
}
}
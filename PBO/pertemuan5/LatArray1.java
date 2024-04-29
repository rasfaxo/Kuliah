package pertemuan5;

import java.util.Scanner;

public class LatArray1 {
    public static void main(String[] args) {
        int i;
        int[] nil_akhir;
        // deklarasi variable array
        nil_akhir = new int[6]; //membuat objek array
        try (Scanner input = new Scanner(System.in)) {
            for (i=0; i<6; i++){
                System.out.println("masukan Array ke " + i +" = ");
                nil_akhir[i]=input.nextInt();
            }
        }
            System.out.println("\n\nData yang Di input ke Elemen Array \n");
            for (i=0; i<6; i++){
                System.out.println("Nilai akhir index"+ i);
                System.out.println(" = "+nil_akhir);
            }
    }
}

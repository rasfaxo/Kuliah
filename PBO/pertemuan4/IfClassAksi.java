package pertemuan4;

import java.util.Scanner;

public class IfClassAksi {
    public static void main(String[] args) {
        try (Scanner input = new Scanner(System.in)) {
            IfClass fungsiif=new IfClass();

            System.out.print("Total Pembelian Rp. ");
            fungsiif.total_beli=input.nextDouble();

            System.out.println("Besarnya Potongan Rp. "+fungsiif.GetPotongan());
            System.out.println("Jumlah yang harus dibayarkan Rp. "+fungsiif.jumlahbayar());
        }

    }
}

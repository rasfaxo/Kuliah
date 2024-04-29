package pertemuan4;

import java.util.Scanner;


public class Latif {
    public static void main(String[] args) {
        double total_beli,potongan=0, jumlah_bayar=0;
        try(Scanner input = new Scanner(System.in)){
        
        System.out.print("Total Pembelian Rp. ");
        total_beli=input.nextDouble();
        }
            if (total_beli>=50000)
            potongan= 0.2*total_beli;
        System.out.println("Besarnya Potongan Rp. "+potongan);
        jumlah_bayar=total_beli-potongan;
        System.out.println("Jumlah yang harus dibayarkan Rp "+jumlah_bayar);

    }
}

package pertemuan5;

import java.util.Scanner;

public class TugasArray {

    public static void main(String[] args) {
        
        // Inisialisasi variabel dan array
        try (Scanner input = new Scanner(System.in)) {
            int jumlah_data,total_bayar = 0;
            String[] kode_barang, nama_barang;
            int[] harga_barang, jumlah_barang, total_harga;
            
            // Input data barang
            System.out.println("\t\tPT.PERMATA ' PRATAMA ' ");
            System.out.println("+++++++++++++++++++++++++++++++++++++++++++");
            System.out.print("Masukan Nama petugas : ");
            String nama_petugas= input.next();
            System.out.print("Tanggal : ");
            String tanggal= input.next();
            System.out.print("Jumlah Data yang akan dimasukan : ");
            jumlah_data = input.nextInt();
            System.out.println("-------------------------------------------");
            
            total_harga = new int[jumlah_data];
            jumlah_barang = new int[jumlah_data];
            kode_barang = new String[jumlah_data];
            nama_barang = new String[jumlah_data];
            harga_barang = new int[jumlah_data];
            for (int i = 0; i < jumlah_data; i++) {
                System.out.println("\nData barang ke-" + (i+1));
                System.out.print("kode barang : ");
                kode_barang[i] = input.next();
                System.out.print("Jumlah      : ");
                jumlah_barang[i] = input.nextInt();
                System.out.println("-------------------------------------------");
                switch (kode_barang[i]) {
                    case "P001":
                        nama_barang[i] = "Printer";
                        harga_barang[i] = 700000;
                        break;
                    case "V001":
                        nama_barang[i] = "VGA Card";
                        harga_barang[i] = 75000;
                        break;
                    case "M001":
                        nama_barang[i] = "Motherboard";
                        harga_barang[i] = 950000;
                        break;
                    default:
                        System.out.println("Kode barang tidak valid.");
                        i--;
                    }
                    
                    total_harga[i] = harga_barang[i] * jumlah_barang[i];
                    total_bayar += total_harga[i];
            }
            
            // Tampilkan output
            System.out.println("\n\t\t\tPT. PERMATA PRATAMA");
            System.out.println("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++");
            System.out.println("Nama Petugas               : "+ nama_petugas +"\t\t\tTanggal : "+tanggal);
            System.out.println("Jumlah Data yang dimasukan : "+jumlah_data);
            System.out.println("-------------------------------------------------------------------------");
            System.out.println("No | Kode Barang | Nama Barang | Harga Barang | Jumlah Beli | Total Harga");
            System.out.println("---|-------------|-------------|--------------|-------------|------------");
            for (int i = 0; i < jumlah_data; i++) {
                System.out.printf("%2d | %-11s | %-11s | %,10d   | %,6d      | %,10d\n", (i+1), kode_barang[i], nama_barang[i], 
                harga_barang[i], jumlah_barang[i], total_harga[i]);
            }
            System.out.println("-------------------------------------------------------------------------");
            System.out.println("\nTotal pendapatan pada tanggal "+tanggal+" adalah sebesar Rp."+total_bayar);
        }
        
    }
}

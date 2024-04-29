package pertemuan5;

import java.util.Scanner;

public class LatihanSoalArray {

    public static void main(String[] args) {

        try (// Inisialisasi variabel dan array
        Scanner input = new Scanner(System.in)) {
            String[] kode_barang = {"P001", "V001", "M001"};
            String[] nama_barang = {"Printer", "VGA Card", "Motherboard"};
            int[] harga_barang = {700000, 75000, 950000};
            int[] jumlah_barang;
            int[] total_harga;
            int jumlah_data = 3, jumlah_beli = 0, diskon = 0, total_bayar = 0;

            // Input data pembelian
            System.out.print("Masuka Nama Petugas : ");
            String nama_pembeli = input.next();
            System.out.print("Tanggal :");
            String tanggal=input.next();
            System.out.println("Masukan Jumlah Barang yang Diinput : ");

            jumlah_barang = new int[jumlah_data];
            total_harga = new int[jumlah_data];
            for (int i = 0; i < jumlah_data; i++) {
                System.out.println("\nData pembelian barang ke-" + (i+1));
                System.out.println("Kode barang: " + kode_barang[i]);
                System.out.println("Nama barang: " + nama_barang[i]);
                System.out.println("Harga barang: " + harga_barang[i]);
                System.out.print("Masukkan jumlah barang yang dibeli: ");
                jumlah_barang[i] = input.nextInt();
                jumlah_beli += jumlah_barang[i];
                total_harga[i] = harga_barang[i] * jumlah_barang[i];
                total_bayar += total_harga[i];
            }

            // Hitung diskon
            if (jumlah_beli > 1000000) {
                diskon = (int) (total_bayar * 0.1);
            }

            // Tampilkan output
            System.out.println("\n=== PT. Permata Pratama ===");
            System.out.println("Nama pembeli: " + nama_pembeli);
            System.out.println("Tanggal : "+tanggal);
            System.out.println("No | Kode Barang | Nama Barang | Harga Barang | Jumlah Beli | Total Harga");
            System.out.println("---|------------|-------------|-------------|-------------|------------");
            for (int i = 0; i < jumlah_data; i++) {
                System.out.printf("%2d | %-11s | %-10s | %,11d | %,11d | %,12d\n", (i+1), kode_barang[i], nama_barang[i], harga_barang[i], jumlah_barang[i], total_harga[i]);
            }
            System.out.println("Diskon: " + String.format("%,d", diskon));
            System.out.println("Total Bayar: " + String.format("%,d", (total_bayar - diskon)));
        }
    }

}


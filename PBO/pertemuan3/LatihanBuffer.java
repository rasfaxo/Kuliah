package pertemuan3;

import java.io.*;

public class LatihanBuffer {
    public static void main(String[] args) throws Exception {

        //membuat objek baru
        InputStreamReader keyReader = new InputStreamReader(System.in);
        BufferedReader input = new BufferedReader(keyReader);
        //dekirasi variable
        String kata1, kata2;

        System.out.print("Masukan kata pertama : ");
        kata1 = input.readLine();

        System.out.print("Masukan kata kedua : ");
        kata2 = input.readLine();

        System.out.println("\n Hasil input String "+kata1+" "+kata2);
    }
}

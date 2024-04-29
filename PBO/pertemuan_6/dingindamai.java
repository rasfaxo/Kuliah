package pertemuan_6;

import java.util.Scanner;

public class dingindamai {
    public static void main(String[] args) {
        
       try(Scanner input = new Scanner(System.in)){
        int jam_kerja,lembur,gaji_bersih;
        int gaji_tetap = 300000;
        int tunjangan,persen;
        

        
        
        
        //layar masukan
    
        System.out.println("\t\tPT.DINGIN DAMAI ' ");
        System.out.println("-------------------------------------------");
        System.out.print("Nama Karyawan : ");
        String nama_karyawan= input.next();
        System.out.print("Golongan : ");
        String golongan=input.next();
        System.out.print("pendidikan (SMU/D3/S1): ");
        String pendidikan = input.next();
        System.out.print("Jumlah jam kerja : ");
        jam_kerja=input.nextInt();
        System.out.println("-------------------------------------------");

        switch (golongan){
            case "1" :
                persen = gaji_tetap * 5/100;
                break;
            
            case "2" :
                persen = gaji_tetap * 10/100;
                break;

            case "3" :
                persen = gaji_tetap * 15/100;
                break;
            default:
            System.out.println("kode golongan tidak valid");
            return;
        }
        switch (pendidikan){
            case "SMU" :
                tunjangan= (int) (gaji_tetap * 2.5/100);
                break;
            case "D3" :
                tunjangan = gaji_tetap * 5/100;
                break;
            case "S1" :
                tunjangan = (int) (gaji_tetap * 7.5/100);
                break;
            default:
            System.out.println("kode penidikan salah");
            return;
        }

        if (jam_kerja >= 8){
            lembur = (jam_kerja - 8) * 2500;
        
            
        }
        else{
        lembur=0;
        }
        //menghitung gaji bersih
        gaji_bersih = tunjangan + persen + lembur + gaji_tetap;

        //layar keluaran
        System.out.println("karyawan yang bernama : "+nama_karyawan);
        System.out.println("Honor tetap           : Rp."+gaji_tetap);
        System.out.println("tunjangan jabatan     : Rp." + persen );
        System.out.println("Tunjangan pendidikan  : Rp."+ tunjangan);
        System.out.println("honor lembur          : Rp."+lembur);
        System.out.println("-------------------------------------------");
        System.out.println("Honor yang diterima : "+gaji_bersih);
        }
    }
    }
    

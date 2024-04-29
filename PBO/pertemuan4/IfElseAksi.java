package pertemuan4;

public class IfElseAksi {
    public static void main(String[] args) {
        IfElseClass ifclass=new IfElseClass();
        
        ifclass.setInputData();
        ifclass.getKeterangan();

        System.out.println("Hasil Akhir");
        System.out.println("====================================");
        System.out.println("Nama Siswa                  :"+ifclass.nama);
        System.out.println("Nilai Akhir Yang Didapat    :"+ifclass.nilAkhir);
        System.out.println("Keterangan                 :"+ifclass.getKeterangan);
        System.out.println("====================================");
    }
    
}

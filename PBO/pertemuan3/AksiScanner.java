package pertemuan3;

public class AksiScanner {
    public static void main(String[] args) 
    {
    //membuat object baru
    ClassScanner scan=new ClassScanner();
    
    scan.inputScanner();
    System.out.println("Nama Anda   :" + scan.getnama());
    System.out.println("Nilai Anda : " + scan.rata());
    }
    
}

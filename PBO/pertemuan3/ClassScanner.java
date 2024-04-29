package pertemuan3;
import java.util.Scanner;

public class ClassScanner {
    
    public String nama;
    public double n1;
    public int n2;
    
    Scanner input = new Scanner(System.in);

    public String getnama(){
        return nama;
    }
    public void inputScanner(){
        System.out.println("masukan nama anda");
        nama = input.nextLine();
        System.out.println("masukan nilai 1 ");
        n1 = input.nextDouble();
        System.out.println("masukan nilai 2 ");
        n2 = input.nextInt();
    }
    public double rata (){
        return((n1+n2)/2);
    }
}

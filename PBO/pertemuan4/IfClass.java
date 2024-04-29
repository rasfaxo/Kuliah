package pertemuan4;

public class IfClass {
    public double total_beli,potongan;

    public void setTotalBeli(double a){
        total_beli=a;
    }
    public double GetPotongan(){
        if (total_beli >=50000){
            potongan=0.2*total_beli;
        }
        return potongan;
    }
    public double jumlahbayar(){
        return (total_beli-potongan);
    }
}

package polymorphism;


    class hewan{
        public void suara() {
            System.out.println("Hewan bersuara : ");
        }
    }
    class kuda extends hewan {
        public void suara(){
            System.out.println("kuda mengikik");
        }
    }
    class kucing extends hewan {
        public void suara() {
            System.out.println("kucing mengeong");
        }
    }
    class ayam extends hewan {
        public void suara(){
            System.out.println("ayam berkokok");
        }
    }
    public class polimorfisme {
        public static void main(String[] args) {
        
            hewan HEWAN = new hewan();
            kuda KUDA = new kuda();
            kucing KUCING = new kucing();
            ayam AYAM = new ayam();

            HEWAN.suara();

            HEWAN=KUDA;
            HEWAN.suara();

            HEWAN=KUCING;
            HEWAN.suara();

            HEWAN=KUCING;
            HEWAN.suara();

            HEWAN=AYAM;
            HEWAN.suara();
        }
    }


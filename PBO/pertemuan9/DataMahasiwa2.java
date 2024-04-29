package pertemuan9;

import javax.swing.*;

public class DataMahasiwa2 extends JFrame {
    JPanel jp= new JPanel();
    JTextField jt1 = new JTextField();
    JTextField jt2 = new JTextField();
    JTextField jt3 = new JTextField();
    JLabel jl1 = new JLabel("NIM");
    JLabel jl2 = new JLabel("NAMA");
    JLabel jl3 = new JLabel("JURUSAN");

    public DataMahasiwa2() {
        add(jl1);
        add(jl2);
        add(jl3);
        add(jt1);
        add(jt2);
        add(jt3);
        add(jp);
        jl1.setBounds(15, 20, 80, 25);
        jl2.setBounds(15, 50, 80, 25);
        jl3.setBounds(15, 80, 80, 25);
        jt1.setBounds(100, 20, 100, 25);
        jt2.setBounds(100, 50, 100, 25);
        jt3.setBounds(100, 80, 100, 25);
}
}

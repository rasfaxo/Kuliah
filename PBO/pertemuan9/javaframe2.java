package pertemuan9;

import javax.swing.*;

public class javaframe2 extends JFrame {
    JPanel jp= new JPanel();
    JTextField jt = new JTextField();
    JLabel jl = new JLabel("label 1");

    public javaframe2() {
        add(jl);
        add(jt);
        add(jp);
        jl.setBounds(15, 20, 80, 25);
        jt.setBounds(100, 20, 100, 25);
    }
}

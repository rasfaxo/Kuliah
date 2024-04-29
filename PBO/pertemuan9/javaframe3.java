package pertemuan9;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class javaframe3 extends JFrame {
    JPanel pl = new JPanel();
    JLabel lb1 = new JLabel("String 1");
    JLabel lb2 = new JLabel("string 2");
    JLabel lb3 = new JLabel("hasil");

    JTextField tf1 = new JTextField();
    JTextField tf2 = new JTextField();
    JTextField tf3 = new JTextField();

    JButton bn1 = new JButton("Proses");
    JButton bn2 = new JButton("Hapus");
    
    public javaframe3() {
        add(pl);
        add(lb1);
        add(lb2);
        add(lb3);
        add(tf1);
        add(tf2);
        add(tf3);
        add(bn1);
        add(bn2);
    }
}

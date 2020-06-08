/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package heranca;
import javax.swing.JOptionPane;

/**
 *
 * @author diego
 */
public class Principal {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Funcionario func = new Funcionario();
        func.setNome(JOptionPane.showInputDialog("Digite seu nome:"));
        func.setRg(JOptionPane.showInputDialog("Digite seu RG:"));
        func.setDepartamento(JOptionPane.showInputDialog("Digite seu Departarmento"));
        func.setSalario  (Double.parseDouble(JOptionPane.showInputDialog("Digite seu Salario:")));
        func.setCarteira_de_trabalho(JOptionPane.showInputDialog("Digite o número da carteira de trabalho:"));
    }
    
}

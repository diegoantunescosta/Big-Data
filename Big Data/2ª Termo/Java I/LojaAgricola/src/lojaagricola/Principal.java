/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package lojaagricola;
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
        LojaAgricola loja = new LojaAgricola();
        loja.setNome(JOptionPane.showInputDialog("Digite seu nome: "));
        loja.setEndereco(JOptionPane.showInputDialog("Digite seu endereço: "));
        loja.setCpf(JOptionPane.showInputDialog("Digite seu CPF: "));
        loja.setCnpj(JOptionPane.showInputDialog("Digite seu CNPJ : "));
        
        System.out.println("Nome: "+ loja.getNome());
        System.out.println("Endereço: "+ loja.getEndereco());
        System.out.println("CPF: " + loja.getCpf());
        System.out.println("CNPJ" + loja.getCnpj());   
        
      
    }
    
}

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package agro;
import java.util.Scanner;
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
        CadernoDeEnderecosAgricultor cd = new CadernoDeEnderecosAgricultor ("Diego", "14996653327", "diegoantunescosta@gmail.com","05.02.1994","Rua Equador - Pompéia/SP");
        CadernoDeEnderecosAgricultor cd1 = new CadernoDeEnderecosAgricultor () ;
        Scanner dados = new Scanner (System.in); 
        cd1.setNome(JOptionPane.showInputDialog("Digite seu nome :"));
        System.out.println("Digite seu telefone: ");
        cd1.setTelefone(dados.next());
        cd.setEmail(JOptionPane.showInputDialog("Digite seu email: "));
        //cd.setTelefone(Integer.parseInt(JOptionPane.showInputDialog("Digite seu telefone")); Para utilizar Int tem que alterar nos métodos
        cd.setTelefone(JOptionPane.showInputDialog("Digite seu telefone"));        
        
        
    
            System.out.println("nome e telefone: "+ cd1.getNomeTel());
            System.out.println("Nome: "+ cd.getNome());
            System.out.println("Telefone: " + cd.getTelefone());
            System.out.println("Email: " + cd.getEmail());
            System.out.println("Nascimento: "+ cd.getNiver());
            System.out.println("Endereço: " + cd.getEndereco());
            
        JOptionPane.showMessageDialog(null , cd.getNome()+"\n "+cd.getTelefone ()+"\n "+cd.getEmail ()+"\n"+cd.getEndereco());
            
    }
        
    }
    


/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package agro;

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
            System.out.println("Nome: "+ cd.getNome());
            System.out.println("Telefone: " + cd.getTelefone());
            System.out.println("Email: " + cd.getEmail());
            System.out.println("Nascimento: "+ cd.getNiver());
            System.out.println("Endereço: " + cd.getEndereco());
            
    }
        
    }
    


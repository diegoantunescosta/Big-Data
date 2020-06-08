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
public class CadernoDeEnderecosAgricultor {
    
    private String nome;
    private String telefone;
    private String email;
    private String niver;
    private String endereco;
    
    public CadernoDeEnderecosAgricultor(String nome, String telefone, String email,String niver, String endereco) {
    
   this.nome = nome;
   this.telefone = telefone;
   this.email = email;
   this.niver = niver;
   this.endereco = endereco;
   
}

    CadernoDeEnderecosAgricultor() {
        
    }
 
    public String getNome(){
        return nome;
    }
    
    public void setNome (String nome) {
        this.nome = nome;
    }
    
    public String getTelefone(){
        return telefone;
    }
    
    public void setTelefone (String telefone) {
        this.telefone = telefone;
    }
     
    public String getEmail(){
        return email;
    }
    
    public void setEmail (String email) {
        this.email = email;
    }
    
    public String getNiver(){
        return niver;
    }
    
    public void setNiver (String niver) {
        this.niver = niver;
    }
    
    public String getEndereco(){
        return endereco;
    }
    
    public void setEndereco (String endereco) {
        this.endereco = endereco;
    }
    
    public String getNomeTel(){
        return getNome()+getTelefone();
    }
} 


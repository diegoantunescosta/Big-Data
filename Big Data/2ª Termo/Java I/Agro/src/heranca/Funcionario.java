/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package heranca;

/**
 *
 * @author diego
 */
public class Funcionario {

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getDepartamento() {
        return departamento;
    }

    public void setDepartamento(String departamento) {
        this.departamento = departamento;
    }

    public double getSalario() {
        return salario;
    }

    public void setSalario(double salario) {
        this.salario = salario;
    }

    public String getRg() {
        return rg;
    }

    public void setRg(String rg) {
        this.rg = rg;
    }

    public String getCpf() {
        return cpf;
    }

    public void setCpf(String cpf) {
        this.cpf = cpf;
    }

    public String getCarteira_de_trabalho() {
        return carteira_de_trabalho;
    }

    public void setCarteira_de_trabalho(String carteira_de_trabalho) {
        this.carteira_de_trabalho = carteira_de_trabalho;
    }
    protected String nome;
    protected String departamento;
    protected double salario;
    protected String rg;
    protected String cpf;
    protected String carteira_de_trabalho;
    
}

import java.util.Scanner;

public class Principal {

	public static void main(String[] args) {
		String endereco = "Rua Equador";
		java.util.Scanner entrada = new Scanner (System.in);
		
		System.out.println("Informe o endereco da pessoa: ");
		endereco = entrada.next();
		
		Pessoa minhaPessoa = new Pessoa (endereco);
		
		System.out.println("O endereco digitado foi : "+minhaPessoa.getEndereco());
		
		
		//estanciando empregado
		
		Empregado meuEmpregado = new Empregado ();
		

	}

}

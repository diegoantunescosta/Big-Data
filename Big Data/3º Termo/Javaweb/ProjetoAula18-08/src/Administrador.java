
public class Administrador extends Empregado {

	private double ajudaCusto;
	
	public Administrador () {
		super();
	}
	
	
	public double getAjudacusto() {
		return ajudaCusto;
	}

	public void setAjudacusto(double ajudacusto) {
		this.ajudaCusto = ajudacusto;
	}
	public double calcularSalario() {
		double salarioLiquido;
		salarioLiquido = super.calcularSalario() + getAjudaCusto ();
		return salarioLiquido;
	}
		
}

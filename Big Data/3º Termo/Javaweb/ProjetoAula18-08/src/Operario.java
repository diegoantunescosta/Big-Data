
public class Operario extends Empregado{
	

	private double valorProducao;
	private double Comissao;
	
	public double getValorProducao() {
		return valorProducao;
	}
	public void setValorProducao(double valorProducao) {
		this.valorProducao = valorProducao;
	}
	public double getComissao() {
		return Comissao;
	}
	public void setComissao(double comissao) {
		Comissao = comissao;
	}
	
	public double calcularSalario () {
		double salarioLiquido = super.calcularSalario() + getComissao(); 
		return salarioLiquido;
	}

}

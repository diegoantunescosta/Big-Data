
public class ImovelVelho extends Imobiliaria {
	
	public double desconto;

	public double getDesconto() {
		return desconto;
	}

	public void setDesconto(double desconto) {
		this.desconto = desconto;
	}
	
	public double getPreco () {
		double precoVelho;
		precoVelho = super.getPreco() - getDesconto();
		return precoVelho;
	}
}


public class Imobiliaria {
	
	private double Imovel;
	private double Adicional;
	public double getImovel() {
		return Imovel;
	}
	public void setImovel(double imovel) {
		Imovel = imovel;
	}
	public double getAdicional() {
		return Adicional;
	}
	public void setAdicional(double adicional) {
		Adicional = adicional;
	}
	
	public double getPreco() {
		return super.getPreco() + getAdicional ();
		
	}
}

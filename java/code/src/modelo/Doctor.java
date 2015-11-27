package modelo;

public class Doctor extends Person{
	private Integer crm;
	private String especialidade;
	
	public Integer getCrm() {
		return crm;
	}

	public void setCrm(Integer crm) {
		this.crm = crm;
	}


	public String getEspecialidade() {
		return especialidade;
	}


	public void setEspecialidade(String especialidade) {
		this.especialidade = especialidade;
	}

	public void givePrescription(String patient){
		
	}
		
		
	public void giveAdvice(String patient){
		
	}	
		
	public void recommendsSurgery(String patient, String surgery){
			
			
	}
		
		
	public void recommendsTreatment(String patient, String treatment){
			
			
	}

}

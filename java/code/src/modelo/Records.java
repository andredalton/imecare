package modelo;

public class Records {

	private String type = "";
	private String namePatient = "";
	private String cpf = "";
	private String cid = "";
	private String diseaseName = "";
	private String symptonName = "";
	private String symptonDescription = "";
	private String medicineName = "";
	private String medicalStripe = "";
	private int anvisaCode = -1;
	private String examName = "";
	private String examDescription = "";


    public String getType(){
		return type;
	}

	public void setType(String type){
		this.type = type;
	}	


    public String getNamePatient(){
		return namePatient;
	}

	public void setNamePatient(String namePatient){
		this.namePatient = namePatient;
	}


    public String getCpf(){
		return cpf;
	}

	public void setCpf(String cpf){
		this.cpf = cpf;
	}

    public String getCid(){
		return cid;
	}

	public void setCid(String cid) {
		this.cid = cid;
	}

    public String getDiseaseName(){
		return diseaseName;
	}

    public void setDiseaseName(String diseaseName) {
		this.diseaseName = diseaseName;
	}

	
    public String getSymptonName(){
		return symptonName;
	}

	public void setSymptonName(String symptonName){
		this.symptonName = symptonName;
	}


    public String getSymptonDescription(){
		return symptonDescription;
	}

	public void setSymptonDescription(String symptonDescription){
		this.symptonDescription = symptonDescription;
	}

    public String getMedicineName(){
		return medicineName;
	}

	public void setMedicineName(String medicineName){
		this.medicineName = medicineName;
	}

    public String getMedicalStripe(){
		return medicalStripe;
	}

	public void setMedicalStripe(String medicalStripe){
		this.medicalStripe = medicalStripe;
	}


    public int getAnvisaCode(){
		return anvisaCode;
	}

	public void setAnvisaCode(int anvisaCode){
		this.anvisaCode = anvisaCode;
	}


	public String getExamName(){
		return examName;
	}

	public void setExamName(String examName){
		this.examName = examName;
	}

	public String getExamDescription(){
		return examDescription;
	}

	public void setExamDescription(String examDescription){
		this.examDescription = examDescription;
	}


	public String toString(){
         
		return 
		"Tipo_sanguíneo: " + getType() + "\nNome paciente: " + getNamePatient() + "\nCPF: " + getCpf() 
		+ "\nCid: " +  getCid() + "\nDoença: " +  getDiseaseName() + "\nSintoma: " +  getSymptonName() + "\nDescrição do sintoma: " + 
		getSymptonDescription() + "\nNome do medicamento: " + getMedicineName() + "\nTarja: " +  getMedicalStripe() + 
		"\nCódigo anvisa: " +  getAnvisaCode() + "\nNome do exame: " +  getExamName() + "\nDescrição do exame: " +  getExamDescription();
	}
}

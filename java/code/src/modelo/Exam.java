package modelo;

public class Exam {

	private int anvisaCode = -1;
	private String name = " ";
	private String description = " ";

	public int getAnvisaCode(){
		return anvisaCode;
	}

	public void setAnvisaCode(int code){
		this.anvisaCode = code;
	}

	public String getName(){
		return name;
	}

	public void setName(String name){
		this.name = name;
	}

	public String getDescription(){
		return description;
	}

	public void setDescription(String description){
		this.description = description;
	}

}

package modelo;

import java.util.Calendar;

public class Person {

	private String name = " ";
	private String address = " ";
	private String email = " ";
	private Calendar birthDate;
	private String cpf = " ";
	private String rg = " ";
	private int phone[] = new int[15];
	
	public String getName() {
		return name;
	}
	
	public void setName(String name) {
		this.name = name;
	}
	
	public String getEmail() {
		return email;
	}
	
	public void setEmail(String email) {
		this.email = email;
	}

	public Calendar getBirthDate() {
		return birthDate;
	}
	
	public void setBirthDate(Calendar birthDate) {
		this.birthDate = birthDate;
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

	public String getAddress() {
		return address;
	}

	public void setAddress(String address) {
		this.address = address;
	}

	public int[] getPhone() {
		return phone;
	}

	public void setPhone(int[] phone) {
		this.phone = phone;
	}
	
}

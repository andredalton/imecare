package modelo;

import java.util.Calendar;

public class DiagnosedDisease {

	private String cid = " ";
	private String doctorCpf = " ";
	private String patientCpf = " ";
	private Calendar date;
	private Calendar time;

	public String getCid(){
		return cid;
	}

	public void setCid(String cid){
		this.cid = cid;
	}

	public String getDoctorCpf(){
		return doctorCpf;
	}

	public void setDoctorCpf(String doctorCpf){
		this.doctorCpf = doctorCpf;
	}
	
	public String getPatientCpf(){
		return patientCpf;
	}

	public void setPatientCpf(String patientCpf){
		this.patientCpf = patientCpf;
	}

	public Calendar getDate(){
		return date;
	}

	public void setDate(Calendar date){
		this.date = date;
	}

	public Calendar getTime(){
		return time;
	}

	public void setTime(Calendar time){
		this.time = time;
	}

}

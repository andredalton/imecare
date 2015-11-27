package modelo;
import java.util.*;

public class Prescreve {

	private String medicineName = "";
	private String doctorCpf = "";
	private int crm = -1;
	private String patientCpf = "";
	private String doctorName = "";
	private String patientName = "";
	private Calendar date;
	private Calendar time;
	private String dose = "";
	private Calendar period;
	private String frequency = "";
	
	
	public String getMedicineName() {
		return medicineName;
	}
	
	public void setMedicineName(String medicineName) {
		this.medicineName = medicineName;
	}
	
	public String getDoctorCpf() {
		return doctorCpf;
	}
	
	public void setDoctorCpf(String doctorCpf) {
		this.doctorCpf = doctorCpf;
	}
	
	public int getCRM() {
		return crm;
	}
	
	public void setCRM(int crm) {
		this.crm =crm;
	}
	
	public String getPatientCpf() {
		return patientCpf;
	}
	
	public void setPatientCpf(String patientCpf) {
		this.patientCpf = patientCpf;
	}
	
	public String getDoctorName() {
		return doctorName;
	}
	
	public void setDoctorName(String DoctorName) {
		this.doctorName = DoctorName;
	}
	
	public String getPatientName() {
		return patientName;
	}
	
	public void setPatientName(String patientName) {
		this.patientName = patientName;
	}
	
	public Calendar getDate() {
		return date;
	}
	
	public void setDate(Calendar date) {
		this.date = date;
	}
	
	public Calendar getTime() {
		return time;
	}
	
	public void setTime(Calendar time) {
		this.time = time;
	}
	
	public String getDose() {
		return dose;
	}
	
	public void setDose(String dose) {
		this.dose = dose;
	}
	
	public Calendar getPeriod() {
		return period;
	}
	
	public void setPeriod(Calendar period) {
		this.period = period;
	}
	
	public String getFrequency() {
		return frequency;
	}
	
	
	public void setFrequency(String frequency) {
		this.frequency = frequency;
	}
	
}









package modelo;
import java.util.Calendar;

public class Schedule {

	private String doctorCpf;
	private String patientCpf;
	private Calendar dateTime;
	private String type;
	private String comment;
	
	public String getDoctorCpf() {
		return doctorCpf;
	}

	public void setDoctorCpf(String cpf) {
		this.doctorCpf = cpf;
	}

	public String getPatientCpf() {
		return patientCpf;
	}

	public void setPatientCpf(String cpf) {
		this.patientCpf = cpf;
	}

	public Calendar getDateTime() {
		return dateTime;
	}

	public void setDateTime(Calendar date) {
		this.dateTime = date;
	}

	public String getType() {
		return type;
	}

	public void setType(String type) {
		this.type = type;
	}

	public String getComment() {
		return comment;
	}

	public void setComment(String comment) {
		this.comment = comment;
	}

}
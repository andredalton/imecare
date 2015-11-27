package bd;

import java.sql.*;

import modelo.Patient;
import modelo.Person;
import bd.PersonDao;

public class PatientDao {

	private Connection conexao;
	 
	public PatientDao() {
		this.conexao = ConnectionFactory.obterInstancia().obterConexao();
	}

	public void addPatient(Patient patient){
		String sql = "insert into paciente "
				+ "(cpf, tipo_sanguineo)" + " values (?,?)";

		PersonDao personDao = new PersonDao();
		personDao.addUser(patient);	

		try {
			// prepared statement para inserção
			PreparedStatement stmt = conexao.prepareStatement(sql);
			stmt.setString(1, patient.getCpf());	
			stmt.setString(2, patient.getBloodType());			
			// executa
			stmt.execute();
			stmt.close();
		} catch (SQLException e) {
			throw new RuntimeException(e);
		}	
		
	}	
	
	public void updatePatient(Patient patient){

		PersonDao person = new PersonDao();
		
		person.updateUser(patient);

		String sql = "update paciente set tipo_sanguineo=? where cpf=?";
		try {
			PreparedStatement stmt = conexao.prepareStatement(sql);
			stmt.setString(1, patient.getBloodType());
			stmt.setString(2, patient.getCpf());
			stmt.execute();
			stmt.close();
		} catch (SQLException e) {
			throw new RuntimeException(e);
		}
	}
	
	public void removePatient(Patient patient) {

        PersonDao person = new PersonDao();
			
		try {
			PreparedStatement stmt = conexao.prepareStatement("delete "
					+ "from paciente where cpf=?");
			stmt.setString(1, patient.getCpf());
			stmt.execute();
			stmt.close();
		} catch (SQLException e) {
			throw new RuntimeException(e);
		}

		person.removeUser(patient);
	}

	public Patient getPatient(String cpf){

		try {
			PersonDao personDao = new PersonDao();
			Person person = personDao.getUser(cpf);
			Patient patient = null;
			
			PreparedStatement stmt = conexao.prepareStatement("select * "
					+ "from paciente where cpf=?");
			stmt.setString(1, cpf);
			ResultSet rs = stmt.executeQuery();

			if (rs.next()) {
				patient = new Patient();

				patient.setBloodType(rs.getString("tipo_sanguineo"));
				patient.setName(person.getName());
				patient.setRg(person.getRg());
				patient.setCpf(person.getCpf());
				patient.setBirthDate(person.getBirthDate());
				patient.setAddress(person.getAddress());
				patient.setEmail(person.getEmail());
			}
			rs.close();
			stmt.close();
			return patient;

		} catch (SQLException e) {
			throw new RuntimeException(e);
		}
	}
	
}

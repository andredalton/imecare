package bd;

import java.sql.*;
//import java.util.*;

import modelo.Prescreve;

public class PrescreveDao {
	
	private Connection conexao;
	 
	public PrescreveDao() {
		this.conexao = ConnectionFactory.obterInstancia().obterConexao();
	}

	
	
	public void addPrescreve(Prescreve prescreve){
		String sql = "insert into prescreve "
				+ "(nome_medicamento, CPF_Medico, CPF_Paciente, " +
				"data, horario, dose, periodo, frequencia)" + 
				" values (?,?,?,?,?,?,?,?)";
		
		try {
			// prepared statement para inserção
			PreparedStatement stmt = conexao.prepareStatement(sql);
	
			// seta os valores

			stmt.setString(1, prescreve.getMedicineName());
			stmt.setString(2, prescreve.getDoctorCpf());  
			stmt.setString(3, prescreve.getPatientCpf());
			stmt.setDate(4, new Date(prescreve.getDate().getTimeInMillis()));
			stmt.setTime(5, new Time(prescreve.getTime().getTimeInMillis()));
			stmt.setString(6, prescreve.getDose());
			stmt.setTime(7, new Time(prescreve.getPeriod().getTimeInMillis()));
			stmt.setString(8, prescreve.getFrequency());				
				
			// executa
			stmt.execute();
			stmt.close();
		} catch (SQLException e) {
			throw new RuntimeException(e);
		}		
	}
			
	public void removePrescreve (Prescreve prescreve) {
		try {
	
			
			PreparedStatement stmt = conexao.prepareStatement("delete "
					+ "from prescreve where cpf_Medico=? AND CPF_Paciente=? " +
					"AND Data=? AND Horario=? AND nome_medicamento=?");
			
			
			stmt.setString(1, prescreve.getDoctorCpf()); 
			stmt.setString(2, prescreve.getPatientCpf());
			stmt.setDate(3, new Date(prescreve.getDate().getTimeInMillis()));
			stmt.setTime(4, new Time(prescreve.getTime().getTimeInMillis()));
			stmt.setString(5, prescreve.getMedicineName());
					
			
			stmt.execute();
			stmt.close();
		} catch (SQLException e) {
			throw new RuntimeException(e);
		}


	}	
	
}
package bd;

import java.sql.*;

import modelo.Schedule;

public class ScheduleDao {

	private Connection conexao;
		 
	public ScheduleDao() {
	     this.conexao = ConnectionFactory.obterInstancia().obterConexao();
	}

	public void addSchedule(Schedule schedule){

			String sql = "insert into atendimento "
					+ "(CPF_Medico, CPF_Paciente, data, horario, tipo_atendimento, comentario)"
					+ " values (?,?,?,?,?,?)";
			
			try {
				PreparedStatement stmt = conexao.prepareStatement(sql);

				stmt.setString(1, schedule.getDoctorCpf());
				stmt.setString(2, schedule.getPatientCpf());
				stmt.setDate(3, new Date(schedule.getDateTime().getTimeInMillis()));
				stmt.setTime(4, new Time(schedule.getDateTime().getTimeInMillis()));
				stmt.setString(5, schedule.getType());
				stmt.setString(6, schedule.getComment());

				// executa
				stmt.execute();
				stmt.close();
			} catch (SQLException e) {
				// A SQLException é "encapsulada" em uma RuntimeException
				// para desacoplar o código da API de JDBC
				throw new RuntimeException(e);
			}	
				
		}

	public void updateSchedule(Schedule schedule){


		String sql = "update atendimento set tipo_atendimento=? comentario=?"
					+ "CPF_Paciente=? and CPF_Medico=? and data=? and hora=?";
		
		try {
			PreparedStatement stmt = conexao.prepareStatement(sql);

			stmt.setString(1, schedule.getType());
			stmt.setString(2, schedule.getComment());
			stmt.setString(3, schedule.getDoctorCpf());
			stmt.setString(4, schedule.getPatientCpf());
			stmt.setDate(5, new Date(schedule.getDateTime().getTimeInMillis()));
			stmt.setTime(6, new Time(schedule.getDateTime().getTimeInMillis()));

			// executa
			stmt.execute();
			stmt.close();
		} catch (SQLException e) {
			// A SQLException é "encapsulada" em uma RuntimeException
			// para desacoplar o código da API de JDBC
			throw new RuntimeException(e);
		}	
			
	}

	public void removeSchedule(Schedule schedule){

		try {
			PreparedStatement stmt = conexao.prepareStatement("delete "
					+ "from atendimento where CPF_Paciente=? and CPF_Medico=? and data=? and hora=?");
			stmt.setString(1, schedule.getPatientCpf());
			stmt.setString(2, schedule.getDoctorCpf());
			stmt.setDate(3, new Date(schedule.getDateTime().getTimeInMillis()));
			stmt.setTime(4, new Time(schedule.getDateTime().getTimeInMillis()));
			stmt.execute();
			stmt.close();
		} catch (SQLException e) {
			throw new RuntimeException(e);
		}

	}
}

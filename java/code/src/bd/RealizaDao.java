package bd;

import java.sql.*;

import modelo.Realiza;

public class RealizaDao {

	private Connection conexao;
		 
	public RealizaDao() {
			this.conexao = ConnectionFactory.obterInstancia().obterConexao();
	}

	public void addRealiza(Realiza realiza){
		String sql = "insert into realiza "
				+ "(codigo_anvisa,cpf_paciente)" + " values (?,?)";
		
		try {
			PreparedStatement stmt = conexao.prepareStatement(sql);

			stmt.setInt(1, realiza.getAnvisaCode());
			stmt.setString(2, realiza.getPatientCpf());

			stmt.execute();
			stmt.close();
		} catch (SQLException e) {
			throw new RuntimeException(e);
		}	
	}

	public void removeRealiza(Realiza realiza){

		try {
			PreparedStatement stmt = conexao.prepareStatement("delete "
					+ "from realiza where cpf_paciente=? and codigo_anvisa=?");
			stmt.setString(1, realiza.getPatientCpf());
			stmt.setInt(2, realiza.getAnvisaCode());
			stmt.execute();
			stmt.close();
		} catch (SQLException e) {
			throw new RuntimeException(e);
		}
	}
}
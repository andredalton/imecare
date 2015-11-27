package bd;

import java.sql.*;

import modelo.Doenca;

public class DoencaDao {

	private Connection conexao;
		 
	public DoencaDao() {
	     this.conexao = ConnectionFactory.obterInstancia().obterConexao();
	}

	public void addDoenca(Doenca doenca){
		String sql = "insert into doenca "
				+ "(CID, nome)" + " values (?,?)";
		
		try {
			// prepared statement para inserção
			PreparedStatement stmt = conexao.prepareStatement(sql);
			stmt.setString(1, doenca.getCid());	
			stmt.setString(2, doenca.getName());			
			// executa
			stmt.execute();
			stmt.close();
		} catch (SQLException e) {
			throw new RuntimeException(e);
		}	
	}
	

	public void removeDoenca(Doenca doenca) {

		try {
			PreparedStatement stmt = conexao.prepareStatement("delete "
					+ "from medicamento where cid=?");
			stmt.setString(1, doenca.getCid());
			stmt.execute();
			stmt.close();
		} catch (SQLException e) {
			throw new RuntimeException(e);
		}
	}
	
}

package bd;

import java.sql.*;
import java.util.*;

import modelo.Possui;

public class PossuiDao {
	
	private Connection conexao;
	 
	public PossuiDao() {
		this.conexao = ConnectionFactory.obterInstancia().obterConexao();
	}

	public void addPossui(Possui possui){
		String sql = "insert into possui "
				+ "(cid, nome_sintoma)" + " values (?,?)";
		
		try {
			// prepared statement para inserção
			PreparedStatement stmt = conexao.prepareStatement(sql);
	
			// seta os valores
				stmt.setString(1, possui.getCid());
			stmt.setString(2, possui.getSymptonName());
			
			// executa
			stmt.execute();
			stmt.close();
		} catch (SQLException e) {
			throw new RuntimeException(e);
		}		
	}
	
					
	public void removePossui(Possui possui) {
		try {
			PreparedStatement stmt = conexao.prepareStatement("delete "
					+ "from pessoa where cid=? AND nome_sintoma=?");
			stmt.setString(1, possui.getCid());
			stmt.setString(1, possui.getSymptonName());
			stmt.execute();
			stmt.close();
		} catch (SQLException e) {
			throw new RuntimeException(e);
		}

		// removeEmail(person);
	}
	
	
}
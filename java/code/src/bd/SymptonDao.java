package bd;

import java.sql.*;

import modelo.Sympton;

public class SymptonDao {

	private Connection conexao;
	 
	public SymptonDao() {
	     this.conexao = ConnectionFactory.obterInstancia().obterConexao();
	}

	public void addSympton(Sympton sympton){
		String sql = "insert into sintoma "
				+ "(nome, descricao)" + " values (?,?)";
		
		try {
			// prepared statement para inserção
			PreparedStatement stmt = conexao.prepareStatement(sql);

			// seta os valores

			stmt.setString(1, sympton.getName());
			stmt.setString(2, sympton.getDescription());
			// executa
			stmt.execute();
			stmt.close();
		} catch (SQLException e) {
			// A SQLException é "encapsulada" em uma RuntimeException
			// para desacoplar o código da API de JDBC
			throw new RuntimeException(e);
		}	
		
	}

	public void updateSympton(Sympton sympton){

		String sql = "update sympton set nome=?, descricao=?"
				+ " where nome=?";
		try {
			PreparedStatement stmt = conexao.prepareStatement(sql);
			stmt.setString(1, sympton.getName());
			stmt.setString(2, sympton.getDescription());
			stmt.execute();
			stmt.close();
		} catch (SQLException e) {
			throw new RuntimeException(e);
		}
	}

	public Sympton getSympton(String name){

		try {
			Sympton sympton = null;
			
			PreparedStatement stmt = conexao.prepareStatement("select * "
					+ "from sintoma where nome=?");
			stmt.setString(1, name);
			ResultSet rs = stmt.executeQuery();

			if (rs.next()) {
				sympton = new Sympton();

				sympton.setName(rs.getString("nome"));
				sympton.setDescription(rs.getString("descricao"));
				

			}
			rs.close();
			stmt.close();
			return sympton;

		} catch (SQLException e) {
			throw new RuntimeException(e);
		}
	}

	public void removeSympton(Sympton sympton) {
		try {
			PreparedStatement stmt = conexao.prepareStatement("delete "
					+ "from sintoma where nome=?");
			stmt.setString(1, sympton.getName());
			stmt.execute();
			stmt.close();
		} catch (SQLException e) {
			throw new RuntimeException(e);
		}

	}

	
}

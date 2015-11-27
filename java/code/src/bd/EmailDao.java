package bd;

import java.sql.*;

import modelo.Person;

public class EmailDao {
	private Connection conexao;
	 
	public EmailDao() {
		this.conexao = ConnectionFactory.obterInstancia().obterConexao();
	}
	
	public void addEmail(Person person){
		String sql = "insert into email "
				+ "(cpf,nome,email)" + " values (?,?,?)";
		
		try {
			// prepared statement para inserção
			PreparedStatement stmt = conexao.prepareStatement(sql);

			// seta os valores

			stmt.setString(1, person.getCpf());
			stmt.setString(2, person.getName());
			stmt.setString(3, person.getEmail());
			// executa
			stmt.execute();
			stmt.close();
		} catch (SQLException e) {
			// A SQLException é "encapsulada" em uma RuntimeException
			// para desacoplar o código da API de JDBC
			throw new RuntimeException(e);
		}
		
	}
	
	public void updateEmail(Person person){

		String sql = "update email set email=?"
				+ " where cpf=?";
		try {
			PreparedStatement stmt = conexao.prepareStatement(sql);
			stmt.setString(1, person.getEmail());
			stmt.setString(2, person.getCpf());
			stmt.execute();
			stmt.close();
		} catch (SQLException e) {
			throw new RuntimeException(e);
		}

	}
	
	public void removeEmail(Person person) {
		try {
			PreparedStatement stmt = conexao.prepareStatement("delete "
					+ "from email where cpf=?");
			stmt.setString(1, person.getCpf());
			stmt.execute();
			stmt.close();
		} catch (SQLException e) {
			throw new RuntimeException(e);
		}
	}
	
	
}

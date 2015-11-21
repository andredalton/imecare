package bd;

import java.sql.*;

import modelo.Contato;

public class ContatoDao {
	
	 private Connection conexao;
	 
	   public ContatoDao() {
	     this.conexao = ConnectionFactory.obterInstancia().obterConexao();
	   }

	   public void cleanTable(String table){
		String sql = "delete from " + table;

		try {
			PreparedStatement stmt = conexao.prepareStatement(sql);			
			stmt.execute();
			stmt.close();
		} catch (SQLException e) {
			throw new RuntimeException(e);
		}	
		}
	   
		public void adiciona(Contato contato) {
			
			
			String sql = "insert into contatos "
					+ "(nome,email,endereco,dataNascimento)" + " values (?,?,?,?)";

			try {
				// prepared statement para inserção
				PreparedStatement stmt = conexao.prepareStatement(sql);

				// seta os valores

				stmt.setString(1, contato.getNome());
				stmt.setString(2, contato.getEmail());
				stmt.setString(3, contato.getEndereco());
				stmt.setDate(4, new Date(contato.getDataNascimento()
						.getTimeInMillis()));

				// executa
				stmt.execute();
				stmt.close();
			} catch (SQLException e) {
				// A SQLException é "encapsulada" em uma RuntimeException
				// para desacoplar o código da API de JDBC
				throw new RuntimeException(e);
			}
		}
}

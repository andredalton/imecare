package teste;

import java.sql.Connection;
import java.sql.SQLException;

import bd.ConnectionFactory;

public class TestaConexao {
	public static void main(String[] args) throws SQLException{
		Connection conexao = ConnectionFactory.obterInstancia().obterConexao();
		System.out.println("Conectado");
		conexao.close();
	}
}
	
	
	


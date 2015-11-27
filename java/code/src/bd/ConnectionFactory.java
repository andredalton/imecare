package bd;

import java.sql.*;
import java.util.Properties;

public class ConnectionFactory {

	public static final String NOME_DRIVER = "org.postgresql.Driver";
    public static final String URL_BD = "jdbc:postgresql://postgresql.linux.ime.usp.br:5432/imecare";
	
	public static final String USUARIO_BD = "imecare";
	public static final String SENHA_BD = "projeto";

	private static ConnectionFactory fabricaDeConexao = null;
	
	private ConnectionFactory() {
		try {
			Class.forName(NOME_DRIVER);
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		}
	}
	
	
	public Connection obterConexao() {

		Properties props = new Properties();
		props.setProperty("ssl","true");
		props.setProperty("sslfactory","org.postgresql.ssl.NonValidatingFactory");
		props.setProperty("currentSchema","engSoft");
		props.setProperty("user", USUARIO_BD);
		props.setProperty("password", SENHA_BD);

		try {
			return DriverManager.getConnection(URL_BD, props);
		} catch (SQLException e) {
			// A SQLException é "encapsulada" em uma RuntimeException
			// para desacoplar o código da API de JDBC
			
	
			throw new RuntimeException(e);
		}
	}
	
	public static ConnectionFactory obterInstancia() {
		// A fábrica é um singleton
		if (fabricaDeConexao == null) {
			fabricaDeConexao = new ConnectionFactory();
		}
		return fabricaDeConexao;
	}
	
	
	
}

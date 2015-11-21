package bd;

import java.sql.*;
import java.util.Calendar;

import modelo.Person;
import bd.EmailDao;

public class PersonDao {
	
	private Connection conexao;
	 
	public PersonDao() {
		this.conexao = ConnectionFactory.obterInstancia().obterConexao();
	}

	public void addUser(Person person){
		String sql = "insert into pessoa "
				+ "(cpf,rg,	nome, dt_nascimento)" + " values (?,?,?,?)";
		
		try {
			// prepared statement para inserção
			PreparedStatement stmt = conexao.prepareStatement(sql);
	
			// seta os valores
	
			stmt.setString(1, person.getCpf());
			stmt.setString(2, person.getRg());
			stmt.setString(3, person.getName());
			stmt.setDate(4, new Date(person.getBirthDate().getTimeInMillis()));
			// executa
			stmt.execute();
			stmt.close();
		} catch (SQLException e) {
			// A SQLException é "encapsulada" em uma RuntimeException
			// para desacoplar o código da API de JDBC
			throw new RuntimeException(e);
		}	
		
		EmailDao emailDao = new EmailDao();
		emailDao.addEmail(person);	
	}
	
	
	public void updateUser(Person person){

		String sql = "update pessoa set nome=?, rg=?, dt_nascimento=?"
				+ " where cpf=?";
		try {
			PreparedStatement stmt = conexao.prepareStatement(sql);
			stmt.setString(1, person.getName());
			stmt.setString(2, person.getRg());
			stmt.setDate(3, new Date(person.getBirthDate().getTimeInMillis()));
			stmt.setString(4, person.getCpf());
			stmt.execute();
			stmt.close();
		} catch (SQLException e) {
			throw new RuntimeException(e);
		}

		EmailDao emailDao = new EmailDao();
		emailDao.updateEmail(person);	
	}

	public Person getUser(String cpf){

		try {
			Person person = null;
			
			PreparedStatement stmt = conexao.prepareStatement("select * "
					+ "from pessoa where cpf=?");
			stmt.setString(1, cpf);
			ResultSet rs = stmt.executeQuery();

			if (rs.next()) {
				person = new Person();

				person.setCpf(cpf);
				person.setName(rs.getString("nome"));
				person.setAddress(rs.getString("endereco"));
				person.setEmail(rs.getString("email"));

				Calendar date = Calendar.getInstance();
				date.setTime(rs.getDate("dt_nascimento"));
				person.setBirthDate(date);

			}
			rs.close();
			stmt.close();
			return person;

		} catch (SQLException e) {
			throw new RuntimeException(e);
		}
	}
	
		
	public void removeUser(Person person) {
		try {
			PreparedStatement stmt = conexao.prepareStatement("delete "
					+ "from pessoa where cpf=?");
			stmt.setString(1, person.getCpf());
			stmt.execute();
			stmt.close();
		} catch (SQLException e) {
			throw new RuntimeException(e);
		}

		EmailDao emailDao = new EmailDao();
		emailDao.removeEmail(person);	
	}	
}

package bd;

import java.sql.*;

import modelo.Exam;

public class ExamDao {

	private Connection conexao;
		 
	public ExamDao() {
			this.conexao = ConnectionFactory.obterInstancia().obterConexao();
	}

	public void addExam(Exam exam){
		String sql = "insert into exame "
				+ "(codigo_anvisa,nome,descricao)" + " values (?,?,?)";
		
		try {
			PreparedStatement stmt = conexao.prepareStatement(sql);

			stmt.setInt(1, exam.getAnvisaCode());
			stmt.setString(2, exam.getName());
			stmt.setString(3, exam.getDescription());

			stmt.execute();
			stmt.close();
		} catch (SQLException e) {
			throw new RuntimeException(e);
		}	
	}

	public void updateExam(Exam exam){

		String sql = "update exame set nome=?, descricao=? where codigo_anvisa=?";
		try {
			PreparedStatement stmt = conexao.prepareStatement(sql);
			stmt.setString(1, exam.getName());
			stmt.setString(2, exam.getDescription());
			stmt.setInt(3, exam.getAnvisaCode());
			stmt.execute();
			stmt.close();
		} catch (SQLException e) {
			throw new RuntimeException(e);
		}

	}

	public void removeExam(Exam exam){

		try {
			PreparedStatement stmt = conexao.prepareStatement("delete "
					+ "from exame where codigo_anvisa=?");
			stmt.setInt(1, exam.getAnvisaCode());
			stmt.execute();
			stmt.close();
		} catch (SQLException e) {
			throw new RuntimeException(e);
		}
	}

	public Exam getExam(int code) {

		try {
			Exam exam = new Exam();
				
			PreparedStatement stmt = conexao.prepareStatement("select * "
					+ "from procedimento where codigo_anvisa=?");
			stmt.setInt(1, code);
			ResultSet rs = stmt.executeQuery();

			if (rs.next()) {
				//exam = new Exam();
				exam.setName(rs.getString("nome"));
				exam.setDescription(rs.getString("descricao"));
				exam.setAnvisaCode(code);					
			}
			rs.close();
			stmt.close();
			return exam;

		} catch (SQLException e) {
			throw new RuntimeException(e);
			}
		}

}

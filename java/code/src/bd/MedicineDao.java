package bd;

import java.sql.*;

import modelo.Medicine;


//Obs: Pacientes podiam ter alergias
public class MedicineDao {
	
	private Connection conexao;
	 
	public MedicineDao() {
		this.conexao = ConnectionFactory.obterInstancia().obterConexao();
	}

	public void addMedicine(Medicine medicine){
			String sql = "insert into medicamento "
					+ "(tarja, nome)" + " values (?,?)";
			
			try {
				// prepared statement para inserção
				PreparedStatement stmt = conexao.prepareStatement(sql);
				stmt.setString(1, medicine.getTarja());	
				stmt.setString(2, medicine.getName());			
				// executa
				stmt.execute();
				stmt.close();
			} catch (SQLException e) {
				throw new RuntimeException(e);
			}	
			
	}
	
	// Obs: Medicamentos não tem substâncias no DB
	public void updateMedicine(Medicine medicine){

		String sql = "update medicamento set tarja=? where nome=?";
		try {
			PreparedStatement stmt = conexao.prepareStatement(sql);
			stmt.setString(1, medicine.getTarja());
			stmt.setString(2, medicine.getName());
			stmt.execute();
			stmt.close();
		} catch (SQLException e) {
			throw new RuntimeException(e);
		}
	}

	public void removeMedicine(Medicine medicine) {

		try {
			PreparedStatement stmt = conexao.prepareStatement("delete "
					+ "from medicamento where nome=?");
			stmt.setString(1, medicine.getName());
			stmt.execute();
			stmt.close();
		} catch (SQLException e) {
			throw new RuntimeException(e);
		}
	}
}
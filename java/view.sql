--Visão e tabelas utilizadas para montar o bd (esquema físico)

CREATE VIEW prontuario AS
SELECT  p.*, d.CID, d.nome AS nome_doenca, s.nome AS nome_sintoma, s.descricao AS descricao_sintoma, 
        m.nome AS nome_medicamento, m.tarja, e.codigo_anvisa, e.nome AS nome_exame, e.descricao 
FROM Paciente p, Doenca d, Doenca_Diagnosticada dd, Possui po, Sintoma s, Prescreve pr, Medicamento m, Realiza r, Exame e
WHERE p.cpf = dd.CPF_Paciente AND dd.CID = d.CID AND  d.CID = po.CID AND po.nome_sintoma = s.nome
      AND m.nome = pr.nome_medicamento AND p.cpf= pr.CPF_Paciente AND p.cpf = r.cpf_paciente AND r.codigo_anvisa = e.codigo_anvisa;




CREATE OR REPLACE FUNCTION PacienteInexistente()
	RETURNS TRIGGER AS $$
BEGIN
	IF(NEW.cpf = null OR NEW.cpf NOT IN (SELECT cpf FROM Paciente)) THEN
	 	RETURN NULL;
	END IF;	
	RETURN NEW;
END;
$$ LANGUAGE plpgsql;



CREATE TRIGGER InsereProntuario
INSTEAD OF INSERT OR UPDATE ON  prontuario
FOR EACH ROW
EXECUTE PROCEDURE PacienteInexistente();


--------------------------------------------------------------------
--Consultas

--Usar union, intersect ou except


--Doenças que um paciente já teve (diagnósticos) >>>>>prioridade 1
SELECT
	doenca.nome
FROM
	imecare_diagnosticada diag INNER JOIN
	imecare_doenca doenca ON diag.doenca_id = doenca.cid INNER JOIN
	imecare_pessoa paciente ON paciente.user_ptr_id = diag.paciente_id
WHERE
	paciente.cpf = '000.000.000-00';


--Liste os atendimentos realizados hoje: >>>>>prioridade 2
SELECT
	paciente.cpf, paciente.nome, medico.cpf, medico.nome, atend.horario
FROM
	imecare_atendimento atend INNER JOIN
	imecare_pessoa paciente ON paciente.user_ptr_id = atend.paciente_id INNER JOIN
	imecare_pessoa medico ON medico.user_ptr_id = atend.medico_id
WHERE
	atend.data = (select current_date);

--Selecione para cada paciente, seu nome e a quantidade de procedimentos realizados por ele >>>>prioridade3
SELECT
	(SELECT nome FROM imecare_pessoa WHERE user_ptr_id = rel.paciente_id),
	COUNT(*) as quantidade
FROM
	imecare_realiza rel
GROUP BY
	rel.paciente_id;


-- Quantidade de pacientes atendido por cada médico >>>>prioridade 4
SELECT
	(SELECT nome FROM imecare_pessoa WHERE user_ptr_id = atend.medico_id) as medico,
	COUNT(DISTINCT(atend.paciente_id)) as total
FROM
	imecare_atendimento atend
GROUP BY
	atend.medico_id;
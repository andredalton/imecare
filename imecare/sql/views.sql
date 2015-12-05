-- CREATE TABLE imecare_prontuario (
--     id integer NOT NULL,
--     categoria character varying(20) NOT NULL,
--     texto character varying(255) NOT NULL,
--     data date NOT NULL,
--     medico_id integer,
--     paciente_id integer NOT NULL
-- );

CREATE VIEW imecare_prontuario AS
SELECT
  *
FROM
  (
    (
      SELECT
        round(random() * 50000000 + 1) AS id,
        'diagnostico' AS categoria,
        doenca.nome   AS texto,
        diag.inicio   AS data,
        atendimento.medico_id AS medico_id,
        diag.paciente_id AS paciente_id
      FROM
        imecare_diagnosticada diag INNER JOIN
        imecare_doenca doenca ON diag.doenca_id = doenca.cid INNER JOIN
        imecare_atendimento atendimento ON atendimento.id = diag.atendimento_id
    )
    UNION
    (
      SELECT
        round(random() * 50000000 + 1) AS id,
        'cura'       AS categoria,
        doenca.nome  AS texto,
        diag.fim     AS data,
        atendimento.medico_id AS medico_id,
        diag.paciente_id AS paciente_id
      FROM
        imecare_diagnosticada diag INNER JOIN
        imecare_doenca doenca ON diag.doenca_id = doenca.cid INNER JOIN
        imecare_atendimento atendimento ON atendimento.id = diag.atendimento_id
      WHERE
        diag.fim IS NOT NULL
    )
    UNION
    (
      SELECT
        round(random() * 50000000 + 1) AS id,
        'atendimento' AS categoria,
        atendimento.comentarios  AS texto,
        atendimento.data AS data,
        atendimento.medico_id AS medico_id,
        atendimento.paciente_id AS paciente_id
      FROM
          imecare_atendimento atendimento INNER JOIN
          imecare_pessoa paciente ON atendimento.paciente_id = paciente.user_ptr_id INNER JOIN
          imecare_pessoa medico ON atendimento.medico_id = medico.user_ptr_id
        WHERE
          character_length(atendimento.comentarios) > 0
    )
    UNION
    (
      SELECT
        round(random() * 50000000 + 1) AS id,
        'prescrição' AS categoria,
        sol.procedimento_id  AS texto,
        atendimento.data AS data,
	atendimento.medico_id AS medico_id,
	atendimento.paciente_id AS paciente_id
      FROM
          imecare_solicita sol INNER JOIN
          imecare_atendimento atendimento ON atendimento.id = sol.atendimento_id
    )
    UNION
    (
      SELECT
        round(random() * 50000000 + 1) AS id,
        'realização' AS categoria,
        rel.procedimento_id  AS texto,
        rel.data AS data,
        CASE
          WHEN rel.solicitacao_id IS NULL THEN NULL
          ELSE
            (
              SELECT
                atend.medico_id
              FROM
                imecare_solicita sol INNER JOIN
                imecare_atendimento atend ON sol.atendimento_id = atend.id
              WHERE
                sol.id = rel.solicitacao_id
            )
        END,
	rel.paciente_id AS paciente_id
      FROM
          imecare_realiza rel
    )
  ) as prontuario
ORDER BY data DESC;
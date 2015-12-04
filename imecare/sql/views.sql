SELECT
  *
FROM
  (
    (
      SELECT
        'diagnostico' AS categoria,
        paciente.cpf  AS paciente_cpf,
        medico.cpf    AS medico_cpf,
        doenca.nome   AS titulo,
        diag.inicio   AS data_evento
      FROM
        imecare_diagnosticada diag INNER JOIN
        imecare_pessoa paciente ON diag.paciente_id = paciente.user_ptr_id
        INNER JOIN
        imecare_doenca doenca ON diag.doenca_id = doenca.cid
        INNER JOIN
        imecare_atendimento atendimento ON atendimento.id = diag.atendimento_id
        INNER JOIN
        imecare_pessoa medico ON atendimento.medico_id = medico.user_ptr_id
    )
    UNION
    (
      SELECT
        'cura'       AS categoria,
        paciente.cpf AS paciente_cpf,
        medico.cpf   AS medico_cpf,
        doenca.nome  AS titulo,
        diag.fim     AS data_evento
      FROM
        imecare_diagnosticada diag INNER JOIN
        imecare_pessoa paciente ON diag.paciente_id = paciente.user_ptr_id
        INNER JOIN
        imecare_doenca doenca ON diag.doenca_id = doenca.cid
        INNER JOIN
        imecare_atendimento atendimento ON atendimento.id = diag.atendimento_id
        INNER JOIN
        imecare_pessoa medico ON atendimento.medico_id = medico.user_ptr_id
      WHERE
        diag.fim IS NOT NULL
    )
    UNION
    (
      SELECT
        'atendimento' AS categoria,
        paciente.cpf AS paciente_cpf,
        medico.cpf   AS medico_cpf,
        atendimento.comentarios  AS titulo,
        atendimento.data     AS data_evento
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
        'prescricao' AS categoria,
        paciente.cpf AS paciente_cpf,
        medico.cpf   AS medico_cpf,
        sol.procedimento_id  AS titulo,
        atendimento.data AS data_evento
      FROM
          imecare_solicita sol INNER JOIN
          imecare_atendimento atendimento ON atendimento.id = sol.atendimento_id INNER JOIN
          imecare_pessoa paciente ON atendimento.paciente_id = paciente.user_ptr_id INNER JOIN
          imecare_pessoa medico ON atendimento.medico_id = medico.user_ptr_id
    )
  ) as prontuario
ORDER BY data_evento DESC;
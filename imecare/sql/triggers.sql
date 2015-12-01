-- Trigger para auto-inserção de doença em paciente uma vez que se insere o diagnóstico no atendimento
CREATE OR REPLACE FUNCTION DoencaDiagnosticadaEmPaciente()
    RETURNS TRIGGER AS $$
BEGIN
    IF((NEW.atendimento_id = null) OR NEW.doenca_id = null) THEN
        RETURN NULL;
    END IF; 
    INSERT INTO
        imecare_diagnosticadaem (doenca_id, paciente_id)
        VALUES
        (
            NEW.doenca_id, 
            (SELECT paciente_id FROM imecare_atendimento WHERE id = NEW.atendimento_id)
        );
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER InsereDiagnostico
BEFORE INSERT on imecare_diagnosticada
FOR EACH ROW
EXECUTE PROCEDURE DoencaDiagnosticadaEmPaciente();
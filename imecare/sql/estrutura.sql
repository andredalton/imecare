--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: labbd; Type: SCHEMA; Schema: -; Owner: imecare
--

CREATE SCHEMA labbd;


ALTER SCHEMA labbd OWNER TO imecare;

SET search_path = labbd, pg_catalog;

--
-- Name: doencadiagnosticadaempaciente(); Type: FUNCTION; Schema: labbd; Owner: imecare
--

CREATE FUNCTION doencadiagnosticadaempaciente() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
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
$$;


ALTER FUNCTION labbd.doencadiagnosticadaempaciente() OWNER TO imecare;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE auth_group OWNER TO imecare;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: labbd; Owner: imecare
--

CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_group_id_seq OWNER TO imecare;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: labbd; Owner: imecare
--

ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE auth_group_permissions OWNER TO imecare;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: labbd; Owner: imecare
--

CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_group_permissions_id_seq OWNER TO imecare;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: labbd; Owner: imecare
--

ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE auth_permission OWNER TO imecare;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: labbd; Owner: imecare
--

CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_permission_id_seq OWNER TO imecare;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: labbd; Owner: imecare
--

ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE TABLE auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(30) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE auth_user OWNER TO imecare;

--
-- Name: auth_user_groups; Type: TABLE; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE TABLE auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE auth_user_groups OWNER TO imecare;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: labbd; Owner: imecare
--

CREATE SEQUENCE auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_groups_id_seq OWNER TO imecare;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: labbd; Owner: imecare
--

ALTER SEQUENCE auth_user_groups_id_seq OWNED BY auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: labbd; Owner: imecare
--

CREATE SEQUENCE auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_id_seq OWNER TO imecare;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: labbd; Owner: imecare
--

ALTER SEQUENCE auth_user_id_seq OWNED BY auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE TABLE auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE auth_user_user_permissions OWNER TO imecare;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: labbd; Owner: imecare
--

CREATE SEQUENCE auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_user_permissions_id_seq OWNER TO imecare;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: labbd; Owner: imecare
--

ALTER SEQUENCE auth_user_user_permissions_id_seq OWNED BY auth_user_user_permissions.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE TABLE django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE django_admin_log OWNER TO imecare;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: labbd; Owner: imecare
--

CREATE SEQUENCE django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_admin_log_id_seq OWNER TO imecare;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: labbd; Owner: imecare
--

ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE TABLE django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE django_content_type OWNER TO imecare;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: labbd; Owner: imecare
--

CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_content_type_id_seq OWNER TO imecare;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: labbd; Owner: imecare
--

ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE TABLE django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE django_migrations OWNER TO imecare;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: labbd; Owner: imecare
--

CREATE SEQUENCE django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_migrations_id_seq OWNER TO imecare;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: labbd; Owner: imecare
--

ALTER SEQUENCE django_migrations_id_seq OWNED BY django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE django_session OWNER TO imecare;

--
-- Name: imecare_atendimento; Type: TABLE; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE TABLE imecare_atendimento (
    id integer NOT NULL,
    comentarios text NOT NULL,
    data date NOT NULL,
    horario time without time zone NOT NULL,
    medico_id integer NOT NULL,
    paciente_id integer NOT NULL
);


ALTER TABLE imecare_atendimento OWNER TO imecare;

--
-- Name: imecare_atendimento_id_seq; Type: SEQUENCE; Schema: labbd; Owner: imecare
--

CREATE SEQUENCE imecare_atendimento_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE imecare_atendimento_id_seq OWNER TO imecare;

--
-- Name: imecare_atendimento_id_seq; Type: SEQUENCE OWNED BY; Schema: labbd; Owner: imecare
--

ALTER SEQUENCE imecare_atendimento_id_seq OWNED BY imecare_atendimento.id;


--
-- Name: imecare_diagnosticada; Type: TABLE; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE TABLE imecare_diagnosticada (
    id integer NOT NULL,
    cronica boolean NOT NULL,
    inicio date NOT NULL,
    fim date,
    atendimento_id integer NOT NULL,
    doenca_id character varying(15) NOT NULL,
    paciente_id integer NOT NULL
);


ALTER TABLE imecare_diagnosticada OWNER TO imecare;

--
-- Name: imecare_diagnosticada_id_seq; Type: SEQUENCE; Schema: labbd; Owner: imecare
--

CREATE SEQUENCE imecare_diagnosticada_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE imecare_diagnosticada_id_seq OWNER TO imecare;

--
-- Name: imecare_diagnosticada_id_seq; Type: SEQUENCE OWNED BY; Schema: labbd; Owner: imecare
--

ALTER SEQUENCE imecare_diagnosticada_id_seq OWNED BY imecare_diagnosticada.id;


--
-- Name: imecare_doenca; Type: TABLE; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE TABLE imecare_doenca (
    nome character varying(255) NOT NULL,
    cid character varying(15) NOT NULL,
    generica_id character varying(15)
);


ALTER TABLE imecare_doenca OWNER TO imecare;

--
-- Name: imecare_pessoa; Type: TABLE; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE TABLE imecare_pessoa (
    user_ptr_id integer NOT NULL,
    nome character varying(150) NOT NULL,
    rg character varying(15) NOT NULL,
    cpf character varying(15) NOT NULL,
    crm character varying(15),
    tipo_sanguineo character varying(3) NOT NULL,
    data_nascimento date NOT NULL
);


ALTER TABLE imecare_pessoa OWNER TO imecare;

--
-- Name: imecare_procedimento; Type: TABLE; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE TABLE imecare_procedimento (
    nome character varying(100) NOT NULL
);


ALTER TABLE imecare_procedimento OWNER TO imecare;

--
-- Name: imecare_realiza; Type: TABLE; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE TABLE imecare_realiza (
    id integer NOT NULL,
    data date NOT NULL,
    horario time without time zone NOT NULL,
    paciente_id integer NOT NULL,
    procedimento_id character varying(100) NOT NULL,
    solicitacao_id integer
);


ALTER TABLE imecare_realiza OWNER TO imecare;

--
-- Name: imecare_solicita; Type: TABLE; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE TABLE imecare_solicita (
    id integer NOT NULL,
    detalhes text NOT NULL,
    atendimento_id integer NOT NULL,
    procedimento_id character varying(100) NOT NULL
);


ALTER TABLE imecare_solicita OWNER TO imecare;

--
-- Name: imecare_prontuario; Type: VIEW; Schema: labbd; Owner: imecare
--

CREATE VIEW imecare_prontuario AS
 SELECT prontuario.id,
    prontuario.categoria,
    prontuario.texto,
    prontuario.data,
    prontuario.medico_id,
    prontuario.paciente_id
   FROM ( SELECT round(((random() * (50000000)::double precision) + (1)::double precision)) AS id,
            'diagnostico'::text AS categoria,
            doenca.nome AS texto,
            diag.inicio AS data,
            atendimento.medico_id,
            diag.paciente_id
           FROM ((imecare_diagnosticada diag
             JOIN imecare_doenca doenca ON (((diag.doenca_id)::text = (doenca.cid)::text)))
             JOIN imecare_atendimento atendimento ON ((atendimento.id = diag.atendimento_id)))
        UNION
         SELECT round(((random() * (50000000)::double precision) + (1)::double precision)) AS id,
            'cura'::text AS categoria,
            doenca.nome AS texto,
            diag.fim AS data,
            atendimento.medico_id,
            diag.paciente_id
           FROM ((imecare_diagnosticada diag
             JOIN imecare_doenca doenca ON (((diag.doenca_id)::text = (doenca.cid)::text)))
             JOIN imecare_atendimento atendimento ON ((atendimento.id = diag.atendimento_id)))
          WHERE (diag.fim IS NOT NULL)
        UNION
         SELECT round(((random() * (50000000)::double precision) + (1)::double precision)) AS id,
            'atendimento'::text AS categoria,
            atendimento.comentarios AS texto,
            atendimento.data,
            atendimento.medico_id,
            atendimento.paciente_id
           FROM ((imecare_atendimento atendimento
             JOIN imecare_pessoa paciente ON ((atendimento.paciente_id = paciente.user_ptr_id)))
             JOIN imecare_pessoa medico ON ((atendimento.medico_id = medico.user_ptr_id)))
          WHERE (character_length(atendimento.comentarios) > 0)
        UNION
         SELECT round(((random() * (50000000)::double precision) + (1)::double precision)) AS id,
            'prescrição'::text AS categoria,
            sol.procedimento_id AS texto,
            atendimento.data,
            atendimento.medico_id,
            atendimento.paciente_id
           FROM (imecare_solicita sol
             JOIN imecare_atendimento atendimento ON ((atendimento.id = sol.atendimento_id)))
        UNION
         SELECT round(((random() * (50000000)::double precision) + (1)::double precision)) AS id,
            'realização'::text AS categoria,
            rel.procedimento_id AS texto,
            rel.data,
                CASE
                    WHEN (rel.solicitacao_id IS NULL) THEN NULL::integer
                    ELSE ( SELECT atend.medico_id
                       FROM (imecare_solicita sol
                         JOIN imecare_atendimento atend ON ((sol.atendimento_id = atend.id)))
                      WHERE (sol.id = rel.solicitacao_id))
                END AS medico_id,
            rel.paciente_id
           FROM imecare_realiza rel) prontuario
  ORDER BY prontuario.data DESC;


ALTER TABLE imecare_prontuario OWNER TO imecare;

--
-- Name: imecare_realiza_id_seq; Type: SEQUENCE; Schema: labbd; Owner: imecare
--

CREATE SEQUENCE imecare_realiza_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE imecare_realiza_id_seq OWNER TO imecare;

--
-- Name: imecare_realiza_id_seq; Type: SEQUENCE OWNED BY; Schema: labbd; Owner: imecare
--

ALTER SEQUENCE imecare_realiza_id_seq OWNED BY imecare_realiza.id;


--
-- Name: imecare_solicita_id_seq; Type: SEQUENCE; Schema: labbd; Owner: imecare
--

CREATE SEQUENCE imecare_solicita_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE imecare_solicita_id_seq OWNER TO imecare;

--
-- Name: imecare_solicita_id_seq; Type: SEQUENCE OWNED BY; Schema: labbd; Owner: imecare
--

ALTER SEQUENCE imecare_solicita_id_seq OWNED BY imecare_solicita.id;


--
-- Name: id; Type: DEFAULT; Schema: labbd; Owner: imecare
--

ALTER TABLE ONLY auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: labbd; Owner: imecare
--

ALTER TABLE ONLY auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: labbd; Owner: imecare
--

ALTER TABLE ONLY auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: labbd; Owner: imecare
--

ALTER TABLE ONLY auth_user ALTER COLUMN id SET DEFAULT nextval('auth_user_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: labbd; Owner: imecare
--

ALTER TABLE ONLY auth_user_groups ALTER COLUMN id SET DEFAULT nextval('auth_user_groups_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: labbd; Owner: imecare
--

ALTER TABLE ONLY auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('auth_user_user_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: labbd; Owner: imecare
--

ALTER TABLE ONLY django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: labbd; Owner: imecare
--

ALTER TABLE ONLY django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: labbd; Owner: imecare
--

ALTER TABLE ONLY django_migrations ALTER COLUMN id SET DEFAULT nextval('django_migrations_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: labbd; Owner: imecare
--

ALTER TABLE ONLY imecare_atendimento ALTER COLUMN id SET DEFAULT nextval('imecare_atendimento_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: labbd; Owner: imecare
--

ALTER TABLE ONLY imecare_diagnosticada ALTER COLUMN id SET DEFAULT nextval('imecare_diagnosticada_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: labbd; Owner: imecare
--

ALTER TABLE ONLY imecare_realiza ALTER COLUMN id SET DEFAULT nextval('imecare_realiza_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: labbd; Owner: imecare
--

ALTER TABLE ONLY imecare_solicita ALTER COLUMN id SET DEFAULT nextval('imecare_solicita_id_seq'::regclass);


--
-- Name: auth_group_name_key; Type: CONSTRAINT; Schema: labbd; Owner: imecare; Tablespace:
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions_group_id_permission_id_key; Type: CONSTRAINT; Schema: labbd; Owner: imecare; Tablespace:
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_key UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions_pkey; Type: CONSTRAINT; Schema: labbd; Owner: imecare; Tablespace:
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group_pkey; Type: CONSTRAINT; Schema: labbd; Owner: imecare; Tablespace:
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission_content_type_id_codename_key; Type: CONSTRAINT; Schema: labbd; Owner: imecare; Tablespace:
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_key UNIQUE (content_type_id, codename);


--
-- Name: auth_permission_pkey; Type: CONSTRAINT; Schema: labbd; Owner: imecare; Tablespace:
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_pkey; Type: CONSTRAINT; Schema: labbd; Owner: imecare; Tablespace:
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_user_id_group_id_key; Type: CONSTRAINT; Schema: labbd; Owner: imecare; Tablespace:
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_key UNIQUE (user_id, group_id);


--
-- Name: auth_user_pkey; Type: CONSTRAINT; Schema: labbd; Owner: imecare; Tablespace:
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: labbd; Owner: imecare; Tablespace:
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_user_id_permission_id_key; Type: CONSTRAINT; Schema: labbd; Owner: imecare; Tablespace:
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_key UNIQUE (user_id, permission_id);


--
-- Name: auth_user_username_key; Type: CONSTRAINT; Schema: labbd; Owner: imecare; Tablespace:
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log_pkey; Type: CONSTRAINT; Schema: labbd; Owner: imecare; Tablespace:
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type_app_label_45f3b1d93ec8c61c_uniq; Type: CONSTRAINT; Schema: labbd; Owner: imecare; Tablespace:
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_45f3b1d93ec8c61c_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type_pkey; Type: CONSTRAINT; Schema: labbd; Owner: imecare; Tablespace:
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations_pkey; Type: CONSTRAINT; Schema: labbd; Owner: imecare; Tablespace:
--

ALTER TABLE ONLY django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session_pkey; Type: CONSTRAINT; Schema: labbd; Owner: imecare; Tablespace:
--

ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: imecare_atendimento_medico_id_3d14aadf080ff0e1_uniq; Type: CONSTRAINT; Schema: labbd; Owner: imecare; Tablespace:
--

ALTER TABLE ONLY imecare_atendimento
    ADD CONSTRAINT imecare_atendimento_medico_id_3d14aadf080ff0e1_uniq UNIQUE (medico_id, paciente_id, data, horario);


--
-- Name: imecare_atendimento_pkey; Type: CONSTRAINT; Schema: labbd; Owner: imecare; Tablespace:
--

ALTER TABLE ONLY imecare_atendimento
    ADD CONSTRAINT imecare_atendimento_pkey PRIMARY KEY (id);


--
-- Name: imecare_diagnosticada_pkey; Type: CONSTRAINT; Schema: labbd; Owner: imecare; Tablespace:
--

ALTER TABLE ONLY imecare_diagnosticada
    ADD CONSTRAINT imecare_diagnosticada_pkey PRIMARY KEY (id);


--
-- Name: imecare_doenca_nome_key; Type: CONSTRAINT; Schema: labbd; Owner: imecare; Tablespace:
--

ALTER TABLE ONLY imecare_doenca
    ADD CONSTRAINT imecare_doenca_nome_key UNIQUE (nome);


--
-- Name: imecare_doenca_pkey; Type: CONSTRAINT; Schema: labbd; Owner: imecare; Tablespace:
--

ALTER TABLE ONLY imecare_doenca
    ADD CONSTRAINT imecare_doenca_pkey PRIMARY KEY (cid);


--
-- Name: imecare_pessoa_cpf_key; Type: CONSTRAINT; Schema: labbd; Owner: imecare; Tablespace:
--

ALTER TABLE ONLY imecare_pessoa
    ADD CONSTRAINT imecare_pessoa_cpf_key UNIQUE (cpf);


--
-- Name: imecare_pessoa_crm_key; Type: CONSTRAINT; Schema: labbd; Owner: imecare; Tablespace:
--

ALTER TABLE ONLY imecare_pessoa
    ADD CONSTRAINT imecare_pessoa_crm_key UNIQUE (crm);


--
-- Name: imecare_pessoa_pkey; Type: CONSTRAINT; Schema: labbd; Owner: imecare; Tablespace:
--

ALTER TABLE ONLY imecare_pessoa
    ADD CONSTRAINT imecare_pessoa_pkey PRIMARY KEY (user_ptr_id);


--
-- Name: imecare_pessoa_rg_key; Type: CONSTRAINT; Schema: labbd; Owner: imecare; Tablespace:
--

ALTER TABLE ONLY imecare_pessoa
    ADD CONSTRAINT imecare_pessoa_rg_key UNIQUE (rg);


--
-- Name: imecare_procedimento_pkey; Type: CONSTRAINT; Schema: labbd; Owner: imecare; Tablespace:
--

ALTER TABLE ONLY imecare_procedimento
    ADD CONSTRAINT imecare_procedimento_pkey PRIMARY KEY (nome);


--
-- Name: imecare_realiza_pkey; Type: CONSTRAINT; Schema: labbd; Owner: imecare; Tablespace:
--

ALTER TABLE ONLY imecare_realiza
    ADD CONSTRAINT imecare_realiza_pkey PRIMARY KEY (id);


--
-- Name: imecare_solicita_pkey; Type: CONSTRAINT; Schema: labbd; Owner: imecare; Tablespace:
--

ALTER TABLE ONLY imecare_solicita
    ADD CONSTRAINT imecare_solicita_pkey PRIMARY KEY (id);


--
-- Name: auth_group_name_253ae2a6331666e8_like; Type: INDEX; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE INDEX auth_group_name_253ae2a6331666e8_like ON auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_0e939a4f; Type: INDEX; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE INDEX auth_group_permissions_0e939a4f ON auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_8373b171; Type: INDEX; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE INDEX auth_group_permissions_8373b171 ON auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_417f1b1c; Type: INDEX; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE INDEX auth_permission_417f1b1c ON auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_0e939a4f; Type: INDEX; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE INDEX auth_user_groups_0e939a4f ON auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_e8701ad4; Type: INDEX; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE INDEX auth_user_groups_e8701ad4 ON auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_8373b171; Type: INDEX; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE INDEX auth_user_user_permissions_8373b171 ON auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_e8701ad4; Type: INDEX; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE INDEX auth_user_user_permissions_e8701ad4 ON auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_51b3b110094b8aae_like; Type: INDEX; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE INDEX auth_user_username_51b3b110094b8aae_like ON auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_417f1b1c; Type: INDEX; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE INDEX django_admin_log_417f1b1c ON django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_e8701ad4; Type: INDEX; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE INDEX django_admin_log_e8701ad4 ON django_admin_log USING btree (user_id);


--
-- Name: django_session_de54fa62; Type: INDEX; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE INDEX django_session_de54fa62 ON django_session USING btree (expire_date);


--
-- Name: django_session_session_key_461cfeaa630ca218_like; Type: INDEX; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE INDEX django_session_session_key_461cfeaa630ca218_like ON django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: imecare_atendimento_88edd913; Type: INDEX; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE INDEX imecare_atendimento_88edd913 ON imecare_atendimento USING btree (medico_id);


--
-- Name: imecare_atendimento_f7989c29; Type: INDEX; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE INDEX imecare_atendimento_f7989c29 ON imecare_atendimento USING btree (paciente_id);


--
-- Name: imecare_diagnosticada_2be3109b; Type: INDEX; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE INDEX imecare_diagnosticada_2be3109b ON imecare_diagnosticada USING btree (atendimento_id);


--
-- Name: imecare_diagnosticada_3ccef179; Type: INDEX; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE INDEX imecare_diagnosticada_3ccef179 ON imecare_diagnosticada USING btree (doenca_id);


--
-- Name: imecare_diagnosticada_f7989c29; Type: INDEX; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE INDEX imecare_diagnosticada_f7989c29 ON imecare_diagnosticada USING btree (paciente_id);


--
-- Name: imecare_doenca_cid_3a918325f6802ba3_like; Type: INDEX; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE INDEX imecare_doenca_cid_3a918325f6802ba3_like ON imecare_doenca USING btree (cid varchar_pattern_ops);


--
-- Name: imecare_doenca_ffc40d82; Type: INDEX; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE INDEX imecare_doenca_ffc40d82 ON imecare_doenca USING btree (generica_id);


--
-- Name: imecare_doenca_generica_id_bdda4717a8bc0fd_like; Type: INDEX; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE INDEX imecare_doenca_generica_id_bdda4717a8bc0fd_like ON imecare_doenca USING btree (generica_id varchar_pattern_ops);


--
-- Name: imecare_doenca_nome_6d867965df55dee3_like; Type: INDEX; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE INDEX imecare_doenca_nome_6d867965df55dee3_like ON imecare_doenca USING btree (nome varchar_pattern_ops);


--
-- Name: imecare_pessoa_cpf_78c0ffda0ed7b343_like; Type: INDEX; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE INDEX imecare_pessoa_cpf_78c0ffda0ed7b343_like ON imecare_pessoa USING btree (cpf varchar_pattern_ops);


--
-- Name: imecare_pessoa_crm_78c10614ba8f7230_like; Type: INDEX; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE INDEX imecare_pessoa_crm_78c10614ba8f7230_like ON imecare_pessoa USING btree (crm varchar_pattern_ops);


--
-- Name: imecare_pessoa_rg_3630e85a0821f0fc_like; Type: INDEX; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE INDEX imecare_pessoa_rg_3630e85a0821f0fc_like ON imecare_pessoa USING btree (rg varchar_pattern_ops);


--
-- Name: imecare_procedimento_nome_55e60f2a18f5f75e_like; Type: INDEX; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE INDEX imecare_procedimento_nome_55e60f2a18f5f75e_like ON imecare_procedimento USING btree (nome varchar_pattern_ops);


--
-- Name: imecare_realiza_1b1fabd9; Type: INDEX; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE INDEX imecare_realiza_1b1fabd9 ON imecare_realiza USING btree (solicitacao_id);


--
-- Name: imecare_realiza_9145380d; Type: INDEX; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE INDEX imecare_realiza_9145380d ON imecare_realiza USING btree (procedimento_id);


--
-- Name: imecare_realiza_f7989c29; Type: INDEX; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE INDEX imecare_realiza_f7989c29 ON imecare_realiza USING btree (paciente_id);


--
-- Name: imecare_realiza_procedimento_id_1bd6fdae17cf4b85_like; Type: INDEX; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE INDEX imecare_realiza_procedimento_id_1bd6fdae17cf4b85_like ON imecare_realiza USING btree (procedimento_id varchar_pattern_ops);


--
-- Name: imecare_solicita_2be3109b; Type: INDEX; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE INDEX imecare_solicita_2be3109b ON imecare_solicita USING btree (atendimento_id);


--
-- Name: imecare_solicita_9145380d; Type: INDEX; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE INDEX imecare_solicita_9145380d ON imecare_solicita USING btree (procedimento_id);


--
-- Name: imecare_solicita_procedimento_id_597bb633b2d08a78_like; Type: INDEX; Schema: labbd; Owner: imecare; Tablespace:
--

CREATE INDEX imecare_solicita_procedimento_id_597bb633b2d08a78_like ON imecare_solicita USING btree (procedimento_id varchar_pattern_ops);


--
-- Name: auth_content_type_id_508cf46651277a81_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: labbd; Owner: imecare
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_content_type_id_508cf46651277a81_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissio_group_id_689710a9a73b7457_fk_auth_group_id; Type: FK CONSTRAINT; Schema: labbd; Owner: imecare
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_group_id_689710a9a73b7457_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id; Type: FK CONSTRAINT; Schema: labbd; Owner: imecare
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user__permission_id_384b62483d7071f0_fk_auth_permission_id; Type: FK CONSTRAINT; Schema: labbd; Owner: imecare
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user__permission_id_384b62483d7071f0_fk_auth_permission_id FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id; Type: FK CONSTRAINT; Schema: labbd; Owner: imecare
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id; Type: FK CONSTRAINT; Schema: labbd; Owner: imecare
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permiss_user_id_7f0938558328534a_fk_auth_user_id; Type: FK CONSTRAINT; Schema: labbd; Owner: imecare
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permiss_user_id_7f0938558328534a_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: djan_content_type_id_697914295151027a_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: labbd; Owner: imecare
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT djan_content_type_id_697914295151027a_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id; Type: FK CONSTRAINT; Schema: labbd; Owner: imecare
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: i_procedimento_id_1bd6fdae17cf4b85_fk_imecare_procedimento_nome; Type: FK CONSTRAINT; Schema: labbd; Owner: imecare
--

ALTER TABLE ONLY imecare_realiza
    ADD CONSTRAINT i_procedimento_id_1bd6fdae17cf4b85_fk_imecare_procedimento_nome FOREIGN KEY (procedimento_id) REFERENCES imecare_procedimento(nome) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: i_procedimento_id_597bb633b2d08a78_fk_imecare_procedimento_nome; Type: FK CONSTRAINT; Schema: labbd; Owner: imecare
--

ALTER TABLE ONLY imecare_solicita
    ADD CONSTRAINT i_procedimento_id_597bb633b2d08a78_fk_imecare_procedimento_nome FOREIGN KEY (procedimento_id) REFERENCES imecare_procedimento(nome) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: imec_paciente_id_4bdba0ff40f324b7_fk_imecare_pessoa_user_ptr_id; Type: FK CONSTRAINT; Schema: labbd; Owner: imecare
--

ALTER TABLE ONLY imecare_realiza
    ADD CONSTRAINT imec_paciente_id_4bdba0ff40f324b7_fk_imecare_pessoa_user_ptr_id FOREIGN KEY (paciente_id) REFERENCES imecare_pessoa(user_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: imec_paciente_id_5ff5216e922eba84_fk_imecare_pessoa_user_ptr_id; Type: FK CONSTRAINT; Schema: labbd; Owner: imecare
--

ALTER TABLE ONLY imecare_diagnosticada
    ADD CONSTRAINT imec_paciente_id_5ff5216e922eba84_fk_imecare_pessoa_user_ptr_id FOREIGN KEY (paciente_id) REFERENCES imecare_pessoa(user_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: imec_paciente_id_7c3149484ece77b7_fk_imecare_pessoa_user_ptr_id; Type: FK CONSTRAINT; Schema: labbd; Owner: imecare
--

ALTER TABLE ONLY imecare_atendimento
    ADD CONSTRAINT imec_paciente_id_7c3149484ece77b7_fk_imecare_pessoa_user_ptr_id FOREIGN KEY (paciente_id) REFERENCES imecare_pessoa(user_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: imeca_atendimento_id_13bf074ef803d2b8_fk_imecare_atendimento_id; Type: FK CONSTRAINT; Schema: labbd; Owner: imecare
--

ALTER TABLE ONLY imecare_diagnosticada
    ADD CONSTRAINT imeca_atendimento_id_13bf074ef803d2b8_fk_imecare_atendimento_id FOREIGN KEY (atendimento_id) REFERENCES imecare_atendimento(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: imeca_atendimento_id_57fbcb3d89f3b8c6_fk_imecare_atendimento_id; Type: FK CONSTRAINT; Schema: labbd; Owner: imecare
--

ALTER TABLE ONLY imecare_solicita
    ADD CONSTRAINT imeca_atendimento_id_57fbcb3d89f3b8c6_fk_imecare_atendimento_id FOREIGN KEY (atendimento_id) REFERENCES imecare_atendimento(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: imecar_medico_id_70ed55c3ffd7fc17_fk_imecare_pessoa_user_ptr_id; Type: FK CONSTRAINT; Schema: labbd; Owner: imecare
--

ALTER TABLE ONLY imecare_atendimento
    ADD CONSTRAINT imecar_medico_id_70ed55c3ffd7fc17_fk_imecare_pessoa_user_ptr_id FOREIGN KEY (medico_id) REFERENCES imecare_pessoa(user_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: imecare_diagno_doenca_id_3d73cef44aea888f_fk_imecare_doenca_cid; Type: FK CONSTRAINT; Schema: labbd; Owner: imecare
--

ALTER TABLE ONLY imecare_diagnosticada
    ADD CONSTRAINT imecare_diagno_doenca_id_3d73cef44aea888f_fk_imecare_doenca_cid FOREIGN KEY (doenca_id) REFERENCES imecare_doenca(cid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: imecare_doenc_generica_id_bdda4717a8bc0fd_fk_imecare_doenca_cid; Type: FK CONSTRAINT; Schema: labbd; Owner: imecare
--

ALTER TABLE ONLY imecare_doenca
    ADD CONSTRAINT imecare_doenc_generica_id_bdda4717a8bc0fd_fk_imecare_doenca_cid FOREIGN KEY (generica_id) REFERENCES imecare_doenca(cid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: imecare_pessoa_user_ptr_id_7317d2564fb35c6a_fk_auth_user_id; Type: FK CONSTRAINT; Schema: labbd; Owner: imecare
--

ALTER TABLE ONLY imecare_pessoa
    ADD CONSTRAINT imecare_pessoa_user_ptr_id_7317d2564fb35c6a_fk_auth_user_id FOREIGN KEY (user_ptr_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: imecare_r_solicitacao_id_3497f5633597df8_fk_imecare_solicita_id; Type: FK CONSTRAINT; Schema: labbd; Owner: imecare
--

ALTER TABLE ONLY imecare_realiza
    ADD CONSTRAINT imecare_r_solicitacao_id_3497f5633597df8_fk_imecare_solicita_id FOREIGN KEY (solicitacao_id) REFERENCES imecare_solicita(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

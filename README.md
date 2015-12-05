IMECARE - Prontuário digital
========

<!--[![alt tag](https://codeclimate.com/github/ocr-doacao/cvocr/badges/gpa.svg)](https://codeclimate.com/github/ocr-doacao/cvocr)-->

Desenvolvimento de um sistema de armazenamento de informações médicas em larga escala.

Utilização
========

Inicializar a aplicação:

python manage.py runserver IP:PORTA

Instalação
========

É necessário instalar as dependências de python (requirements.txt)

pip install -r requirements.txt

Uma vez instaladas as dependências e o django esteja funcionando corretamente, não se deve fazer a migração dos modelos,
já que o modelo Prontuário é implementado como uma visão.

Então é necessário recriar o banco através do arquivo: imecare/sql/estruturas.sql

Também é necessário inserir dados de doenças (imecare/sql/insert_doenca_principal.sql) e de
procedimentos (imecare/sql/insert_procedimentos.sql) antes do sistema funcionar.

Utilização
========

Uma vez que o sistema esteja instalado, basta iniciar o serviço a partir do comando:

python manage.py runserver 0.0.0.0:8080 

Pode ser passado a este comando um IP e uma porta de acesso diferentes.

Os pacientes e os médicos podem ser cadastrados a partir da página inicial do site. 
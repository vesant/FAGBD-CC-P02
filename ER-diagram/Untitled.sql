CREATE TABLE `Users` (
  `id_user` INTEGER PRIMARY KEY NOT NULL,
  `login` TEXT,
  `senha` TEXT,
  `tipo_user` TEXT
);

CREATE TABLE `Paciente` (
  `id_paciente` INTEGER PRIMARY KEY NOT NULL,
  `nome` TEXT,
  `data_nascimento` TEXT,
  `genero` TEXT,
  `contato` TEXT,
  `prontuario` TEXT
);

CREATE TABLE `Medico` (
  `id_medico` INTEGER PRIMARY KEY NOT NULL,
  `nome` TEXT,
  `especialidade` TEXT,
  `contato` TEXT
);

CREATE TABLE `Enfermeiro` (
  `id_enfermeiro` INTEGER PRIMARY KEY NOT NULL,
  `nome` TEXT,
  `contato` TEXT
);

CREATE TABLE `Consulta` (
  `id_consulta` INTEGER PRIMARY KEY NOT NULL,
  `id_paciente` INTEGER,
  `id_medico` INTEGER,
  `data_consulta` TEXT,
  `status` TEXT
);

CREATE TABLE `Tratamento` (
  `id_tratamento` INTEGER PRIMARY KEY NOT NULL,
  `id_paciente` INTEGER,
  `descricao` TEXT,
  `data_tratamento` TEXT
);

CREATE TABLE `Prescricao` (
  `id_prescricao` INTEGER PRIMARY KEY NOT NULL,
  `id_paciente` INTEGER,
  `id_medico` INTEGER,
  `nome_medicamento` TEXT,
  `data_prescricao` TEXT
);

CREATE TABLE `Log_Acesso` (
  `id_log` INTEGER PRIMARY KEY NOT NULL,
  `id_user` INTEGER,
  `acao_executada` TEXT,
  `data` DATETIME,
  `status` TEXT
);

ALTER TABLE `Consulta` ADD FOREIGN KEY (`id_paciente`) REFERENCES `Paciente` (`id_paciente`);

ALTER TABLE `Consulta` ADD FOREIGN KEY (`id_medico`) REFERENCES `Medico` (`id_medico`);

ALTER TABLE `Tratamento` ADD FOREIGN KEY (`id_paciente`) REFERENCES `Paciente` (`id_paciente`);

ALTER TABLE `Prescricao` ADD FOREIGN KEY (`id_paciente`) REFERENCES `Paciente` (`id_paciente`);

ALTER TABLE `Prescricao` ADD FOREIGN KEY (`id_medico`) REFERENCES `Medico` (`id_medico`);

ALTER TABLE `Log_Acesso` ADD FOREIGN KEY (`id_user`) REFERENCES `Users` (`id_user`);

CREATE DATABASE if not exists mydb;

CREATE TABLE IF NOT EXISTS `mydb`.`Coordenadores` (
  `idCoordenadores` INT NOT NULL,
  `nome` VARCHAR(100) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`idCoordenadores`));


CREATE TABLE IF NOT EXISTS `mydb`.`Cursos` (
  `idCursos` INT NOT NULL,
  `nome` VARCHAR(45) NOT NULL,
  `codigo` VARCHAR(10) NOT NULL,
  `Coordenadores_idCoordenadores` INT NOT NULL,
  PRIMARY KEY (`idCursos`),
  INDEX `fk_Cursos_Coordenadores_idx` (`Coordenadores_idCoordenadores` ASC) VISIBLE,
  CONSTRAINT `fk_Cursos_Coordenadores`
    FOREIGN KEY (`Coordenadores_idCoordenadores`)
    REFERENCES `mydb`.`Coordenadores` (`idCoordenadores`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


CREATE TABLE IF NOT EXISTS `mydb`.`Aluno` (
  `nome` VARCHAR(100) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `matricula` INT NOT NULL,
  `Cursos_idCursos` INT NOT NULL,
  INDEX `fk_Aluno_Cursos1_idx` (`Cursos_idCursos` ASC) VISIBLE,
  PRIMARY KEY (`matricula`),
  CONSTRAINT `fk_Aluno_Cursos1`
    FOREIGN KEY (`Cursos_idCursos`)
    REFERENCES `mydb`.`Cursos` (`idCursos`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

CREATE TABLE IF NOT EXISTS `mydb`.`Disciplina` (
  `idDisciplina` INT NOT NULL,
  `nome` VARCHAR(100) NOT NULL,
  `codigo` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`idDisciplina`));

CREATE TABLE IF NOT EXISTS `mydb`.`Competencias` (
  `idCompetencias` INT NOT NULL,
  `Descrição` VARCHAR(600) NOT NULL,
  `op1` VARCHAR(600) NOT NULL,
  `op2` VARCHAR(600) NOT NULL,
  `op3` VARCHAR(600) NOT NULL,
  `op4` VARCHAR(600) NOT NULL,
  `op5` VARCHAR(600) NOT NULL,
  PRIMARY KEY (`idCompetencias`));

CREATE TABLE IF NOT EXISTS `mydb`.`Professores` (
  `idProfessores` INT NOT NULL,
  `nome` VARCHAR(100) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`idProfessores`));

CREATE TABLE IF NOT EXISTS `mydb`.`Atividade` (
  `idAtividade` INT NOT NULL,
  `titulo` VARCHAR(100) NOT NULL,
  `data` DATE NOT NULL,
  PRIMARY KEY (`idAtividade`));

CREATE TABLE IF NOT EXISTS `mydb`.`Turma` (
  `idTurma` INT NOT NULL,
  `semestre` INT NOT NULL,
  `Professores_idProfessores` INT NOT NULL,
  `Disciplina_idDisciplina` INT NOT NULL,
  PRIMARY KEY (`idTurma`),
  INDEX `fk_Turma_Professores1_idx` (`Professores_idProfessores` ASC) VISIBLE,
  INDEX `fk_Turma_Disciplina1_idx` (`Disciplina_idDisciplina` ASC) VISIBLE,
  CONSTRAINT `fk_Turma_Professores1`
    FOREIGN KEY (`Professores_idProfessores`)
    REFERENCES `mydb`.`Professores` (`idProfessores`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Turma_Disciplina1`
    FOREIGN KEY (`Disciplina_idDisciplina`)
    REFERENCES `mydb`.`Disciplina` (`idDisciplina`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

CREATE TABLE IF NOT EXISTS `mydb`.`Nota` (
  `idNota` INT NOT NULL,
  `nota` INT NOT NULL,
  `data` DATE NOT NULL,
  `Atividade_idAtividade` INT NOT NULL,
  `Competencias_idCompetencias` INT NOT NULL,
  `Professores_idProfessores` INT NOT NULL,
  `Aluno_matricula` INT NOT NULL,
  PRIMARY KEY (`idNota`),
  INDEX `fk_Nota_Atividade1_idx` (`Atividade_idAtividade` ASC) VISIBLE,
  INDEX `fk_Nota_Competencias1_idx` (`Competencias_idCompetencias` ASC) VISIBLE,
  INDEX `fk_Nota_Professores1_idx` (`Professores_idProfessores` ASC) VISIBLE,
  INDEX `fk_Nota_Aluno1_idx` (`Aluno_matricula` ASC) VISIBLE,
  CONSTRAINT `fk_Nota_Atividade1`
    FOREIGN KEY (`Atividade_idAtividade`)
    REFERENCES `mydb`.`Atividade` (`idAtividade`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Nota_Competencias1`
    FOREIGN KEY (`Competencias_idCompetencias`)
    REFERENCES `mydb`.`Competencias` (`idCompetencias`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Nota_Professores1`
    FOREIGN KEY (`Professores_idProfessores`)
    REFERENCES `mydb`.`Professores` (`idProfessores`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Nota_Aluno1`
    FOREIGN KEY (`Aluno_matricula`)
    REFERENCES `mydb`.`Aluno` (`matricula`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

CREATE TABLE IF NOT EXISTS `mydb`.`Turma_Aluno` (
  `Turma_idTurma` INT NOT NULL,
  `Disciplina_idDisciplina` INT NOT NULL,
  `semestre` INT NOT NULL,
  `Aluno_matricula` INT NOT NULL,
  PRIMARY KEY (`Turma_idTurma`, `Disciplina_idDisciplina`),
  INDEX `fk_Turma_has_Disciplina_Disciplina1_idx` (`Disciplina_idDisciplina` ASC) VISIBLE,
  INDEX `fk_Turma_has_Disciplina_Turma1_idx` (`Turma_idTurma` ASC) VISIBLE,
  INDEX `fk_Turma_Aluno_Aluno1_idx` (`Aluno_matricula` ASC) VISIBLE,
  CONSTRAINT `fk_Turma_has_Disciplina_Turma1`
    FOREIGN KEY (`Turma_idTurma`)
    REFERENCES `mydb`.`Turma` (`idTurma`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Turma_has_Disciplina_Disciplina1`
    FOREIGN KEY (`Disciplina_idDisciplina`)
    REFERENCES `mydb`.`Disciplina` (`idDisciplina`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Turma_Aluno_Aluno1`
    FOREIGN KEY (`Aluno_matricula`)
    REFERENCES `mydb`.`Aluno` (`matricula`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
    
    -- Coordenadores
INSERT INTO `mydb`.`Coordenadores` (`idCoordenadores`, `nome`, `email`) VALUES 
(1, 'João Silva', 'joao.silva@email.com'),
(2, 'Maria Oliveira', 'maria.oliveira@email.com'),
(3, 'Pedro Santos', 'pedro.santos@email.com'),
(4, 'Ana Costa', 'ana.costa@email.com');

-- Cursos
INSERT INTO `mydb`.`Cursos` (`idCursos`, `nome`, `codigo`, `Coordenadores_idCoordenadores`) VALUES 
(1, 'Engenharia de Software', 'ES101', 1),
(2, 'Administração', 'ADM202', 2),
(3, 'Medicina', 'MED303', 3),
(4, 'Direito', 'DIR404', 4);

-- Aluno
INSERT INTO `mydb`.`Aluno` (`nome`, `email`, `matricula`, `Cursos_idCursos`) VALUES 
('Carlos Oliveira', 'carlos.oliveira@email.com', 1001, 1),
('Fernanda Santos', 'fernanda.santos@email.com', 1002, 2),
('Luiza Pereira', 'luiza.pereira@email.com', 1003, 3),
('Rafaela Martins', 'rafaela.martins@email.com', 1004, 4);

-- Disciplina
INSERT INTO `mydb`.`Disciplina` (`idDisciplina`, `nome`, `codigo`) VALUES 
(1, 'Programação Avançada', 'PA101'),
(2, 'Gestão Financeira', 'GF202'),
(3, 'Anatomia Humana', 'AH303'),
(4, 'Direito Civil', 'DC404');

-- Competencias
INSERT INTO `mydb`.`Competencias` (`idCompetencias`, `Descrição`, `op1`, `op2`, `op3`, `op4`, `op5`) VALUES 
(1, 'Competência 1', 'Opção 1', 'Opção 2', 'Opção 3', 'Opção 4', 'Opção 5'),
(2, 'Competência 2', 'Opção 1', 'Opção 2', 'Opção 3', 'Opção 4', 'Opção 5'),
(3, 'Competência 3', 'Opção 1', 'Opção 2', 'Opção 3', 'Opção 4', 'Opção 5'),
(4, 'Competência 4', 'Opção 1', 'Opção 2', 'Opção 3', 'Opção 4', 'Opção 5');

-- Professores
INSERT INTO `mydb`.`Professores` (`idProfessores`, `nome`, `email`) VALUES 
(1, 'Fernando Lima', 'fernando.lima@email.com'),
(2, 'Mariana Souza', 'mariana.souza@email.com'),
(3, 'Roberto Almeida', 'roberto.almeida@email.com'),
(4, 'Camila Santos', 'camila.santos@email.com');

-- Atividade
INSERT INTO `mydb`.`Atividade` (`idAtividade`, `titulo`, `data`) VALUES 
(1, 'Atividade 1', '2024-05-01'),
(2, 'Atividade 2', '2024-05-02'),
(3, 'Atividade 3', '2024-05-03'),
(4, 'Atividade 4', '2024-05-04');

-- Turma
INSERT INTO `mydb`.`Turma` (`idTurma`, `semestre`, `Professores_idProfessores`, `Disciplina_idDisciplina`) VALUES 
(1, 1, 1, 1),
(2, 2, 2, 2),
(3, 3, 3, 3),
(4, 4, 4, 4);

-- Nota
INSERT INTO `mydb`.`Nota` (`idNota`, `nota`, `data`, `Atividade_idAtividade`, `Competencias_idCompetencias`, `Professores_idProfessores`, `Aluno_matricula`) VALUES 
(1, 8, '2024-05-01', 1, 1, 1, 1001),
(2, 7, '2024-05-02', 2, 2, 2, 1002),
(3, 9, '2024-05-03', 3, 3, 3, 1003),
(4, 10, '2024-05-04', 4, 4, 4, 1004);

-- Turma_Aluno
INSERT INTO `mydb`.`Turma_Aluno` (`Turma_idTurma`, `Disciplina_idDisciplina`, `semestre`, `Aluno_matricula`) VALUES 
(1, 1, 1, 1001),
(2, 2, 2, 1002),
(3, 3, 3, 1003),
(4, 4, 4, 1004);

SELECT * FROM `mydb`.`Nota`;
-- Clientes
CREATE TABLE Cliente (
    cliente_id INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    tipo CHAR(2) CHECK (tipo IN ('PF','PJ'))
);

-- Veículos
CREATE TABLE Veiculo (
    veiculo_id INT PRIMARY KEY,
    cliente_id INT NOT NULL,
    modelo VARCHAR(100) NOT NULL,
    ano INT,
    FOREIGN KEY (cliente_id) REFERENCES Cliente(cliente_id)
);

-- Mecânicos
CREATE TABLE Mecanico (
    mecanico_id INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    especialidade VARCHAR(50)
);

-- Equipes
CREATE TABLE Equipe (
    equipe_id INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

-- Equipe-Mecânico (associação N:N)
CREATE TABLE EquipeMecanico (
    equipe_id INT NOT NULL,
    mecanico_id INT NOT NULL,
    PRIMARY KEY (equipe_id, mecanico_id),
    FOREIGN KEY (equipe_id) REFERENCES Equipe(equipe_id),
    FOREIGN KEY (mecanico_id) REFERENCES Mecanico(mecanico_id)
);

-- Peças
CREATE TABLE Peca (
    peca_id INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10,2) NOT NULL
);

-- Ordens de Serviço
CREATE TABLE OrdemServico (
    ordem_id INT PRIMARY KEY,
    veiculo_id INT NOT NULL,
    mecanico_id INT NOT NULL,
    data_ordem DATE NOT NULL,
    descricao VARCHAR(255),
    FOREIGN KEY (veiculo_id) REFERENCES Veiculo(veiculo_id),
    FOREIGN KEY (mecanico_id) REFERENCES Mecanico(mecanico_id)
);

-- Itens da Ordem (peças usadas)
CREATE TABLE ItemOrdem (
    item_id INT PRIMARY KEY,
    ordem_id INT NOT NULL,
    peca_id INT NOT NULL,
    quantidade INT NOT NULL,
    FOREIGN KEY (ordem_id) REFERENCES OrdemServico(ordem_id),
    FOREIGN KEY (peca_id) REFERENCES Peca(peca_id)
);

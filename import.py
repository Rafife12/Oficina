import zipfile
from google.colab import files

# Caminho para salvar o ZIP
zip_path = '/content/Projeto-BD-Oficina.zip'

# Conteúdos dos arquivos
readme_content = """# Projeto Lógico de Banco de Dados – Oficina Mecânica

## Descrição do Projeto
Este projeto representa o modelo lógico de um sistema de oficina mecânica, contemplando clientes, veículos, mecânicos, equipes, ordens de serviço, serviços e peças.

## Pontos Importantes do Modelo
- Cada cliente pode ter vários veículos.
- Cada ordem de serviço possui data, veículo, mecânico responsável e serviços realizados.
- Equipes podem ser formadas por vários mecânicos.
- Algumas peças podem ser usadas em múltiplos serviços.
- Relacionamentos EER foram mapeados para tabelas relacionais com chaves primárias, estrangeiras e constraints de integridade.

## Estrutura de Scripts
- `criar_tabelas.sql` → Criação das tabelas com chaves primárias, estrangeiras e constraints.
- `inserir_dados.sql` → Popular o banco de dados com dados de teste.
- `queries.sql` → Consultas SQL demonstrando SELECT, WHERE, HAVING, ORDER BY, JOINs e atributos derivados.
"""

criar_tabelas_sql = """-- Clientes
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
"""

inserir_dados_sql = """-- Clientes
INSERT INTO Cliente VALUES (1, 'João Silva', 'PF');
INSERT INTO Cliente VALUES (2, 'Oficina XYZ', 'PJ');

-- Veículos
INSERT INTO Veiculo VALUES (1, 1, 'Fiat Uno', 2010);
INSERT INTO Veiculo VALUES (2, 1, 'Honda Civic', 2018);

-- Mecânicos
INSERT INTO Mecanico VALUES (1, 'Carlos', 'Motor');
INSERT INTO Mecanico VALUES (2, 'Ana', 'Elétrica');

-- Equipes
INSERT INTO Equipe VALUES (1, 'Equipe A');
INSERT INTO Equipe VALUES (2, 'Equipe B');

-- Associação Equipe-Mecânico
INSERT INTO EquipeMecanico VALUES (1, 1);
INSERT INTO EquipeMecanico VALUES (2, 2);

-- Peças
INSERT INTO Peca VALUES (1, 'Filtro de Óleo', 50.00);
INSERT INTO Peca VALUES (2, 'Pastilha de Freio', 120.00);

-- Ordens de Serviço
INSERT INTO OrdemServico VALUES (1, 1, 1, '2025-08-22', 'Troca de óleo e revisão geral');

-- Itens da Ordem
INSERT INTO ItemOrdem VALUES (1, 1, 1, 1);
INSERT INTO ItemOrdem VALUES (2, 1, 2, 2);
"""

queries_sql = """-- a) Recuperação simples
SELECT * FROM Cliente;

-- b) Filtros com WHERE
SELECT nome, tipo
FROM Cliente
WHERE tipo = 'PF';

-- c) Atributos derivados
SELECT v.modelo, v.ano, CONCAT(v.modelo, ' - ', v.ano) AS descricao_veiculo
FROM Veiculo v;

-- d) Ordenação
SELECT o.ordem_id, o.data_ordem, c.nome AS cliente
FROM OrdemServico o
JOIN Veiculo v ON o.veiculo_id = v.veiculo_id
JOIN Cliente c ON v.cliente_id = c.cliente_id
ORDER BY o.data_ordem DESC;

-- e) Filtros em grupos – HAVING
SELECT v.cliente_id, COUNT(o.ordem_id) AS total_ordens
FROM OrdemServico o
JOIN Veiculo v ON o.veiculo_id = v.veiculo_id
GROUP BY v.cliente_id
HAVING COUNT(o.ordem_id) > 0;

-- f) JOINs complexos
SELECT o.ordem_id, c.nome AS cliente, m.nome AS mecanico, p.nome AS peca, io.quantidade
FROM OrdemServico o
JOIN Veiculo v ON o.veiculo_id = v.veiculo_id
JOIN Cliente c ON v.cliente_id = c.cliente_id
JOIN Mecanico m ON o.mecanico_id = m.mecanico_id
JOIN ItemOrdem io ON o.ordem_id = io.ordem_id
JOIN Peca p ON io.peca_id = p.peca_id;
"""

# Criar o ZIP
with zipfile.ZipFile(zip_path, 'w') as zipf:
    zipf.writestr('Projeto-BD-Oficina/README.md', readme_content)
    zipf.writestr('Projeto-BD-Oficina/scripts/criar_tabelas.sql', criar_tabelas_sql)
    zipf.writestr('Projeto-BD-Oficina/scripts/inserir_dados.sql', inserir_dados_sql)
    zipf.writestr('Projeto-BD-Oficina/scripts/queries.sql', queries_sql)

# Baixar o arquivo
files.download(zip_path)

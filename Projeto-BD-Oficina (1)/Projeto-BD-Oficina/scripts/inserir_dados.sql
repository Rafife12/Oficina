-- Clientes
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

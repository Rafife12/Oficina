-- a) Recuperação simples
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

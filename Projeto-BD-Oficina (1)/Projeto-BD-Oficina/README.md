# Projeto Lógico de Banco de Dados – Oficina Mecânica

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

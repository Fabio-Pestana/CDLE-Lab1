# CDLE — Lab 1: TPC-DS numa Única Máquina

Trabalho realizado no âmbito da unidade curricular **Computação de Dados em Larga Escala (CDLE)**
do Mestrado em Engenharia Informática e de Computadores / Engenharia Informática e Multimédia
do ISEL.

**Autores:** Miguel Alcobia (50746) · Fábio Pestana (50756)
**Docente:** Professor António Teófilo
**Ano letivo:** 2025/2026

O objetivo do lab é correr o pipeline completo do TPC-DS numa só máquina:
gerar os dados → converter para Parquet → explorar → gerar as queries → correr e medir.

---

## Máquina de teste

| Item | Valor |
|---|---|
| Modelo do computador | ASUS TUF Dash F15 FX517ZE |
| CPU e número de cores | Intel Core i7-12650H (10 cores) |
| RAM | 16 GB DDR5 |
| Disco (tipo e espaço livre) | SSD NVMe 512 GB (65 GB livres) |
| Sistema operativo | Windows 11 x64 / Ubuntu 26.04.1 LTS (WSL 2) |
| Versão do DuckDB | 1.5.5 |

---

## Estrutura do repositório

```
.
├── starter/            scripts do starter pack + exemplos SQL próprios
│   └── examples/       queries curtas para explorar os dados (01..09)
├── query_templates/    cópia corrigida dos templates do TPC-DS
├── results/            medições SF1 (ficheiros CSV)
├── results10/          medições SF10 (ficheiros CSV)
├── extras_01/          exercícios extra e trabalho exploratório
└── .gitignore
```

> O kit TPC-DS (`DSGen-software-code-4.0.0/`), os dados gerados (`data/`), os
> ficheiros Parquet (`parquet/`) e as queries geradas **não** estão no repositório.
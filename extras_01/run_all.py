import os
import subprocess
import sys

# Variáveis do teu ambiente (ajusta os caminhos se necessário)
python_bin = sys.executable  # Usa o Python do venv ativo
t_dir = os.environ.get("T", ".")  # Usa a variável de ambiente $T se existir, ou o diretório atual

starter_script = os.path.join(t_dir, "starter", "show_query.py")
parquet_dir = os.path.join(t_dir, "parquet", "sf10")
sql_dir = os.path.join(t_dir, "starter", "examples")
results_dir = os.path.join(t_dir, "results10")

# Lista de ficheiros SQL a processar
sql_files = [
    "01_list_tables.sql",
    "02_small_table.sql",
    "03_describe_table.sql",
    "04_row_counts.sql",
    "05_sample_fact_rows.sql",
    "06_keys_to_dates.sql",
    "07_simple_join.sql",
    "08_nulls.sql",
]

# Criar a pasta de resultados se não existir
os.makedirs(results_dir, exist_ok=True)

# Processar cada ficheiro SQL
for sql_file in sql_files:
    # Define o nome do ficheiro CSV de saída (ex: 01_list_tables.csv)
    base_name = os.path.splitext(sql_file)[0]
    out_csv = os.path.join(results_dir, f"{base_name}.csv")
    sql_path = os.path.join(sql_dir, sql_file)

    cmd = [
        python_bin,
        starter_script,
        "--parquet",
        parquet_dir,
        "--out",
        out_csv,
        sql_path,
    ]

    print(f"[running] A executar {sql_file} ...")

    result = subprocess.run(cmd)

    if result.returncode == 0:
        print(f"  [pass] Guardado em {out_csv}\n")
    else:
        print(f"  [error] Erro ao executar {sql_file}\n")
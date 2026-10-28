from pathlib import Path
import pandas as pd


def carregar_dados(caminho_arquivo: Path) -> pd.DataFrame:
    """Carrega e valida os dados de operação logística."""
    if not caminho_arquivo.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho_arquivo}")

    df = pd.read_csv(caminho_arquivo)

    # Validações de consistência
    if (df["horas"] <= 0).any():
        raise ValueError("As horas trabalhadas devem ser maiores que zero.")

    if (df[["pacotes", "atrasos"]] < 0).any().any():
        raise ValueError("Pacotes e atrasos não podem ser negativos.")

    return df


def calcular_indicadores(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Calcula indicadores de produtividade e qualidade por funcionário e turno."""
    # Métricas individuais por registro
    df["pacotes_por_hora"] = df["pacotes"] / df["horas"]
    df["taxa_atraso"] = (df["atrasos"] / df["pacotes"]) * 100

    # 1. Produtividade consolidada por funcionário
    prod_funcionario = (
        df.groupby("funcionario")
        .agg(
            pacotes=("pacotes", "sum"),
            horas=("horas", "sum"),
            atrasos=("atrasos", "sum"),
        )
    )
    prod_funcionario["pacotes_por_hora"] = (
        prod_funcionario["pacotes"] / prod_funcionario["horas"]
    )
    prod_funcionario["taxa_atraso_pct"] = (
        prod_funcionario["atrasos"] / prod_funcionario["pacotes"] * 100
    )

    # 2. Produtividade consolidada por turno
    prod_turno = (
        df.groupby("turno")
        .agg(
            pacotes=("pacotes", "sum"),
            horas=("horas", "sum"),
            atrasos=("atrasos", "sum"),
        )
    )
    prod_turno["pacotes_por_hora"] = prod_turno["pacotes"] / prod_turno["horas"]
    prod_turno["taxa_atraso_pct"] = (
        prod_turno["atrasos"] / prod_turno["pacotes"] * 100
    )

    return prod_funcionario, prod_turno


def main():
    BASE_DIR = Path(__file__).resolve().parent.parent
    caminho_dados = BASE_DIR / "dados" / "operacao.csv"

    print("Carregando dados da operação...")
    df = carregar_dados(caminho_dados)

    prod_funcionario, prod_turno = calcular_indicadores(df)

    print("\n=== PRODUTIVIDADE POR FUNCIONÁRIO ===")
    print(prod_funcionario.round(2))

    print("\n=== PRODUTIVIDADE POR TURNO ===")
    print(prod_turno.round(2))

    # Salvar relatório consolidado
    saida = BASE_DIR / "dados" / "relatorio_produtividade.csv"
    prod_funcionario.round(2).to_csv(saida)
    print(f"\nRelatório salvo com sucesso em: {saida}")


if __name__ == "__main__":
    main()

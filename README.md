# 📦 Analisador de Produtividade Logística com Python

Sistema em Python focado em operações logísticas (recebimento, separação/picking e expedição), projetado para transformar dados brutos de turnos e funcionários em métricas de produtividade, identificando gargalos operacionais e oportunidades de otimização.

---

## 🎯 Problema de Negócio

Em centros de distribuição e operações de e-commerce, o volume de pacotes processados varia constantemente. Avaliar apenas o volume absoluto esconde ineficiências:
- Um colaborador pode processar muitos pacotes, mas com alta taxa de avarias ou atrasos.
- Diferentes turnos enfrentam gargalos distintos.
- É necessário correlacionar **velocidade** (pacotes/hora) e **qualidade** (taxa de atraso).

Este projeto resolve essa dor fornecendo uma análise estruturada, padronizada e automatizada.

---

## 📁 Estrutura do Projeto

```text
analisador-logistico/
├── dados/
│   ├── operacao.csv                  # Base de dados operacional
│   └── relatorio_produtividade.csv   # Relatório gerado automaticamente
├── src/
│   └── analise.py                    # Script de validação e cálculo dos indicadores
├── requirements.txt                  # Dependências do projeto
└── README.md                         # Documentação e guia de execução
```

---

## 📊 Indicadores Calculados

1. **Pacotes por Hora (Produtividade):**
   $$\text{Pacotes por Hora} = \frac{\sum \text{Pacotes Processados}}{\sum \text{Horas Trabalhadas}}$$

2. **Taxa de Atraso (Qualidade/Gargalo):**
   $$\text{Taxa de Atraso (\%)} = \left(\frac{\sum \text{Atrasos}}{\sum \text{Pacotes Processados}}\right) \times 100$$

3. **Visão por Turno e Funcionário:**
   Agrupamentos que destacam variações de desempenho entre períodos (Manhã vs. Tarde) e perfis operacionais.

---

## 🚀 Como Executar Localmente

### 1. Pré-requisitos
- Python 3.10 ou superior instalado.

### 2. Configurar o Ambiente Virtual

```bash
# Entre na pasta do projeto
cd analisador-logistico

# Crie o ambiente virtual
python3 -m venv .venv

# Ative o ambiente virtual
# No Linux/macOS:
source .venv/bin/activate
# No Windows:
# .venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt
```

### 3. Executar a Análise

```bash
python src/analise.py
```

O script irá validar os dados, exibir no terminal as tabelas de resumo por funcionário e por turno, e salvar o arquivo `dados/relatorio_produtividade.csv`.

---

## 🗺️ Roadmap de Evolução

- [x] **Etapa 1 — Fundamentos & Script Base:** Validação de dados, tratamento de regras de negócio e cálculo dos indicadores em Pandas.
- [ ] **Etapa 2 — Análise Exploratória Aprofundada:** Detecção automática de anomalias (outliers), médias móveis e testes de consistência.
- [ ] **Etapa 3 — Dashboard Interativo com Streamlit:** Visualização gráfica com filtros por data, turno e ranking de desempenho.
- [ ] **Etapa 4 — Diferencial de IA & Automação:** Geração de diagnósticos automáticos em linguagem natural e sugestões de alocação de equipe.

---

## 🛠️ Tecnologias

- **Python 3**
- **Pandas** (Tratamento e agregação de dados)
- **Pathlib** (Manipulação portável de caminhos de arquivos)

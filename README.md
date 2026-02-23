# 📘 Boletim de Alunos — Console (Python)

Aplicativo de console para **gerenciamento de boletins escolares**, permitindo cadastrar, visualizar, excluir (desativar) e exportar boletins para arquivo JSON.  
Projeto criado para estudo de **lógica**, **estruturas de dados** (dicionários) e **fluxo de controle** em Python 3.

> ⚠️ Observação: Este projeto é didático. A funcionalidade *importar boletins* ainda não foi implementada.

---

## ✨ Funcionalidades Implementadas

### ✅ 1) Cadastrar boletim
- Gera **ID automaticamente**  
- Calcula aprovação (`nota > 6.0`)  
- Define matrícula como **ativa**  
- Armazena tudo em um **dicionário central**

### ✅ 2) Visualizar todos os boletins
- Lista apenas alunos com **matrícula ativa**  
- Exibe boletins com **formatação organizada**  
- Caso não existam boletins → exibe mensagem adequada

### ✅ 3) Visualizar boletim individual
- Busca pelo **ID**  
- Mostra **situação** (aprovado/reprovado) e **status** (ativo/inativo)  
- Saída **limpa e legível**

### ✅ 4) Excluir boletim
- **Não remove** do sistema  
- Apenas marca como **matrícula inativa**  
- Mantém **histórico** sem perda de dados

### ⛔ 5) Importar boletins *(ainda não implementado)*
Ao selecionar, o sistema exibe:
```
• Funcionalidade ainda não implementada nessa versão •
```

### ✅ 6) Exportar boletins
Gera um arquivo `.json` contendo **todos os boletins** (ativos e inativos):

- Nome do arquivo **definido pelo usuário**  
- Arquivo salvo com **indentação** e **UTF-8**

> Exemplo: `boletins.json`

---

## 📦 Tecnologias Utilizadas
- **Python 3.10+** (usa `match`/`case`)
- Módulo padrão **`json`** para exportação

---

## 🔧 Pré-requisitos

Verifique a versão do Python:
```bash
python --version
```

Execute o programa
```bash
python main.py
```

## 🗂️ Organização dos Dados (em memória)

Os boletins são armazenados em um dicionário mapeado por **ID**:

```python
dict_boletim_alunos = {
    1: {
        "id": 1,
        "nome": "Carlos",
        "idade": 16,
        "nota": 8.5,
        "is_aprovado": True,
        "is_ativo": True
    }
}
```

## 📤 Exemplo de Arquivo JSON Gerado

```json
{
    "1": {
        "id": 1,
        "nome": "Carlos",
        "idade": 16,
        "nota": 8.5,
        "is_aprovado": true,
        "is_ativo": true
    }
}
```
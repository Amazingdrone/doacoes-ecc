import streamlit as st
import pandas as pd
import os
import io
from fpdf import FPDF

# ==========================================
# 1. CONFIGURAÇÃO DA PÁGINA
# ==========================================
st.set_page_config(page_title="Doações ECC", layout="centered")

ARQUIVO_DADOS = 'banco_doacoes_v2.csv'

# ==========================================
# 2. FUNÇÃO DE EMOJIS AUTOMÁTICOS
# ==========================================
def obter_emoji(item_nome):
    nome = item_nome.lower()
    if "arroz" in nome: return "🍚"
    if "frango" in nome: return "🍗"
    if "carne" in nome: return "🥩"
    if "macarrão" in nome: return "🍝"
    if "batata" in nome: return "🥔"
    if "tomate" in nome: return "🍅"
    if "alface" in nome: return "🥬"
    if "cenoura" in nome: return "🥕"
    if "vagem" in nome or "ervilha" in nome: return "🫛"
    if "champion" in nome or "cogumelo" in nome: return "🍄"
    if "ketchup" in nome or "mostarda" in nome or "massa" in nome or "creme de leite" in nome or "leite moça" in nome: return "🥫"
    if "shoyo" in nome or "vinagre" in nome or "óleo" in nome: return "🫙"
    if "suco" in nome: return "🧃"
    if "limão" in nome: return "🍋"
    if "copo" in nome or "copinho" in nome: return "🥤"
    if "milho" in nome: return "🌽"
    if "maionese" in nome or "requeijão" in nome or "margarina" in nome: return "🧈"
    if "coco" in nome: return "🥥"
    if "leite" in nome: return "🥛"
    if "pudim" in nome: return "🍮"
    if "chantily" in nome: return "🧁"
    if "açúcar" in nome or "sal " in nome or "sal" == nome.strip() or "pimenta" in nome: return "🧂"
    if "coca" in nome or "guaraná" in nome or "fanta" in nome or "refrigerante" in nome: return "🥤"
    if "água" in nome: return "💧"
    if "morango" in nome: return "🍓"
    if "uva" in nome: return "🍇"
    if "mamão" in nome: return "🍈"
    if "ovo" in nome: return "🥚"
    if "queijo" in nome: return "🧀"
    if "presunto" in nome or "salame" in nome or "mortadela" in nome: return "🥓"
    if "café" in nome: return "☕"
    if "bolacha" in nome or "biscoito" in nome: return "🍪"
    if "chá" in nome: return "🍵"
    if "maçã" in nome: return "🍎"
    if "abacaxi" in nome: return "🍍"
    if "cravo" in nome or "canela" in nome: return "🍂"
    if "cebola" in nome: return "🧅"
    if "alho" in nome: return "🧄"
    if "orégano" in nome or "cheiro verde" in nome or "salsão" in nome or "poró" in nome: return "🌿"
    if "pimentão" in nome: return "🫑"
    return "📦" # Emoji padrão se não encontrar a palavra

# ==========================================
# 3. INICIALIZAÇÃO DO BANCO DE DADOS (CSV)
# ==========================================
def carregar_dados():
    if os.path.exists(ARQUIVO_DADOS):
        return pd.read_csv(ARQUIVO_DADOS)
    
    # Nova estrutura com Qtd Total, Faltante e Unidades!
    dados_iniciais = [
        # Almoço Sábado
        {"Categoria": "Almoço Sáb", "Item": "Arroz branco", "Qtd_Total": 13.0, "Unidade": "kg", "Qtd_Faltante": 0.0, "Status": "Doado", "Doadores": "Têre (Betel) (8kg), Cristina (Maranata) (5kg)"},
        {"Categoria": "Almoço Sáb", "Item": "Peito de Frango s/osso", "Qtd_Total": 65.0, "Unidade": "kg", "Qtd_Faltante": 65.0, "Status": "Pendente", "Doadores": ""},
        {"Categoria": "Almoço Sáb", "Item": "Batata palha", "Qtd_Total": 18.0, "Unidade": "kg", "Qtd_Faltante": 18.0, "Status": "Pendente", "Doadores": ""},
        {"Categoria": "Almoço Sáb", "Item": "Creme de leite", "Qtd_Total": 2.0, "Unidade": "cx c/ 20", "Qtd_Faltante": 0.0, "Status": "Doado", "Doadores": "Neemias (2cx)"},
        {"Categoria": "Almoço Sáb", "Item": "Champion", "Qtd_Total": 1.0, "Unidade": "Balde", "Qtd_Faltante": 1.0, "Status": "Pendente", "Doadores": ""},
        {"Categoria": "Almoço Sáb", "Item": "Ketchup", "Qtd_Total": 1.0, "Unidade": "litro", "Qtd_Faltante": 0.0, "Status": "Doado", "Doadores": "Onória (Betel) (1L)"},
        {"Categoria": "Almoço Sáb", "Item": "Mostarda", "Qtd_Total": 1.0, "Unidade": "litro", "Qtd_Faltante": 0.0, "Status": "Doado", "Doadores": "Onória (Betel) (1L)"},
        {"Categoria": "Almoço Sáb", "Item": "Shoyo", "Qtd_Total": 1.0, "Unidade": "litro", "Qtd_Faltante": 1.0, "Status": "Pendente", "Doadores": ""},
        {"Categoria": "Almoço Sáb", "Item": "Tomate", "Qtd_Total": 10.0, "Unidade": "kg", "Qtd_Faltante": 0.0, "Status": "Doado", "Doadores": "André Aranha (10kg)"},
        {"Categoria": "Almoço Sáb", "Item": "Alface", "Qtd_Total": 15.0, "Unidade": "maços", "Qtd_Faltante": 15.0, "Status": "Pendente", "Doadores": ""},
        {"Categoria": "Almoço Sáb", "Item": "Cenoura", "Qtd_Total": 6.0, "Unidade": "kg", "Qtd_Faltante": 6.0, "Status": "Pendente", "Doadores": ""},
        {"Categoria": "Almoço Sáb", "Item": "Vagem", "Qtd_Total": 3.0, "Unidade": "kg", "Qtd_Faltante": 3.0, "Status": "Pendente", "Doadores": ""},
        {"Categoria": "Almoço Sáb", "Item": "Massa de tomate", "Qtd_Total": 6.0, "Unidade": "kg", "Qtd_Faltante": 6.0, "Status": "Pendente", "Doadores": ""},
        # Sobremesa Sábado
        {"Categoria": "Sobremesa Sáb", "Item": "Suco maracujá conc.", "Qtd_Total": 10.0, "Unidade": "garrafas", "Qtd_Faltante": 10.0, "Status": "Pendente", "Doadores": ""},
        {"Categoria": "Sobremesa Sáb", "Item": "Creme de leite", "Qtd_Total": 6.0, "Unidade": "cx c/20", "Qtd_Faltante": 0.0, "Status": "Doado", "Doadores": "Nize (Maranata) (1cx), Neemias (5cx)"},
        {"Categoria": "Sobremesa Sáb", "Item": "Leite moça", "Qtd_Total": 20.0, "Unidade": "cx", "Qtd_Faltante": 0.0, "Status": "Doado", "Doadores": "Marcos e Thays (20cx)"},
        {"Categoria": "Sobremesa Sáb", "Item": "Limão", "Qtd_Total": 2.0, "Unidade": "kg", "Qtd_Faltante": 0.0, "Status": "Doado", "Doadores": "Ivanice (Maranata) (2kg)"},
        {"Categoria": "Sobremesa Sáb", "Item": "Creme de leite p/ limão", "Qtd_Total": 6.0, "Unidade": "cx c/20", "Qtd_Faltante": 0.0, "Status": "Doado", "Doadores": "Diego (Ágape) (3cx), Neemias (3cx)"},
        {"Categoria": "Sobremesa Sáb", "Item": "Leite moça p/ limão", "Qtd_Total": 20.0, "Unidade": "cx", "Qtd_Faltante": 0.0, "Status": "Doado", "Doadores": "Marcos e Thays (20cx)"},
        {"Categoria": "Sobremesa Sáb", "Item": "Copinhos sobremesa c/tampa", "Qtd_Total": 400.0, "Unidade": "unid.", "Qtd_Faltante": 0.0, "Status": "Doado", "Doadores": "Indianara (Maranata) (400)"},
        # Almoço Domingo
        {"Categoria": "Almoço Dom", "Item": "Macarrão", "Qtd_Total": 10.0, "Unidade": "kg", "Qtd_Faltante": 0.0, "Status": "Doado", "Doadores": "Silvia e Onória (10kg)"},
        {"Categoria": "Almoço Dom", "Item": "Molho de tomate", "Qtd_Total": 6.0, "Unidade": "kg", "Qtd_Faltante": 0.0, "Status": "Doado", "Doadores": "Juliana Borges (6kg)"},
        {"Categoria": "Almoço Dom", "Item": "Carne moída", "Qtd_Total": 60.0, "Unidade": "kg", "Qtd_Faltante": 60.0, "Status": "Pendente", "Doadores": ""},
        {"Categoria": "Almoço Dom", "Item": "Alface", "Qtd_Total": 15.0, "Unidade": "maços", "Qtd_Faltante": 15.0, "Status": "Pendente", "Doadores": ""},
        {"Categoria": "Almoço Dom", "Item": "Tomate", "Qtd_Total": 6.0, "Unidade": "kg", "Qtd_Faltante": 0.0, "Status": "Doado", "Doadores": "Miely (6kg)"},
        {"Categoria": "Almoço Dom", "Item": "Milho verde", "Qtd_Total": 2.0, "Unidade": "kg", "Qtd_Faltante": 0.0, "Status": "Doado", "Doadores": "Miely (2kg)"},
        {"Categoria": "Almoço Dom", "Item": "Ervilha", "Qtd_Total": 1.0, "Unidade": "kg", "Qtd_Faltante": 0.0, "Status": "Doado", "Doadores": "Miely (1kg)"},
        {"Categoria": "Almoço Dom", "Item": "Maionese Hellman's", "Qtd_Total": 2.0, "Unidade": "kg", "Qtd_Faltante": 0.0, "Status": "Doado", "Doadores": "Miely (2kg)"},
        # Risoto Domingo
        {"Categoria": "Risoto Dom", "Item": "Arroz branco", "Qtd_Total": 10.0, "Unidade": "kg", "Qtd_Faltante": 0.0, "Status": "Doado", "Doadores": "Shin (Betel) (10kg)"},
        {"Categoria": "Risoto Dom", "Item": "Tomate cereja", "Qtd_Total": 2.0, "Unidade": "caixas", "Qtd_Faltante": 2.0, "Status": "Pendente", "Doadores": ""},
        {"Categoria": "Risoto Dom", "Item": "Creme de leite", "Qtd_Total": 1.0, "Unidade": "cx c/20", "Qtd_Faltante": 0.0, "Status": "Doado", "Doadores": "Marcos e Thays (1cx)"},
        {"Categoria": "Risoto Dom", "Item": "Leite de coco", "Qtd_Total": 5.0, "Unidade": "garrafas", "Qtd_Faltante": 5.0, "Status": "Pendente", "Doadores": ""},
        {"Categoria": "Risoto Dom", "Item": "Requeijão", "Qtd_Total": 4.0, "Unidade": "potes", "Qtd_Faltante": 4.0, "Status": "Pendente", "Doadores": ""},
        # Sobremesa Domingo
        {"Categoria": "Sobremesa Dom", "Item": "Leite", "Qtd_Total": 12.0, "Unidade": "Litros", "Qtd_Faltante": 6.0, "Status": "Pendente", "Doadores": "Valéria (Maranata) (6 L)"},
        {"Categoria": "Sobremesa Dom", "Item": "Pudim de baunilha", "Qtd_Total": 26.0, "Unidade": "cx", "Qtd_Faltante": 13.0, "Status": "Pendente", "Doadores": "Valéria (Maranata) (13 cx)"},
        {"Categoria": "Sobremesa Dom", "Item": "Chantily", "Qtd_Total": 2.0, "Unidade": "litros", "Qtd_Faltante": 0.0, "Status": "Doado", "Doadores": "Michele (Maranata) (2L)"},
        {"Categoria": "Sobremesa Dom", "Item": "Açúcar", "Qtd_Total": 5.0, "Unidade": "kg", "Qtd_Faltante": 0.0, "Status": "Doado", "Doadores": "Nádia (Maranata) (5kg)"},
        # Bebidas
        {"Categoria": "Bebidas", "Item": "Coca-cola normal 2L", "Qtd_Total": 12.0, "Unidade": "garrafas", "Qtd_Faltante": 6.0, "Status": "Pendente", "Doadores": "Marcos e Thays (6 un)"},
        {"Categoria": "Bebidas", "Item": "Coca-cola Zero 2L", "Qtd_Total": 12.0, "Unidade": "garrafas", "Qtd_Faltante": 6.0, "Status": "Pendente", "Doadores": "Marcos e Thays (6 un)"},
        {"Categoria": "Bebidas", "Item": "Guaraná normal 2L", "Qtd_Total": 12.0, "Unidade": "garrafas", "Qtd_Faltante": 6.0, "Status": "Pendente", "Doadores": "Luiza (Maranata) (6 un)"},
        {"Categoria": "Bebidas", "Item": "Guaraná Zero 2L", "Qtd_Total": 10.0, "Unidade": "garrafas", "Qtd_Faltante": 10.0, "Status": "Pendente", "Doadores": ""},
        {"Categoria": "Bebidas", "Item": "Fanta laranja 2L", "Qtd_Total": 12.0, "Unidade": "garrafas", "Qtd_Faltante": 12.0, "Status": "Pendente", "Doadores": ""},
        {"Categoria": "Bebidas", "Item": "Água min. c/ gás 1,5L", "Qtd_Total": 12.0, "Unidade": "garrafas", "Qtd_Faltante": 12.0, "Status": "Pendente", "Doadores": ""},
        # Café da Manhã
        {"Categoria": "Café da Manhã", "Item": "Morango", "Qtd_Total": 4.0, "Unidade": "caixas", "Qtd_Faltante": 4.0, "Status": "Pendente", "Doadores": ""},
        {"Categoria": "Café da Manhã", "Item": "Uva Italia", "Qtd_Total": 2.0, "Unidade": "caixas", "Qtd_Faltante": 2.0, "Status": "Pendente", "Doadores": ""},
        {"Categoria": "Café da Manhã", "Item": "Uva Rubi", "Qtd_Total": 2.0, "Unidade": "caixas", "Qtd_Faltante": 2.0, "Status": "Pendente", "Doadores": ""},
        {"Categoria": "Café da Manhã", "Item": "Mamão formosa", "Qtd_Total": 5.0, "Unidade": "unid.", "Qtd_Faltante": 0.0, "Status": "Doado", "Doadores": "Cliceu (Maranata) (5)"},
        {"Categoria": "Café da Manhã", "Item": "Ovos", "Qtd_Total": 20.0, "Unidade": "dúzias", "Qtd_Faltante": 20.0, "Status": "Pendente", "Doadores": ""},
        {"Categoria": "Café da Manhã", "Item": "Queijo mussarela", "Qtd_Total": 1.0, "Unidade": "kg", "Qtd_Faltante": 1.0, "Status": "Pendente", "Doadores": ""},
        {"Categoria": "Café da Manhã", "Item": "Queijo prato", "Qtd_Total": 1.0, "Unidade": "kg", "Qtd_Faltante": 1.0, "Status": "Pendente", "Doadores": ""},
        {"Categoria": "Café da Manhã", "Item": "Presunto", "Qtd_Total": 1.0, "Unidade": "kg", "Qtd_Faltante": 1.0, "Status": "Pendente", "Doadores": ""},
        {"Categoria": "Café da Manhã", "Item": "Salame", "Qtd_Total": 0.5, "Unidade": "kg", "Qtd_Faltante": 0.5, "Status": "Pendente", "Doadores": ""},
        {"Categoria": "Café da Manhã", "Item": "Mortadela", "Qtd_Total": 0.5, "Unidade": "kg", "Qtd_Faltante": 0.0, "Status": "Doado", "Doadores": "Cliceu (Maranata) (0.5kg)"},
        {"Categoria": "Café da Manhã", "Item": "Café Lontrinha", "Qtd_Total": 5.0, "Unidade": "kg", "Qtd_Faltante": 0.0, "Status": "Doado", "Doadores": "Marcos e Thays (5kg)"},
        {"Categoria": "Café da Manhã", "Item": "Suco de caixinha", "Qtd_Total": 12.0, "Unidade": "cx 1L", "Qtd_Faltante": 6.0, "Status": "Pendente", "Doadores": "Kari (Maranata) (6cx)"},
        {"Categoria": "Café da Manhã", "Item": "Leite integral", "Qtd_Total": 18.0, "Unidade": "litros", "Qtd_Faltante": 18.0, "Status": "Pendente", "Doadores": ""},
        {"Categoria": "Café da Manhã", "Item": "Leite sem lactose", "Qtd_Total": 3.0, "Unidade": "litros", "Qtd_Faltante": 0.0, "Status": "Doado", "Doadores": "Nádia (Maranata) (3L)"},
        {"Categoria": "Café da Manhã", "Item": "Açúcar", "Qtd_Total": 7.0, "Unidade": "kg", "Qtd_Faltante": 4.0, "Status": "Pendente", "Doadores": "Michele (Maranata) (3kg)"},
        {"Categoria": "Café da Manhã", "Item": "Água", "Qtd_Total": 4.0, "Unidade": "galões 5L", "Qtd_Faltante": 4.0, "Status": "Pendente", "Doadores": ""},
        {"Categoria": "Café da Manhã", "Item": "Bolacha salgada", "Qtd_Total": 5.0, "Unidade": "kg", "Qtd_Faltante": 5.0, "Status": "Pendente", "Doadores": ""},
        {"Categoria": "Café da Manhã", "Item": "Bolacha recheada", "Qtd_Total": 10.0, "Unidade": "kg", "Qtd_Faltante": 10.0, "Status": "Pendente", "Doadores": ""},
        # Chá
        {"Categoria": "Chá", "Item": "Chá mate nat. à granel", "Qtd_Total": 1.0, "Unidade": "caixa", "Qtd_Faltante": 1.0, "Status": "Pendente", "Doadores": ""},
        {"Categoria": "Chá", "Item": "Maçãs", "Qtd_Total": 12.0, "Unidade": "unid.", "Qtd_Faltante": 12.0, "Status": "Pendente", "Doadores": ""},
        {"Categoria": "Chá", "Item": "Abacaxi", "Qtd_Total": 6.0, "Unidade": "unid.", "Qtd_Faltante": 6.0, "Status": "Pendente", "Doadores": ""},
        {"Categoria": "Chá", "Item": "Cravo", "Qtd_Total": 3.0, "Unidade": "pct", "Qtd_Faltante": 3.0, "Status": "Pendente", "Doadores": ""},
        {"Categoria": "Chá", "Item": "Canela em rama", "Qtd_Total": 3.0, "Unidade": "pct", "Qtd_Faltante": 3.0, "Status": "Pendente", "Doadores": ""},
        # Temperos/Outros
        {"Categoria": "Temperos", "Item": "Cebola", "Qtd_Total": 4.0, "Unidade": "kg", "Qtd_Faltante": 0.0, "Status": "Doado", "Doadores": "Nazira (4kg)"},
        {"Categoria": "Temperos", "Item": "Alho", "Qtd_Total": 1.0, "Unidade": "kg", "Qtd_Faltante": 1.0, "Status": "Pendente", "Doadores": ""},
        {"Categoria": "Temperos", "Item": "Vinagre", "Qtd_Total": 2.0, "Unidade": "litros", "Qtd_Faltante": 0.0, "Status": "Doado", "Doadores": "Nilceu (Betel) (2L)"},
        {"Categoria": "Temperos", "Item": "Óleo", "Qtd_Total": 6.0, "Unidade": "litros", "Qtd_Faltante": 0.0, "Status": "Doado", "Doadores": "Juliana Borges (6L)"},
        {"Categoria": "Temperos", "Item": "Pimenta em pó", "Qtd_Total": 3.0, "Unidade": "pct", "Qtd_Faltante": 3.0, "Status": "Pendente", "Doadores": ""},
        {"Categoria": "Temperos", "Item": "Sal", "Qtd_Total": 4.0, "Unidade": "pct", "Qtd_Faltante": 4.0, "Status": "Pendente", "Doadores": ""},
        {"Categoria": "Temperos", "Item": "Creme de cebola", "Qtd_Total": 2.0, "Unidade": "pct", "Qtd_Faltante": 2.0, "Status": "Pendente", "Doadores": ""},
        {"Categoria": "Temperos", "Item": "Margarina", "Qtd_Total": 1.0, "Unidade": "pote gr.", "Qtd_Faltante": 1.0, "Status": "Pendente", "Doadores": ""},
        {"Categoria": "Temperos", "Item": "Orégano", "Qtd_Total": 1.0, "Unidade": "pct", "Qtd_Faltante": 1.0, "Status": "Pendente", "Doadores": ""},
        {"Categoria": "Temperos", "Item": "Tomate cereja", "Qtd_Total": 2.0, "Unidade": "cx", "Qtd_Faltante": 2.0, "Status": "Pendente", "Doadores": ""},
        {"Categoria": "Temperos", "Item": "Pimentão vermelho", "Qtd_Total": 3.0, "Unidade": "unid.", "Qtd_Faltante": 3.0, "Status": "Pendente", "Doadores": ""},
        {"Categoria": "Temperos", "Item": "Pimentão amarelo", "Qtd_Total": 3.0, "Unidade": "unid.", "Qtd_Faltante": 3.0, "Status": "Pendente", "Doadores": ""},
        {"Categoria": "Temperos", "Item": "Pimentão verde", "Qtd_Total": 3.0, "Unidade": "unid.", "Qtd_Faltante": 3.0, "Status": "Pendente", "Doadores": ""},
        {"Categoria": "Temperos", "Item": "Alho poró", "Qtd_Total": 1.0, "Unidade": "maço", "Qtd_Faltante": 1.0, "Status": "Pendente", "Doadores": ""},
        {"Categoria": "Temperos", "Item": "Salsão", "Qtd_Total": 1.0, "Unidade": "maço", "Qtd_Faltante": 1.0, "Status": "Pendente", "Doadores": ""},
        {"Categoria": "Temperos", "Item": "Caldo de legumes", "Qtd_Total": 1.0, "Unidade": "pct", "Qtd_Faltante": 1.0, "Status": "Pendente", "Doadores": ""},
        {"Categoria": "Temperos", "Item": "Cheiro verde", "Qtd_Total": 7.0, "Unidade": "maços", "Qtd_Faltante": 7.0, "Status": "Pendente", "Doadores": ""},
        {"Categoria": "Temperos", "Item": "Cebola roxa", "Qtd_Total": 7.0, "Unidade": "unid.", "Qtd_Faltante": 7.0, "Status": "Pendente", "Doadores": ""},
        {"Categoria": "Diversos", "Item": "Copos c/ água mineral", "Qtd_Total": 300.0, "Unidade": "unid.", "Qtd_Faltante": 300.0, "Status": "Pendente", "Doadores": ""}
    ]
    df = pd.DataFrame(dados_iniciais)
    df.to_csv(ARQUIVO_DADOS, index=False)
    return df

def salvar_dados(df):
    df.to_csv(ARQUIVO_DADOS, index=False)

# Carrega os dados sempre que a página atualiza
df_doacoes = carregar_dados()

if 'etapa' not in st.session_state:
    st.session_state.etapa = 1
if 'itens_selecionados' not in st.session_state:
    st.session_state.itens_selecionados = []

# ==========================================
# 4. MENU LATERAL
# ==========================================
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3048/3048122.png", width=100)
st.sidebar.title("Menu ECC")
menu = st.sidebar.radio("Escolha a página:", ["Área de Doação (Irmãos)", "Painel de Controle (Coordenação)"])

# ==========================================
# 5. TELA 1: ÁREA DE DOAÇÃO (PARCIAL)
# ==========================================
if menu == "Área de Doação (Irmãos)":
    st.title("Lista de Doações - ECC 🙏")
    
    df_pendentes = df_doacoes[df_doacoes["Status"] == "Pendente"]

    if df_pendentes.empty:
        st.success("Glória a Deus! Todos os itens já foram doados.")
    else:
        if st.session_state.etapa == 1:
            st.write("Marque o que deseja doar. Se o item tiver muita quantidade, você pode escolher doar apenas uma parte!")
            
            selecionados_agora = []
            
            categorias = df_pendentes['Categoria'].unique()
            for cat in categorias:
                with st.expander(f"📌 {cat}", expanded=True):
                    df_cat = df_pendentes[df_pendentes['Categoria'] == cat]
                    for idx, row in df_cat.iterrows():
                        falta = float(row['Qtd_Faltante'])
                        unidade = row['Unidade']
                        
                        # Formata pra não ficar "8.0" se for número redondo
                        falta_disp = int(falta) if falta.is_integer() else falta
                        total_disp = int(row['Qtd_Total']) if float(row['Qtd_Total']).is_integer() else row['Qtd_Total']
                        
                        # O EMOJI MÁGICO ENTRA AQUI!
                        emoji = obter_emoji(row['Item'])
                        nome_display = f"{emoji} {row['Item']} (Falta: {falta_disp} {unidade} de {total_disp} {unidade})"
                        chave_unica = f"item_{idx}"
                        
                        # Se a pessoa marcou o checkbox
                        if st.checkbox(nome_display, key=chave_unica):
                            
                            # Define se o passo é de 0.5 (kg/litro) ou 1.0 (unidades/caixas)
                            step_val = 0.5 if unidade in ['kg', 'litro', 'litros'] else 1.0
                            
                            qtd_doada = st.number_input(
                                f"↳ Quantidade que você vai doar ({unidade}):",
                                min_value=0.5 if step_val == 0.5 else 1.0,
                                max_value=float(falta),
                                step=step_val,
                                value=float(falta),
                                key=f"qtd_{idx}"
                            )
                            selecionados_agora.append({"idx": idx, "qtd": qtd_doada, "unidade": unidade, "item": row['Item'], "emoji": emoji})
            
            if st.button("Próximo ➡️"):
                if selecionados_agora:
                    st.session_state.itens_selecionados = selecionados_agora
                    st.session_state.etapa = 2
                    st.rerun()
                else:
                    st.warning("Selecione pelo menos um item para continuar.")
                    
        # ETAPA 2: CONFIRMAÇÃO
        elif st.session_state.etapa == 2:
            st.header("2. Confirme sua doação")
            st.write("**Você está doando:**")
            
            for item_data in st.session_state.itens_selecionados:
                qtd_formatada = int(item_data['qtd']) if float(item_data['qtd']).is_integer() else item_data['qtd']
                st.success(f"✅ {item_data['emoji']} {item_data['item']} - {qtd_formatada} {item_data['unidade']}")
                
            nome_doador = st.text_input("Qual é o seu nome ou da sua família?")
            
            col1, col2 = st.columns([1, 1])
            with col1:
                if st.button("⬅️ Voltar"):
                    st.session_state.etapa = 1
                    st.rerun()
            with col2:
                if st.button("💾 Confirmar Doação"):
                    if nome_doador:
                        for item_data in st.session_state.itens_selecionados:
                            idx = item_data['idx']
                            qtd_doada = item_data['qtd']
                            unid = item_data['unidade']
                            
                            # Subtrai do faltante
                            df_doacoes.at[idx, 'Qtd_Faltante'] -= qtd_doada
                            
                            # Registra o nome + quantidade q a pessoa deu
                            qtd_fmt = int(qtd_doada) if float(qtd_doada).is_integer() else qtd_doada
                            novo_registro = f"{nome_doador} ({qtd_fmt} {unid})"
                            
                            doadores_atuais = str(df_doacoes.at[idx, 'Doadores'])
                            if doadores_atuais == "nan" or doadores_atuais.strip() == "":
                                df_doacoes.at[idx, 'Doadores'] = novo_registro
                            else:
                                df_doacoes.at[idx, 'Doadores'] = doadores_atuais + ", " + novo_registro
                            
                            # Se zerou, marca como doado
                            if df_doacoes.at[idx, 'Qtd_Faltante'] <= 0:
                                df_doacoes.at[idx, 'Status'] = 'Doado'
                                df_doacoes.at[idx, 'Qtd_Faltante'] = 0.0
                        
                        salvar_dados(df_doacoes)
                        
                        st.balloons()
                        st.success(f"Deus abençoe, {nome_doador}! Sua doação foi registrada.")
                        st.session_state.etapa = 1
                        st.session_state.itens_selecionados = []
                    else:
                        st.error("Por favor, preencha o seu nome.")

# ==========================================
# 6. TELA 2: PAINEL DE CONTROLE 
# ==========================================
elif menu == "Painel de Controle (Coordenação)":
    st.title("📊 Painel de Controle")
    
    # ----------------------------------------------------
    # BOTÕES DE EXPORTAÇÃO (XLS e PDF)
    # ----------------------------------------------------
    col_pdf, col_xls = st.columns(2)
    
    # Gerar Excel
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
        df_doacoes.to_excel(writer, index=False, sheet_name="Doacoes")
    
    with col_xls:
        st.download_button(
            label="📊 Baixar Relatório (Excel)",
            data=buffer.getvalue(),
            file_name="relatorio_ecc.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    # Gerar PDF
    def gerar_pdf(df):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, "Relatório de Doações - ECC", ln=True, align='C')
        pdf.ln(5)
        
        pdf.set_font("Arial", size=10)
        for _, row in df.iterrows():
            falta_disp = int(row['Qtd_Faltante']) if float(row['Qtd_Faltante']).is_integer() else row['Qtd_Faltante']
            tot_disp = int(row['Qtd_Total']) if float(row['Qtd_Total']).is_integer() else row['Qtd_Total']
            
            texto = f"[{row['Status'].upper()}] {row['Categoria']} | {row['Item']}: Falta {falta_disp} de {tot_disp} {row['Unidade']} -> Doadores: {row['Doadores']}"
            texto_seguro = texto.encode('latin-1', 'replace').decode('latin-1')
            pdf.multi_cell(0, 8, txt=texto_seguro)
            
        return pdf.output(dest="S").encode("latin-1")
    
    with col_pdf:
        st.download_button(
            label="📄 Baixar Relatório (PDF)",
            data=gerar_pdf(df_doacoes),
            file_name="relatorio_ecc.pdf",
            mime="application/pdf"
        )
    
    st.divider()

    # ----------------------------------------------------
    # TABELA VISUAL
    # ----------------------------------------------------
    st.subheader("📋 Acompanhamento ao Vivo")
    filtro_status = st.radio("Filtrar por:", ["Todos", "Apenas Pendentes", "Apenas Doados"], horizontal=True)
    
    if filtro_status == "Apenas Pendentes":
        df_mostrar = df_doacoes[df_doacoes['Status'] == "Pendente"]
    elif filtro_status == "Apenas Doados":
        df_mostrar = df_doacoes[df_doacoes['Status'] == "Doado"]
    else:
        df_mostrar = df_doacoes
        
    st.dataframe(df_mostrar, use_container_width=True, hide_index=True)

    # ----------------------------------------------------
    # ADICIONAR NOVO ITEM
    # ----------------------------------------------------
    st.divider()
    st.subheader("➕ Adicionar Novo Item")
    
    lista_categorias = df_doacoes['Categoria'].unique().tolist()
    nova_categoria = st.selectbox("Escolha a Área/Categoria:", lista_categorias)
    novo_nome_item = st.text_input("Nome do item (Ex: Pão Francês)")
    
    col_qtd, col_un = st.columns(2)
    with col_qtd:
        nova_qtd = st.number_input("Quantidade Total (Ex: 50)", min_value=0.5, step=1.0)
    with col_un:
        nova_unidade = st.text_input("Unidade (Ex: kg, unid, L)")
        
    if st.button("Adicionar Item à Lista"):
        if novo_nome_item.strip() != "" and nova_unidade.strip() != "":
            nova_linha = {
                "Categoria": nova_categoria, 
                "Item": novo_nome_item, 
                "Qtd_Total": float(nova_qtd),
                "Unidade": nova_unidade,
                "Qtd_Faltante": float(nova_qtd),
                "Status": "Pendente", 
                "Doadores": ""
            }
            df_doacoes = pd.concat([df_doacoes, pd.DataFrame([nova_linha])], ignore_index=True)
            salvar_dados(df_doacoes)
            st.success(f"Item adicionado!")
            st.rerun()
        else:
            st.error("Preencha o nome e a unidade.")

    # ----------------------------------------------------
    # CANCELAR/RESETAR ITEM
    # ----------------------------------------------------
    st.divider()
    st.subheader("❌ Resetar Doação de um Item")
    st.warning("Atenção: Cancelar um item vai apagar TODAS as doações registradas nele e voltar a quantidade faltante pro máximo.")
    
    df_alterados = df_doacoes[df_doacoes['Qtd_Faltante'] < df_doacoes['Qtd_Total']]
    opcoes_cancelar = ["Selecione..."]
    dict_cancelar = {}
    
    for idx, row in df_alterados.iterrows():
        texto_opcao = f"{row['Item']} (Doado por: {row['Doadores']})"
        opcoes_cancelar.append(texto_opcao)
        dict_cancelar[texto_opcao] = idx
        
    item_para_cancelar = st.selectbox("Escolha o item para resetar:", opcoes_cancelar)
    
    if st.button("Resetar este item para Pendente"):
        if item_para_cancelar != "Selecione...":
            idx_cancelar = dict_cancelar[item_para_cancelar]
            
            df_doacoes.at[idx_cancelar, 'Status'] = 'Pendente'
            df_doacoes.at[idx_cancelar, 'Qtd_Faltante'] = df_doacoes.at[idx_cancelar, 'Qtd_Total']
            df_doacoes.at[idx_cancelar, 'Doadores'] = ''
            salvar_dados(df_doacoes)
            
            st.success("Item resetado com sucesso!")
            st.rerun()

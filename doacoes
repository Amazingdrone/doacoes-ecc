import streamlit as st
import pandas as pd
import os

# ==========================================
# 1. CONFIGURAÇÃO DA PÁGINA
# ==========================================
st.set_page_config(page_title="Doações ECC", layout="centered")

ARQUIVO_DADOS = 'banco_doacoes.csv'

# ==========================================
# 2. INICIALIZAÇÃO DO BANCO DE DADOS (CSV)
# ==========================================
def carregar_dados():
    # Se o arquivo já existe, carrega ele (para manter os dados salvos)
    if os.path.exists(ARQUIVO_DADOS):
        return pd.read_csv(ARQUIVO_DADOS)
    
    # Se não existe, cria o banco de dados inicial com todos os itens da sua lista!
    dados_iniciais = [
        # Sábado - Almoço
        {"Categoria": "Almoço Sáb", "Item": "Arroz branco (8kg)", "Status": "Doado", "Doador": "Têre (Betel)"},
        {"Categoria": "Almoço Sáb", "Item": "Arroz branco (5kg)", "Status": "Doado", "Doador": "Cristina (Maranata)"},
        {"Categoria": "Almoço Sáb", "Item": "Peito de Frango s/osso (65kg)", "Status": "Pendente", "Doador": ""},
        {"Categoria": "Almoço Sáb", "Item": "Batata palha (18kg)", "Status": "Pendente", "Doador": ""},
        {"Categoria": "Almoço Sáb", "Item": "Creme de leite (2 cx c/ 20)", "Status": "Doado", "Doador": "Neemias"},
        {"Categoria": "Almoço Sáb", "Item": "Champion (1 Balde)", "Status": "Pendente", "Doador": ""},
        {"Categoria": "Almoço Sáb", "Item": "Ketchup (1 litro)", "Status": "Doado", "Doador": "Onória (Betel)"},
        {"Categoria": "Almoço Sáb", "Item": "Mostarda (1 litro)", "Status": "Doado", "Doador": "Onória (Betel)"},
        {"Categoria": "Almoço Sáb", "Item": "Shoyo (1 litro)", "Status": "Pendente", "Doador": ""},
        {"Categoria": "Almoço Sáb", "Item": "Tomate (10 kg)", "Status": "Doado", "Doador": "André Aranha"},
        {"Categoria": "Almoço Sáb", "Item": "Alface (15 maços)", "Status": "Pendente", "Doador": ""},
        {"Categoria": "Almoço Sáb", "Item": "Cenoura (6kg)", "Status": "Pendente", "Doador": ""},
        {"Categoria": "Almoço Sáb", "Item": "Vagem (3kg)", "Status": "Pendente", "Doador": ""},
        {"Categoria": "Almoço Sáb", "Item": "Massa de tomate (6Kg)", "Status": "Pendente", "Doador": ""},
        # Sábado - Mousse
        {"Categoria": "Sobremesa Sáb", "Item": "Suco maracujá conc. (10 garrafas)", "Status": "Pendente", "Doador": ""},
        {"Categoria": "Sobremesa Sáb", "Item": "Creme de leite (1 cx c/20)", "Status": "Doado", "Doador": "Nize (Maranata)"},
        {"Categoria": "Sobremesa Sáb", "Item": "Creme de leite (5 cx c/20)", "Status": "Doado", "Doador": "Neemias"},
        {"Categoria": "Sobremesa Sáb", "Item": "Leite moça (20 caixinhas)", "Status": "Doado", "Doador": "Marcos e Thays"},
        {"Categoria": "Sobremesa Sáb", "Item": "Limão (2 kg)", "Status": "Doado", "Doador": "Ivanice (Maranata)"},
        {"Categoria": "Sobremesa Sáb", "Item": "Creme de leite p/ limão (3 cx c/20)", "Status": "Doado", "Doador": "Diego (Ágape)"},
        {"Categoria": "Sobremesa Sáb", "Item": "Creme de leite p/ limão (3 cx c/20)", "Status": "Doado", "Doador": "Neemias"},
        {"Categoria": "Sobremesa Sáb", "Item": "Leite moça p/ limão (20 caixinhas)", "Status": "Doado", "Doador": "Marcos e Thays"},
        {"Categoria": "Sobremesa Sáb", "Item": "Copinhos sobremesa c/tampa (400)", "Status": "Doado", "Doador": "Indianara (Maranata)"},
        # Domingo - Almoço e Risoto
        {"Categoria": "Almoço Dom", "Item": "Macarrão (10 kg)", "Status": "Doado", "Doador": "Silvia e Onória"},
        {"Categoria": "Almoço Dom", "Item": "Molho de tomate (6 kg)", "Status": "Doado", "Doador": "Juliana Borges"},
        {"Categoria": "Almoço Dom", "Item": "Carne moída (60 kg)", "Status": "Pendente", "Doador": ""},
        {"Categoria": "Almoço Dom", "Item": "Alface (15 maços)", "Status": "Pendente", "Doador": ""},
        {"Categoria": "Almoço Dom", "Item": "Tomate (6 kg)", "Status": "Doado", "Doador": "Miely"},
        {"Categoria": "Almoço Dom", "Item": "Milho verde (2 kg)", "Status": "Doado", "Doador": "Miely"},
        {"Categoria": "Almoço Dom", "Item": "Ervilha (1 kg)", "Status": "Doado", "Doador": "Miely"},
        {"Categoria": "Almoço Dom", "Item": "Maionese Hellman's (2 kg)", "Status": "Doado", "Doador": "Miely"},
        {"Categoria": "Risoto Dom", "Item": "Arroz branco (10kg)", "Status": "Doado", "Doador": "Shin (Betel)"},
        {"Categoria": "Risoto Dom", "Item": "Tomate cereja (2 caixas)", "Status": "Pendente", "Doador": ""},
        {"Categoria": "Risoto Dom", "Item": "Creme de leite (1 cx c/20)", "Status": "Doado", "Doador": "Marcos e Thays"},
        {"Categoria": "Risoto Dom", "Item": "Leite de coco (5 garrafas)", "Status": "Pendente", "Doador": ""},
        {"Categoria": "Risoto Dom", "Item": "Requeijão (4 potes)", "Status": "Pendente", "Doador": ""},
        # Domingo - Pudim
        {"Categoria": "Sobremesa Dom", "Item": "Leite (6 Litros) - Parte 1", "Status": "Doado", "Doador": "Valéria (Maranata)"},
        {"Categoria": "Sobremesa Dom", "Item": "Leite (6 Litros) - Parte 2", "Status": "Pendente", "Doador": ""},
        {"Categoria": "Sobremesa Dom", "Item": "Pudim de baunilha (13 cx) - Parte 1", "Status": "Doado", "Doador": "Valéria (Maranata)"},
        {"Categoria": "Sobremesa Dom", "Item": "Pudim de baunilha (13 cx) - Parte 2", "Status": "Pendente", "Doador": ""},
        {"Categoria": "Sobremesa Dom", "Item": "Chantily (2 litros)", "Status": "Doado", "Doador": "Michele (Maranata)"},
        {"Categoria": "Sobremesa Dom", "Item": "Açúcar (5 kg)", "Status": "Doado", "Doador": "Nádia (Maranata)"},
        # Bebidas
        {"Categoria": "Bebidas", "Item": "Coca-cola normal 2L (6 garrafas)", "Status": "Doado", "Doador": "Marcos e Thays"},
        {"Categoria": "Bebidas", "Item": "Coca-cola normal 2L (6 garrafas)", "Status": "Pendente", "Doador": ""},
        {"Categoria": "Bebidas", "Item": "Coca-cola Zero 2L (6 garrafas)", "Status": "Doado", "Doador": "Marcos e Thays"},
        {"Categoria": "Bebidas", "Item": "Coca-cola Zero 2L (6 garrafas)", "Status": "Pendente", "Doador": ""},
        {"Categoria": "Bebidas", "Item": "Guaraná normal 2L (6 garrafas)", "Status": "Doado", "Doador": "Luiza (Maranata)"},
        {"Categoria": "Bebidas", "Item": "Guaraná normal 2L (6 garrafas)", "Status": "Pendente", "Doador": ""},
        {"Categoria": "Bebidas", "Item": "Guaraná Zero 2L (10 garrafas)", "Status": "Pendente", "Doador": ""},
        {"Categoria": "Bebidas", "Item": "Fanta laranja 2L (6 garrafas)", "Status": "Pendente", "Doador": ""},
        {"Categoria": "Bebidas", "Item": "Água mineral c/ gás 1,5L (12 garrafas)", "Status": "Pendente", "Doador": ""},
        # Outros
        {"Categoria": "Temperos/Outros", "Item": "Cebola (4 kg)", "Status": "Doado", "Doador": "Nazira"},
        {"Categoria": "Temperos/Outros", "Item": "Alho (1 kg)", "Status": "Pendente", "Doador": ""},
        {"Categoria": "Temperos/Outros", "Item": "Vinagre (2 litros)", "Status": "Doado", "Doador": "Nilceu (Betel)"},
        {"Categoria": "Temperos/Outros", "Item": "Óleo (6 litros)", "Status": "Doado", "Doador": "Juliana Borges"},
        {"Categoria": "Temperos/Outros", "Item": "Sal (4 pacotes)", "Status": "Pendente", "Doador": ""},
        {"Categoria": "Temperos/Outros", "Item": "Cheiro verde (7 maços)", "Status": "Pendente", "Doador": ""},
        {"Categoria": "Diversos", "Item": "Copos com água mineral (300 unid.)", "Status": "Pendente", "Doador": ""}
    ]
    df = pd.DataFrame(dados_iniciais)
    df.to_csv(ARQUIVO_DADOS, index=False)
    return df

def salvar_dados(df):
    df.to_csv(ARQUIVO_DADOS, index=False)

# Carrega os dados sempre que a página atualiza
df_doacoes = carregar_dados()

# Variáveis de controle de tela
if 'etapa' not in st.session_state:
    st.session_state.etapa = 1
if 'itens_selecionados' not in st.session_state:
    st.session_state.itens_selecionados = []

# ==========================================
# 3. MENU LATERAL (Navegação)
# ==========================================
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3048/3048122.png", width=100) # Ícone de doação
st.sidebar.title("Menu ECC")
menu = st.sidebar.radio("Escolha a página:", ["Área de Doação (Irmãos)", "Painel de Controle (Coordenação)"])

# ==========================================
# 4. TELA 1: ÁREA DE DOAÇÃO (Para os irmãos)
# ==========================================
if menu == "Área de Doação (Irmãos)":
    st.title("Lista de Doações - ECC 🙏")
    
    # Filtra apenas o que ainda está pendente
    df_pendentes = df_doacoes[df_doacoes["Status"] == "Pendente"]

    if df_pendentes.empty:
        st.success("Glória a Deus! Todos os itens já foram doados. Muito obrigado a todos!")
    else:
        # Fluxo de doação
        if st.session_state.etapa == 1:
            st.header("1. O que você gostaria de doar?")
            st.write("Marque os itens abaixo e clique em Próximo.")
            
            selecionados_agora = []
            
            # Agrupa os itens por categoria para ficar mais organizado
            categorias = df_pendentes['Categoria'].unique()
            for cat in categorias:
                st.subheader(f"📌 {cat}")
                itens_cat = df_pendentes[df_pendentes['Categoria'] == cat]['Item'].tolist()
                for item in itens_cat:
                    if st.checkbox(item, key=item):
                        selecionados_agora.append(item)
            
            if st.button("Próximo ➡️"):
                if selecionados_agora:
                    st.session_state.itens_selecionados = selecionados_agora
                    st.session_state.etapa = 2
                    st.rerun()
                else:
                    st.warning("Por favor, selecione pelo menos um item para continuar.")
                    
        elif st.session_state.etapa == 2:
            st.header("2. Confirme sua doação")
            st.write("**Você selecionou:**")
            for item in st.session_state.itens_selecionados:
                st.success(f"✅ {item}")
                
            nome_doador = st.text_input("Qual é o seu nome ou da sua família?")
            
            col1, col2 = st.columns([1, 1])
            with col1:
                if st.button("⬅️ Voltar"):
                    st.session_state.etapa = 1
                    st.rerun()
            with col2:
                if st.button("💾 Confirmar Doação"):
                    if nome_doador:
                        # Atualiza o banco de dados
                        for item in st.session_state.itens_selecionados:
                            # Localiza a linha do item e atualiza
                            indice = df_doacoes.index[df_doacoes['Item'] == item].tolist()[0]
                            df_doacoes.at[indice, 'Status'] = 'Doado'
                            df_doacoes.at[indice, 'Doador'] = nome_doador
                        
                        salvar_dados(df_doacoes) # Salva no CSV
                        
                        st.balloons()
                        st.success(f"Deus abençoe, {nome_doador}! Sua doação foi registrada.")
                        st.session_state.etapa = 1
                        st.session_state.itens_selecionados = []
                    else:
                        st.error("Por favor, preencha o seu nome.")

# ==========================================
# 5. TELA 2: PAINEL DE CONTROLE (Coordenador)
# ==========================================
elif menu == "Painel de Controle (Coordenação)":
    st.title("📊 Painel de Controle - Coordenação")
    st.write("Acompanhe aqui como estão as doações em tempo real.")
    
    # Métricas
    total_itens = len(df_doacoes)
    total_doados = len(df_doacoes[df_doacoes['Status'] == 'Doado'])
    total_pendentes = len(df_doacoes[df_doacoes['Status'] == 'Pendente'])
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total de Itens", total_itens)
    col2.metric("✅ Já Doados", total_doados)
    col3.metric("⏳ Pendentes", total_pendentes)
    
    st.divider()
    
    # Mostra a tabela completa com filtro
    st.subheader("Lista Completa")
    filtro_status = st.radio("Filtrar por:", ["Todos", "Apenas Pendentes", "Apenas Doados"], horizontal=True)
    
    if filtro_status == "Apenas Pendentes":
        df_mostrar = df_doacoes[df_doacoes['Status'] == "Pendente"]
    elif filtro_status == "Apenas Doados":
        df_mostrar = df_doacoes[df_doacoes['Status'] == "Doado"]
    else:
        df_mostrar = df_doacoes
        
    st.dataframe(df_mostrar, use_container_width=True, hide_index=True)

    # Opção para o coordenador "desmarcar" um item caso alguém desista
    st.divider()
    st.subheader("Corrigir/Cancelar Doação")
    item_para_cancelar = st.selectbox("Se alguém desistiu, escolha o item para voltar para pendente:", 
                                      ["Selecione..."] + df_doacoes[df_doacoes['Status'] == 'Doado']['Item'].tolist())
    
    if st.button("Cancelar doação deste item"):
        if item_para_cancelar != "Selecione...":
            indice = df_doacoes.index[df_doacoes['Item'] == item_para_cancelar].tolist()[0]
            df_doacoes.at[indice, 'Status'] = 'Pendente'
            df_doacoes.at[indice, 'Doador'] = ''
            salvar_dados(df_doacoes)
            st.success(f"O item '{item_para_cancelar}' voltou para a lista de pendentes!")
            st.rerun()

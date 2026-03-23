# ==========================================
        # ETAPA 1: ONDE ACONTECEU O ERRO
        # ==========================================
        if st.session_state.etapa == 1:
            st.header("1. O que você gostaria de doar?")
            st.write("Marque os itens abaixo e clique em Próximo.")
            
            selecionados_agora = []
            
            categorias = df_pendentes['Categoria'].unique()
            for cat in categorias:
                st.subheader(f"📌 {cat}")
                
                # Pegamos os itens da categoria já com o número da linha original (índice)
                df_cat = df_pendentes[df_pendentes['Categoria'] == cat]
                for idx, row in df_cat.iterrows():
                    nome_do_item = row['Item']
                    
                    # Criamos uma chave 100% única usando o número da linha (ex: item_42)
                    chave_unica = f"item_{idx}"
                    
                    if st.checkbox(nome_do_item, key=chave_unica):
                        # Guardamos o NÚMERO DA LINHA (idx) em vez do nome do item
                        selecionados_agora.append(idx)
            
            if st.button("Próximo ➡️"):
                if selecionados_agora:
                    st.session_state.itens_selecionados = selecionados_agora
                    st.session_state.etapa = 2
                    st.rerun()
                else:
                    st.warning("Por favor, selecione pelo menos um item para continuar.")
                    
        # ==========================================
        # ETAPA 2: CONFIRMAÇÃO
        # ==========================================
        elif st.session_state.etapa == 2:
            st.header("2. Confirme sua doação")
            st.write("**Você selecionou:**")
            
            # Mostramos o nome do item buscando pelo número da linha
            for idx in st.session_state.itens_selecionados:
                nome_do_item = df_doacoes.at[idx, 'Item']
                st.success(f"✅ {nome_do_item}")
                
            nome_doador = st.text_input("Qual é o seu nome ou da sua família?")
            
            col1, col2 = st.columns([1, 1])
            with col1:
                if st.button("⬅️ Voltar"):
                    st.session_state.etapa = 1
                    st.rerun()
            with col2:
                if st.button("💾 Confirmar Doação"):
                    if nome_doador:
                        # Atualiza o banco de dados editando a linha exata (evita erro em itens com mesmo nome)
                        for idx in st.session_state.itens_selecionados:
                            df_doacoes.at[idx, 'Status'] = 'Doado'
                            df_doacoes.at[idx, 'Doador'] = nome_doador
                        
                        salvar_dados(df_doacoes) # Salva no CSV
                        
                        st.balloons()
                        st.success(f"Deus abençoe, {nome_doador}! Sua doação foi registrada.")
                        st.session_state.etapa = 1
                        st.session_state.itens_selecionados = []
                    else:
                        st.error("Por favor, preencha o seu nome.")

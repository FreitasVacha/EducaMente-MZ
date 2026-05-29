import streamlit as st

# Configuração da Página
st.set_page_config(page_title="EducaMente MZ", page_icon="📚", layout="centered")

# Estilo visual
st.title("📚 EducaMente MZ")
st.markdown("### Hub Inteligente de Apoio ao SNE - Moçambique")

# Seletor de Perfil
perfil = st.sidebar.selectbox("Selecione seu perfil", ["Docente", "Aluno"])

if perfil == "Docente":
    st.header("Painel do Docente")
    disciplina = st.selectbox("Disciplina", ["Português", "Matemática", "História", "Física", "Biologia"])
    tema = st.text_input("Tema da Aula")
    
    if st.button("Gerar Plano de Aula"):
        if tema:
            st.markdown("---")
            st.success(f"Plano Estruturado: {tema}")
            st.write("**Objetivo (Taxonomia de Bloom):** Analisar e Aplicar conceitos.")
            st.write("**Sequência Didática:** Introdução (10min) -> Desenvolvimento (30min) -> Avaliação (10min).")
            st.write("**Dica:** Este tema costuma ser desafiador pela confusão entre conceitos básicos.")
            st.info("Nota: Este plano foi gerado com base nas diretrizes do SNE.")
        else:
            st.warning("Por favor, insira o tema da aula.")

elif perfil == "Aluno":
    st.header("Painel do Aluno")
    tema_busca = st.text_input("Pesquisar matéria para estudo")
    
    if st.button("Buscar Resumo"):
        if tema_busca:
            st.markdown("---")
            st.write(f"### Resumo: {tema_busca}")
            st.write("Aqui aparecerá o resumo filtrado dos manuais do SNE.")
            st.download_button("Baixar Kit de Estudo (PDF)", data="Conteúdo em PDF", file_name="estudo.pdf")
        else:
            st.warning("Insira o tema que deseja estudar.")

st.sidebar.markdown("---")
st.sidebar.info("Desenvolvido para fortalecer a educação em Moçambique.")

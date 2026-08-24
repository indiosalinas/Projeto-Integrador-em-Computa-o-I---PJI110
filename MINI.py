import streamlit as st

st.set_page_config(page_title="MINI Psiquiatria", layout="centered")

st.title("🧠 MINI - Entrevista Psiquiátrica Estruturada")

# -----------------------------
# ESTADO
# -----------------------------
if "respostas" not in st.session_state:
    st.session_state.respostas = {}

r = st.session_state.respostas

# -----------------------------
# MÓDULO A - DEPRESSÃO
# -----------------------------
# -----------------------------
# MÓDULO A - EPISÓDIO DEPRESSIVO MAIOR
# -----------------------------
st.header("Módulo A - Episódio Depressivo Maior")

# A1
r["A1"] = st.radio(
    "Nas duas últimas semanas, sentiu-se triste, desanimado ou deprimido na maior parte do dia?",
    ["Não", "Sim"], key="A1"
) == "Sim"

# A2
r["A2"] = st.radio(
    "Nas duas últimas semanas, perdeu o interesse ou prazer pelas coisas?",
    ["Não", "Sim"], key="A2"
) == "Sim"

# Condição para seguir
if r["A1"] or r["A2"]:

    st.subheader("Sintomas associados (A3)")

    r["A3a"] = st.checkbox("Alteração de apetite ou peso (±5%)")
    r["A3b"] = st.checkbox("Problemas de sono")
    r["A3c"] = st.checkbox("Agitação ou lentificação psicomotora")
    r["A3d"] = st.checkbox("Fadiga ou falta de energia")
    r["A3e"] = st.checkbox("Sentimento de culpa ou inutilidade")
    r["A3f"] = st.checkbox("Dificuldade de concentração")
    r["A3g"] = st.checkbox("Pensamentos de morte ou autoagressão")

    total_A3 = sum([
        r["A3a"], r["A3b"], r["A3c"],
        r["A3d"], r["A3e"], r["A3f"], r["A3g"]
    ])

    # Critério A4
    if total_A3 >= 3:
        st.success("Critério para Episódio Depressivo Maior ATUAL")

        # A5a
        r["A5a"] = st.radio(
            "Teve outros períodos semelhantes na vida?",
            ["Não", "Sim"], key="A5a"
        ) == "Sim"

        if r["A5a"]:
            # A5b
            r["A5b"] = st.radio(
                "Houve intervalo de pelo menos 2 meses sem sintomas?",
                ["Não", "Sim"], key="A5b"
            ) == "Sim"

            if r["A5b"]:
                st.warning("Episódio Depressivo Maior RECORRENTE")

        # -----------------------------
    # -----------------------------
# MELANCÓLICO (A')
# -----------------------------
st.subheader("Características Melancólicas")

# A6
A6_result = False

if r.get("A2"):
    st.info("A2 = SIM → A6 automaticamente positivo")
    A6_result = True

else:
    r["A6a"] = st.radio(
        "Perdeu a capacidade de reagir a coisas agradáveis?",
        ["Não", "Sim"],
        key="A6a"
    ) == "Sim"

    if not r["A6a"]:
        r["A6b"] = st.radio(
            "Mesmo com algo agradável, não conseguia melhorar?",
            ["Não", "Sim"],
            key="A6b"
        ) == "Sim"
    else:
        r["A6b"] = False

    A6_result = r["A6a"] or r["A6b"]

r["A6_final"] = A6_result


# A7
if r["A6_final"]:

    r["A7a"] = st.checkbox("Depressão diferente do luto", key="A7a")
    r["A7b"] = st.checkbox("Pior pela manhã", key="A7b")
    r["A7c"] = st.checkbox("Acorda muito cedo", key="A7c")
    r["A7d"] = r.get("A3c", False)
    r["A7e"] = r.get("A3a", False)
    r["A7f"] = st.checkbox("Culpa excessiva", key="A7f")

    total_A7 = sum([
        r["A7a"], r["A7b"], r["A7c"],
        r["A7d"], r["A7e"], r["A7f"]
    ])

    if total_A7 >= 3:
        st.error("Depressão com características melancólicas")

# -----------------------------
# MÓDULO D - MANIA
# -----------------------------
st.header("Módulo D - Mania/Hipomania")

r["D1"] = st.radio("Período de humor elevado/irritável?", ["Não", "Sim"], key="D1") == "Sim"

if r["D1"]:
    r["D2a"] = st.checkbox("Grandiosidade")
    r["D2b"] = st.checkbox("Pouca necessidade de sono")
    r["D2c"] = st.checkbox("Mais falante")
    r["D2d"] = st.checkbox("Fuga de ideias")
    r["D2e"] = st.checkbox("Distrabilidade")
    r["D2f"] = st.checkbox("Aumento de atividade")
    r["D2g"] = st.checkbox("Comportamento de risco")

# -----------------------------
# MÓDULO J - TAG
# -----------------------------
st.header("Módulo J - Ansiedade Generalizada")

r["J1"] = st.radio("Preocupação excessiva por meses?", ["Não", "Sim"], key="J1") == "Sim"

if r["J1"]:
    r["J2a"] = st.checkbox("Inquietação")
    r["J2b"] = st.checkbox("Fadiga")
    r["J2c"] = st.checkbox("Dificuldade de concentração", key="J2c")
    r["J2d"] = st.checkbox("Irritabilidade")
    r["J2e"] = st.checkbox("Tensão muscular")
    r["J2f"] = st.checkbox("Alteração do sono")

# -----------------------------
# MÓDULO E - PÂNICO
# -----------------------------
st.header("Módulo E - Transtorno do Pânico")

r["E1"] = st.radio("Teve ataques súbitos de medo intenso?", ["Não", "Sim"], key="E1") == "Sim"

if r["E1"]:
    r["E2a"] = st.checkbox("Palpitação")
    r["E2b"] = st.checkbox("Sudorese")
    r["E2c"] = st.checkbox("Falta de ar")
    r["E2d"] = st.checkbox("Medo de morrer")
    r["E2e"] = st.checkbox("Tontura")

# -----------------------------
# MÓDULO C - SUICÍDIO
# -----------------------------
st.header("Módulo C - Risco de Suicídio")

r["C1"] = st.checkbox("Desejo de estar morto")
r["C2"] = st.checkbox("Quis se machucar")
r["C3"] = st.checkbox("Pensou em suicídio")
r["C4"] = st.checkbox("Planejou suicídio")
r["C5"] = st.checkbox("Tentativa recente")
r["C6"] = st.checkbox("Tentativa na vida")

# -----------------------------
# FUNÇÕES
# -----------------------------
def avaliar_depressao(r):
    if not (r.get("A1") or r.get("A2")):
        return False, 0
    total = sum([r.get(k, False) for k in ["A3a","A3b","A3c","A3d","A3e","A3f","A3g"]])
    return total >= 3, total

def avaliar_mania(r):
    if not r.get("D1"):
        return False, 0
    total = sum([r.get(k, False) for k in ["D2a","D2b","D2c","D2d","D2e","D2f","D2g"]])
    return total >= 3, total

def avaliar_tag(r):
    if not r.get("J1"):
        return False, 0
    total = sum([r.get(k, False) for k in ["J2a","J2b","J2c","J2d","J2e","J2f"]])
    return total >= 3, total

def avaliar_panico(r):
    if not r.get("E1"):
        return False, 0
    total = sum([r.get(k, False) for k in ["E2a","E2b","E2c","E2d","E2e"]])
    return total >= 2, total

def risco_suicidio(r):
    pontos = 0
    if r.get("C1"): pontos += 1
    if r.get("C2"): pontos += 2
    if r.get("C3"): pontos += 6
    if r.get("C4"): pontos += 10
    if r.get("C5"): pontos += 10
    if r.get("C6"): pontos += 4

    if pontos >= 10: return "Alto"
    elif pontos >= 6: return "Moderado"
    elif pontos >= 1: return "Baixo"
    return "Nenhum"

# -----------------------------
# RESULTADO
# -----------------------------
st.header("📊 Resultado")

if st.button("Calcular"):

    dep, n_dep = avaliar_depressao(r)
    mania, n_mania = avaliar_mania(r)
    tag, n_tag = avaliar_tag(r)
    panico, n_panico = avaliar_panico(r)
    suic = risco_suicidio(r)

    if dep:
        st.success(f"Depressão maior ({n_dep} sintomas)")

    if mania:
        st.error(f"⚠️ Mania/Hipomania ({n_mania} sintomas)")

    if tag:
        st.info(f"Ansiedade Generalizada ({n_tag} sintomas)")

    if panico:
        st.warning(f"Pânico ({n_panico} sintomas)")

    if suic == "Alto":
        st.error("RISCO DE SUICÍDIO: ALTO")
    elif suic == "Moderado":
        st.warning("RISCO: MODERADO")

    st.divider()

    resumo = ""

    if mania:
        resumo += "Sugestivo de transtorno bipolar.\n"

    if dep:
        resumo += "Critérios para episódio depressivo maior.\n"

    if tag:
        resumo += "Quadro compatível com ansiedade generalizada.\n"

    if panico:
        resumo += "Presença de sintomas de pânico.\n"

    if suic != "Nenhum":
        resumo += f"Risco de suicídio: {suic}.\n"

    if resumo == "":
        resumo = "Sem alterações significativas."

    st.text_area("Relatório", resumo, height=150)

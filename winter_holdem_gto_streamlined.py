
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="윈터의 홀덤 GTO - 수정 버전", layout="centered")

st.title("🃏 윈터의 홀덤 GTO")
st.markdown("토너먼트 기반 전략 분석기 · 내 카드 2장만 이미지 클릭으로 선택")

# 카드 목록
card_dir = "cards/"
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
suits = ['s', 'h', 'd', 'c']
cards = [r + s for r in ranks for s in suits]

# 세션 상태 초기화
if "selected_cards" not in st.session_state:
    st.session_state.selected_cards = []
if "flop" not in st.session_state:
    st.session_state.flop = ["", "", ""]
if "turn" not in st.session_state:
    st.session_state.turn = ""
if "river" not in st.session_state:
    st.session_state.river = ""

# 내 핸드 (2장)
st.subheader("🎴 내 핸드카드 (2장, 이미지 클릭)")
cols = st.columns(13)
for i, card in enumerate(cards):
    with cols[i % 13]:
        if st.button(" ", key=card):
            if card in st.session_state.selected_cards:
                st.session_state.selected_cards.remove(card)
            elif len(st.session_state.selected_cards) < 2:
                st.session_state.selected_cards.append(card)
        st.image(f"{card_dir}{card}.png", width=60)

st.markdown("**선택된 카드:** " + " ".join(st.session_state.selected_cards))

# 보드카드 선택 (기존 selectbox 유지)
st.subheader("🃏 보드카드 선택 (플랍/턴/리버)")
flop = st.multiselect("플랍 (Flop, 최대 3장)", options=cards, default=st.session_state.flop)
turn = st.selectbox("턴 (Turn)", [""] + cards, index=0 if not st.session_state.turn else cards.index(st.session_state.turn) + 1)
river = st.selectbox("리버 (River)", [""] + cards, index=0 if not st.session_state.river else cards.index(st.session_state.river) + 1)

st.session_state.flop = flop
st.session_state.turn = turn
st.session_state.river = river

# 전략 계산 버튼
if len(st.session_state.selected_cards) == 2:
    if st.button("🎯 GTO 전략 계산"):
        st.success("전략 계산 결과 출력 (포지션, 핸드강도, 추천 액션 등)")
else:
    st.warning("핸드카드 2장을 먼저 선택해주세요.")


import streamlit as st
from pathlib import Path

st.set_page_config(page_title="윈터의 홀덤 GTO FINAL", layout="centered")

st.title("🃏 윈터의 홀덤 GTO - 최종 버전")
st.markdown("이미지 클릭 기반 핸드 + 보드카드 선택 / 포지션 기반 전략 추천")

card_dir = "cards/"
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
suits = ['s', 'h', 'd', 'c']
cards = [r + s for r in ranks for s in suits]

# 세션 상태 초기화
if "hole_cards" not in st.session_state:
    st.session_state.hole_cards = []
if "board_cards" not in st.session_state:
    st.session_state.board_cards = []

# 카드 선택 버튼 함수
def card_button(card, section):
    if st.button(" ", key=f"{section}-{card}"):
        if section == "hole":
            if card in st.session_state.hole_cards:
                st.session_state.hole_cards.remove(card)
            elif len(st.session_state.hole_cards) < 2 and card not in st.session_state.board_cards:
                st.session_state.hole_cards.append(card)
        elif section == "board":
            if card in st.session_state.board_cards:
                st.session_state.board_cards.remove(card)
            elif len(st.session_state.board_cards) < 5 and card not in st.session_state.hole_cards:
                st.session_state.board_cards.append(card)
    st.image(f"{card_dir}{card}.png", width=60)

# 내 핸드카드 선택 영역
st.markdown("## ✋ 내 핸드 (2장)")
hole_cols = st.columns(13)
for i, card in enumerate(cards):
    with hole_cols[i % 13]:
        card_button(card, "hole")

st.markdown("선택된 핸드: " + " ".join(st.session_state.hole_cards))

# 보드카드 선택 영역
st.markdown("## 🃏 보드카드 (최대 5장)")
board_cols = st.columns(13)
for i, card in enumerate(cards):
    with board_cols[i % 13]:
        card_button(card, "board")

st.markdown("선택된 보드카드: " + " ".join(st.session_state.board_cards))

# 전략 계산 버튼
if len(st.session_state.hole_cards) == 2:
    if st.button("🎯 GTO 전략 계산"):
        st.success("전략 계산 결과: [여기에 포지션 + 핸드 강도 기반 해설 출력 예정]")
else:
    st.warning("핸드 카드 2장을 먼저 선택해주세요.")

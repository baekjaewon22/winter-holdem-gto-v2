
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="윈터의 홀덤 GTO - 이미지 UI", layout="centered")

st.title("🃏 윈터의 홀덤 GTO v2")
st.markdown("이미지 클릭 기반 핸드/보드 선택 UI + 포지션/GTO 전략 추천")

st.markdown("## 🎴 내 핸드 선택 (2장)")

# 이미지 폴더 경로 (예: /cards/As.png 형식)
card_dir = "cards/"
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
suits = ['s', 'h', 'd', 'c']
cards = [r + s for r in ranks for s in suits]

selected_cards = st.session_state.get("selected_cards", [])

cols = st.columns(13)
for i, card in enumerate(cards):
    with cols[i % 13]:
        if st.button("", key=card):
            if card in selected_cards:
                selected_cards.remove(card)
            elif len(selected_cards) < 7:
                selected_cards.append(card)
        st.image(f"{card_dir}{card}.png", width=60)

st.session_state["selected_cards"] = selected_cards

st.markdown("### 📍 선택된 카드")
st.write(" ".join(selected_cards))

if len(selected_cards) >= 2:
    st.success("🎯 카드 선택 완료. 이제 GTO 전략 계산이 가능합니다.")
    if st.button("🔍 GTO 전략 계산 시작"):
        st.markdown("📈 [여기에 전략 계산 결과 출력 예정]")
else:
    st.warning("❗ 내 핸드카드 2장 이상 선택해주세요.")

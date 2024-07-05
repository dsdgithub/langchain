import streamlit as st
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# ChatOpenAI 모델 초기화
chat = ChatOpenAI(temperature=0)

# Streamlit UI 설정
# 대화 앞에 달리는 프로필 캐릭터
st.set_page_config(page_title="ChatOpenAI Demo", page_icon=":robot:")
st.header("ChatOpenAI-Demo")

# 세션 상태 초기화
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

# 대화 히스토리 표시
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# 사용자 입력 처리
# if prompt := 는 아래 두줄과 동일함
# prompt = st.chat_input("무엇을 도와드릴까요?")
# if prompt:

if prompt := st.chat_input("무엇을 도와드릴까요?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in chat.stream(st.session_state.messages):
            full_response += (response.content or "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# 스크롤을 최하단으로 이동
st.empty()
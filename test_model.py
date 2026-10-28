
from ollama import chat

print("Connecting to Qwen2.5 1.5B...")


# Start measuring response time
start_time = time.perf_counter()

response = chat(
    model=MODEL_NAME,
    messages=[
        {
            "role": "system",
            "content": (
                "You are a helpful AI study assistant. "
                "Explain concepts in simple language. "
                "Provide examples and code snippets "
                "when necessary."
            )
        },
        *st.session_state.messages
    ]
)

# Total wall-clock response time
response_time = time.perf_counter() - start_time

# Ollama response statistics
output_tokens = response.eval_count or 0
generation_seconds = (response.eval_duration or 0) / 1e9

tokens_per_second = (
    output_tokens / generation_seconds
    if generation_seconds > 0 else 0
)

answer = response.message.content

st.markdown(answer)

# Display model performance metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Response Time", f"{response_time:.2f}s")

with col2:
    st.metric("Output Tokens", output_tokens)

with col3:
    st.metric("Generation Speed", f"{tokens_per_second:.1f} tok/s")

# Save response in chat history
st.session_state.messages.append({
    "role": "assistant",
    "content": answer
})


print("\nAI Response:\n")
print(response.message.content)

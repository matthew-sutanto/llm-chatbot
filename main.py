from langchain_ollama.chat_models import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

from fastapi import Body, FastAPI
from fastapi.responses import FileResponse, StreamingResponse
from pydantic import BaseModel

app = FastAPI()

chat_model = ChatOllama(model="llama3.2:1b")

messages = [
    SystemMessage("""
    You are a very polite and helpful assistant.
    You will always end any response with an emoji.
    """)
]

@app.get("/")
async def index():
    return FileResponse("views/index.html")

class ChatRequest(BaseModel):
    user_message: str
@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    global messages
    async def generate():
        messages.append(HumanMessage(content=request.user_message))
        async for chunk in chat_model.astream(messages):
            yield f"data: {chunk.content}\n\n"
        messages.append(AIMessage(content=chunk.content))

    return StreamingResponse(
        generate(),
        media_type="text/event-stream"
    )


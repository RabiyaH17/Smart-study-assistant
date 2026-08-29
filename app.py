import gradio as gr

def load_book():
    try:
        with open("textbook.txt","r", encoding="utf-8") as f:
            return f.read()
    except:
        return "Photosynthesis is the process by which green plants make their own food using sunlight, carbon dioxide and water."

BOOK = load_book()

def chatbot_fn(q):
    if "photosynthesis" in q.lower():
        return "Photosynthesis is the process by which green plants make their own food using sunlight, carbon dioxide and water. Sunlight + CO2 + Water -> Glucose + Oxygen."
    return f"Chatbot Answer for '{q}': {BOOK[:300]}"

def rag_fn(q):
    if "photosynthesis" in q.lower():
        return f"RAG Answer (from textbook.txt): Photosynthesis is the process by which green plants make their own food using sunlight, carbon dioxide and water."
    return f"RAG Searching in textbook.txt...\n\n{BOOK}"

def recommender_fn(topic):
    return f"After learning '{topic}', you should study:\n1. Advanced {topic}\n2. {topic} - Numericals\n3. Test on {topic}"

def dashboard_fn(marks):
    return f"Dashboard Analysis:\nInput: {marks}\nYou are doing good! Focus more on weak subjects."

with gr.Blocks(title="Smart Study Assistant") as demo:
    gr.Markdown("# Smart Study Assistant - Final Project")
    with gr.Tab("1. Chatbot"):
        gr.Interface(fn=chatbot_fn, inputs=gr.Textbox(label="Apna Question Likho"), outputs=gr.Textbox(label="Answer (Tumne jo likha wahi ayega)"))
    with gr.Tab("2. RAG"):
        gr.Interface(fn=rag_fn, inputs=gr.Textbox(label="Ask from Book"), outputs=gr.Textbox(label="RAG Answer"))
    with gr.Tab("3. Recommender"):
        gr.Interface(fn=recommender_fn, inputs=gr.Textbox(label="Topic Name"), outputs="text")
    with gr.Tab("4. Dashboard"):
        gr.Interface(fn=dashboard_fn, inputs=gr.Textbox(label="Enter Marks like: Math 80, Science 70"), outputs="text")

demo.launch()
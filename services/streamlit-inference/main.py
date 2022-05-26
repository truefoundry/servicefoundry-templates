from inspect import signature, getmembers, isfunction
import gradio as gr
try:
    import ${module_name} as functions
except ImportError as error:
    print("Failed to import function ${module_name}: " + error.message)
    raise error


def get_input(param_name, annotation):
    if annotation is None:
        return gr.Textbox(label=param_name)
    elif annotation in [int, float]:
        return gr.Number(label=param_name)
    elif annotation == str:
        return gr.Textbox(label=param_name)
    else:
        raise RuntimeError(f"Unsupported type {annotation}.")


with gr.Blocks() as demo:
    with gr.Tabs():
        for name, func in getmembers(functions, predicate=isfunction):
            with gr.TabItem(name):
                sig = signature(func)
                inputs = []
                for param_name, value in sig.parameters.items():
                    text_input = get_input(param_name, value.annotation)
                    inputs.append(text_input)
                button = gr.Button("Submit")
                output = gr.Textbox(label="Output", interactive=False)
                button.click(func, inputs=inputs, outputs=[output])
                
demo.launch(server_name="0.0.0.0", server_port=7860)

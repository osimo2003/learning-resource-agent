import gradio as gr
from agent import learning_resource_agent
from google.adk.runners import InMemoryRunner
from google.adk.plugins.logging_plugin import LoggingPlugin
import asyncio

# Initialize the agent runner
runner = InMemoryRunner(agent=learning_resource_agent, plugins=[LoggingPlugin()])

# Define async function to run the agent
async def run_agent(query):
    response = await runner.run_debug(query)
    return response

# Wrap with Gradio interface
iface = gr.Interface(
    fn=lambda query: asyncio.run(run_agent(query)),
    inputs="text",
    outputs="text",
    title="Learning Resource Agent",
    description="Ask for tutorials, guides, and courses on any topic."
)

# Launch the app
iface.launch()

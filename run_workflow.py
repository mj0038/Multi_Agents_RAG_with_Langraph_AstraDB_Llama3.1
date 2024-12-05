from src.workflows.workflow import build_workflow

def main():
    """
    Run the LangGraph workflow.
    """
    print("Running the workflow...")
    workflow = build_workflow()
    inputs = {"question": "Tell me about agents"}
    outputs = workflow.run(inputs)
    print("Workflow outputs:", outputs)

if __name__ == "__main__":
    main()

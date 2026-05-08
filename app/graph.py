from langgraph.graph import StateGraph, END

from app.state import AgentState

from app.nodes import developer_node, review_node, qa_node, fix_node, report_node

## Initiate the workflow
workflow = StateGraph(AgentState)

## Adding nodes to the workflow
workflow.add_node("developer", developer_node)
workflow.add_node("review", review_node)
workflow.add_node("qa", qa_node)
workflow.add_node("fix", fix_node)
workflow.add_node("report", report_node)

## Defining the workflow entry point
workflow.set_entry_point("developer")

def qa_router(state):

    print("\n=======================================================")
    print("ROUTER Check")
    print("=======================================================")

    print("Needs fixing: ", state['needs_fix'])

    print("Iteration count: ", state['iteration_count'])

    if (state['needs_fix'] and state['iteration_count'] < 3):
        print("Routing to fix node...")
        return "fix"
    else:
        print("Routing to report node...")
        return "report"
    

## Add edges
workflow.add_edge("developer", "review")
workflow.add_edge("review", "qa")

workflow.add_conditional_edges("qa", qa_router)

workflow.add_edge("fix", "review")
workflow.add_edge("report", END)

graph = workflow.compile()
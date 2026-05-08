## Nodes:
## 1. Developer Node
## 2. Review Node
## 3. QA Node
## 4. Fix Node
## 5. Final Report Node

from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

from app.prompts import DEVELOPER_PROMPT, REVIEW_PROMPT, QA_PROMPT, FIX_PROMPT, REPORT_PROMPT

load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("API_KEY"),
    model = os.getenv("MODEL"),
    temperature= 0
)

def developer_node(state):
    print("\n ===============================================")
    print("ENTERING: DEVELOPER NODE")
    print(" ================================================")

    prompt = DEVELOPER_PROMPT.format(requirements=state['requirements'])

    result = llm.invoke(prompt)

    generated_code = result.content.strip()

    print("\n GENERATED CODE:")
    print(generated_code)

    return {
        "generated_code": generated_code
    }

def review_node(state):
    print("\n ===============================================")
    print("ENTERING: REVIEW NODE")
    print(" ================================================")

    prompt = REVIEW_PROMPT.format(generated_code=state['generated_code'])

    result = llm.invoke(prompt)

    review_feedback = result.content.strip()

    print("\n REVIEW FEEDBACK:")
    print(review_feedback)

    return {
        "review_feedback": review_feedback
    }


def qa_node(state):
    print("\n ===============================================")
    print("ENTERING: QA NODE")
    print(" ================================================")

    prompt = QA_PROMPT.format(generated_code=state['generated_code'], 
                              review_feedback=state['review_feedback'])

    result = llm.invoke(prompt)

    qa_feedback = result.content.strip()

    print("\n QA FEEDBACK:")
    print(qa_feedback)

    qa_feedback_upper = qa_feedback.upper()

    needs_fix = ("NEEDS_FIX = TRUE" in qa_feedback_upper)

    print("\n NEEDS FIX? ", needs_fix)

    return {
        "qa_feedback": qa_feedback,
        "needs_fix": needs_fix
    }

def fix_node(state):
    print("\n ===============================================")
    print("ENTERING: FIX NODE")
    print(" ================================================")

    prompt = FIX_PROMPT.format(
        requirements=state['requirements'],
        generated_code=state['generated_code'],
        review_feedback=state['review_feedback'],
        qa_feedback=state['qa_feedback']
    )

    result = llm.invoke(prompt)

    improved_code = result.content.strip()

    print("\n IMPROVED CODE:")
    print(improved_code)

    return {
        "improved_code": improved_code,
        "iteration_count": state['iteration_count'] + 1
    }

def report_node(state):
    print("\n ===============================================")
    print("ENTERING: REPORT NODE")
    print(" ================================================")

    prompt = REPORT_PROMPT.format(
        requirements=state['requirements'],
        review_feedback=state['review_feedback'],
        qa_feedback=state['qa_feedback']
    )

    result = llm.invoke(prompt)

    report = result.content.strip()

    print("\n FINAL REPORT:")
    print(report)

    return {
        "report": report
    }
DEVELOPER_PROMPT = """
Generate the clean code for the following requirements:
requirements: {requirements}
1. The code should be modular and reusable.
2. The code should be tested on multiple scenarios.
3. The code should include comments explaining the logic.
"""

REVIEW_PROMPT = """
Review the following code and provide feedback on its quality, syntax and adherence to best practices including: syntax, optimized performance, and code readability.
code: {generated_code}
"""


QA_PROMPT = """
You are a QA analyst, and your task is to analyze the following code
code: {generated_code}
based on the following feedback from the review agent
review feedback: {review_feedback}
Provide: 
1. Edge cases
2. Syntax errors
3. Logical errors
4. Missing validations
5. Failure scenarios

Finally write the output in exactly ONE of the following:
NEEDS_FIX = TRUE
OR 
NEEDS_FIX = FALSE
"""

FIX_PROMPT = """
Improve this code as a senior developer 
requirements: {requirements}
current_code: {generated_code}
review_feedback: {review_feedback}
qa_feedback: {qa_feedback}
Generate the improved code
"""

REPORT_PROMPT = """
You are a senior technical writter. your task is to generate a report based on the following information:
requirements: {requirements}
review_feedback: {review_feedback}
qa_feedback: {qa_feedback}
Generate the report that provides overall quality, improvement that are made, and final recommendations.
"""
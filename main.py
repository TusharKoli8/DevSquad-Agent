from app.graph import graph

def run():
    print("\n============ AI autonomous developer team============")

    while True:

        requirement = input("\nEnter the requirement (or 'exit' to quit): ")

        if requirement.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break

        result = graph.invoke({
            "requirements": requirement,
            "generated_code": "",
            "review_feedback": "",
            "qa_feedback": "",
            "final_report": "",
            "needs_fix": False,
            "iteration_count": 0
        })

        print("\n=================================================")
        print("FINAL STATE")
        print("=============================================")
        print(result)

if __name__ == "__main__":
    run()
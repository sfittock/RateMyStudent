def ask_questions():
    student_name = input("Please enter the student's name: ")
    student_pronoun = input("Please enter the student's pronoun (he/she/they): ")

    questions = [
        f"On a scale of 1 to 5, what is {student_name}'s attitude towards learning?",
        f"On a scale of 1 to 5, what is {student_name}'s general behaviour?",
        f"On a scale of 1 to 5, how well does {student_name} work with others?",
        f"On a scale of 1 to 5, how well does {student_name} listen and follow instructions?",
        f"On a scale of 1 to 5, how organised is {student_name}?",
    ]

    responses = [
        [
            "The student has a poor attitude towards learning.",
            "The student often demonstrates a negative attitude towards learning.",
            "The student usually demonstrates a satisfactory attitude towards learning.",
            "The student demonstrates a good attitude towards learning.",
            "The student is always highly enthusiastic about learning new things.",
        ],
        [
            "The student usually has bad behaviour in the classroom and in the playground.",
            "The student sometimes shows poor behaviour in the classroom and playground.",
            "The student mostly has good behavious in the classroom and playgorund.",
            "The student often demonstrates good behaviour in the classroom and playground.",
            "The student always demonstrates excellent behaviour in the classroom and playground.",
        ],
        [
            "The student finds it difficult to coorperatively work well with others.",
            "The student struggles to work well with others at times.",
            "The student has worked well with others at times but sometimes finds it distracting.",
            "The student enjoys working with others and is usually able to woth effectively in a group.",
            "The student works collaboratively with peers to meet shared goals.",
        ],
        [
            "The student often does not listen to the teacher and finds it hard to follow instructions.",
            "The student can find it difficult to listen to instructions and carry them out in the classroom.",
            "The student has demonstrated sufficient listening skills and mostly follows instructions.",
            "The student often uses good listening skills to understand and carryout instructions provided by the teacher.",
            "The student has consistently demonstrated excellent listening and instruction following skills.",
        ],
        [
            "The student is unorganised, which impacts on their learning.",
            "The student can be unorganised at times.",
            "The student is prompt and organised to a satisfactory level.",
            "The student is often organised.",
            "The student is well equipped with effective time management and project management skills.",
        ],
    ]

    answers = []

    for i, question in enumerate(questions):
        print(question)
        answer = input("Please enter a number from 1 to 5: ")
        while answer not in ['1', '2', '3', '4', '5']:
            print("Invalid input! Please enter a number between 1 and 5.")
            answer = input("Please enter a number from 1 to 5: ")
        answers.append((i, answer))

    print(f"\nStudent name and pronoun: {student_name} ({student_pronoun}):")

    for i, answer in answers:
        print(responses[i][int(answer) - 1])

if __name__ == "__main__":
    ask_questions()

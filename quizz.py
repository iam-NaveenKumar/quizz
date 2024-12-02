import streamlit as st

st.title("Programming Quiz")

questions = [
    "What does DRY stand for in programming?",
    "Which data structure works on a FIFO principle?",
    "What is the purpose of an algorithm?",
    "What is a variable in programming?",
    "Which of the following is a valid Python function declaration?",
    "What is the file extension for a JavaScript file?",
    "Which operator is used for exponentiation in Python?",
    "Which keyword is used to create a class in Java?",
    "What does the modulus operator (%) do?",
    "Which sorting algorithm has the best-case complexity of O(n)?",
    "Which statement is true about recursion?",
    "Which logic gate outputs true only if all inputs are true?",
    "What is the main feature of polymorphism?",
    "Which of the following is not an OOP concept?",
    "What is a constructor in OOP?",
    "Which keyword is used for inheritance in Python?",
    "What is the purpose of a breakpoint in debugging?",
    "Which command initializes a Git repository?",
    "Which of the following is an example of asynchronous programming?",
    "What does REST stand for in web development?"
]

options = [
    ("a) Don’t Repeat Yourself", "b) Debugging Reduces Yield", "c) Data Resides Yearly", "d) Dynamic Runtime Yield"),
    ("a) Stack", "b) Queue", "c) Tree", "d) Graph"),
    ("a) To style web pages", "b) To define a sequence of steps to solve a problem", "c) To compile code into machine language", "d) To execute database queries"),
    ("a) A permanent value stored in memory", "b) A placeholder for storing data values", "c) A type of error in code", "d) A programming language"),
    ("a) def myFunction:", "b) function myFunction():", "c) def myFunction():", "d) myFunction():"),
    ("a) .js", "b) .java", "c) .py", "d) .html"),
    ("a) *", "b) **", "c) ^", "d) %"),
    ("a) struct", "b) object", "c) define", "d) class"),
    ("a) Divides two numbers", "b) Returns the remainder of a division", "c) Finds the square of a number", "d) Returns the quotient of a division"),
    ("a) Bubble Sort", "b) Insertion Sort", "c) Merge Sort", "d) Quick Sort"),
    ("a) It can only be used for mathematical functions.", "b) A function calls itself to solve smaller instances of a problem.", "c) Recursion is faster than iteration in all cases.", "d) Recursion cannot be implemented in Python."),
    ("a) OR", "b) AND", "c) XOR", "d) NOT"),
    ("a) Writing methods in binary", "b) Same function name with different implementations", "c) Using only global variables", "d) Protecting data from modification"),
    ("a) Encapsulation", "b) Inheritance", "c) Abstraction", "d) Recursion"),
    ("a) A method used to destroy an object", "b) A special method called automatically when an object is created", "c) A method that initializes the compiler", "d) A method for converting objects to strings"),
    ("a) extends", "b) inherits", "c) super", "d) class"),
    ("a) To stop the program after execution", "b) To pause program execution at a specific point", "c) To increase execution speed", "d) To remove syntax errors"),
    ("a) git commit", "b) git init", "c) git push", "d) git branch"),
    ("a) A loop that processes data sequentially", "b) A function that runs in parallel without waiting for other functions", "c) Using only global variables", "d) None of the above"),
    ("a) Really Easy Syntax Testing", "b) Representational State Transfer", "c) Remote Server Transmission", "d) Random Execution Syntax Template")
]

answers = [
    "a",  # Question 1
    "b",  # Question 2
    "b",  # Question 3
    "b",  # Question 4
    "c",  # Question 5
    "a",  # Question 6
    "b",  # Question 7
    "d",  # Question 8
    "b",  # Question 9
    "b",  # Question 10
    "b",  # Question 11
    "b",  # Question 12
    "b",  # Question 13
    "d",  # Question 14
    "b",  # Question 15
    "c",  # Question 16
    "b",  # Question 17
    "b",  # Question 18
    "b",  # Question 19
    "b",  # Question 20
]

score = 0

st.write("🎉 Welcome to the Programming Quiz! 🎉")

# Loop through each question and options
for idx, question in enumerate(questions):
    st.write(f"**{idx+1}. {question}**")
    choice = st.radio("Choose an option:", options[idx], key=idx, index=None)  # Set default to None to show no option selected
    if choice:  # Check if a choice was made
        if choice.startswith(answers[idx]):
            score += 1
            st.success("Yes, you are great 🔥")
        else:
            st.error(f"Well tried but the correct answer is option {answers[idx]} 🤦‍♂️")
    st.write("\n")
st.write("____________________________________________________________________________________________________")
st.write(f"🎯 Quiz Completed! 🎯")
st.write(f"Your score: {score}/{len(questions)}")

if score == len(questions):
    st.write("Otha!! Super bruh 🥳")
elif score > len(questions)//2 and score < int(len(questions)*(3/4)):
    st.write("Nice buddy 👌")
else:
    st.write("🤦‍♂️🤦‍♂️ Can't even score some decent marks.")

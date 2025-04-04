import marimo

__generated_with = "0.12.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import hashlib
    import os

        # Title Cell
    mo.vstack([
        mo.md("# Finding and Reading Device Manuals"),
        mo.md("by Raul C. Sîmpetru @ [N² lab](https://www.nsquared.tf.fau.de/)").center(),
        mo.md("""
        Welcome! As an engineer or researcher, knowing how to find and extract information from 
        device manuals is a critical skill. In this exercise, you will:

        1. Visit a manufacturer's website to find a specific device manual
        2. Upload the manual to verify you found the correct one
        3. Extract specific information from the manual to answer questions

        This helps develop your ability to navigate technical documentation and find important 
        specifications - essential skills for working with laboratory equipment.
        """)
    ])
    return hashlib, mo, os


@app.cell
def _(mo):
    mo.vstack([
        mo.md("""
            ## OT Bioelettronica

            For this exercise, we'll be working with equipment from [OT Bioelettronica](https://otbioelettronica.it/), 
            a company that designs hardware and software for biomedical research, particularly specializing 
            in electromyography (EMG) systems.

            OT Bioelettronica produces various systems for recording and analyzing bioelectrical signals, 
            including multi-channel amplifiers, electrode arrays, and specialized software for signal processing.
            """),
            mo.image("https://otbioelettronica.it/wp-content/uploads/2023/03/logo_white-2048x628.png", 
                     width=300, style={"background-color": "#000000"}).center(),
            mo.md("""
            ### Your Task

            You need to find the user manual for their **MuoviPro** device. This manual contains 
            essential information about device specifications, setup procedures, and operational guidelines.

            1. Visit [OT Bioelettronica's website](https://otbioelettronica.it/)
            2. Navigate to find the user manual for the MuoviPro device
            3. Download the PDF manual
            4. Upload it below to verify you've found the correct document
        """)
    ])
    return


@app.cell
def _(mo):
    upload = mo.ui.file(label="Upload the MuoviPro manual PDF", kind="area")
    return (upload,)


@app.cell
def _(hashlib, mo, upload):
    if len(upload.value) == 0:
        result = mo.md("❓ Please upload the MuoviPro manual PDF")
    else:
        file_hash = hashlib.md5(upload.value[0].contents).hexdigest().upper()

        if file_hash == "20DC4246841E20DE6E474F42DD8DB3A9":
            result = mo.md("""✅ **Success!** 

                           You've found the correct manual!

                           """)
        else:
            result = mo.md(f"""
            ❌ **That doesn't appear to be the correct manual.**

            Double-check that:

            - You've downloaded the MuoviPro user manual (not another device)
            - The file downloaded properly without corruption
            """)
        pass

    mo.vstack([
        mo.md("""
            ## Upload the MuoviPro User Manual

            After downloading the manual from the manufacturer's website, upload it here to verify
            you've found the correct document.
        """),
        upload,
        result
    ])
    return file_hash, result


@app.cell
def _(mo, result):
    # Only show this section if the correct manual was uploaded
    # Create form elements for student answers
    questions = {
        "q1": mo.ui.text(label="What is the maximum sampling frequency of the MuoviPro device?"),
        "q2": mo.ui.text(label="How many input channels does the MuoviPro support?"),
        "q3": mo.ui.text(label="What is the input impedance of the device?"),
        "q4": mo.ui.text(label="What is the battery life when fully charged?"),
        "q5": mo.ui.text(label="What wireless communication protocol does the device use?")
    }

    # Create a form layout using md.batch().form()
    form = mo.md(
        f"""
        1. {questions["q1"]}
        2. {questions["q2"]}
        3. {questions["q3"]}
        4. {questions["q4"]}
        5. {questions["q5"]}
        """
    ).batch(
        **questions
    ).form()

    quiz_section = mo.vstack([
        mo.md("### Device Specification Questions"),
        mo.md("Answer the following questions based on information in the manual:"),
        form
    ])

    what_to_display = mo.md("Complete the previous step by uploading the correct manual to proceed.")

    if "Success" in result.text:
        manual_section = mo.md("""
        ## Understanding Device Specifications

        Now that you have the correct manual, it's time to explore it and find specific information.
        Review the manual carefully to answer the following questions about the MuoviPro device.
        """)

        what_to_display = mo.vstack([manual_section, quiz_section])

    what_to_display
    return form, manual_section, questions, quiz_section, what_to_display


@app.cell
def _(form, mo, questions):
    # Only evaluate if the form has been submitted
    # Updated with the correct information from the MuoviPro manual
    answers = {
        "q1": "1",       # Maximum sampling frequency
        "q2": "2",           # Number of input channels
        "q3": "3",        # Input impedance
        "q4": "4",      # Battery life
        "q5": "5"     # Wireless protocol
    }

    # Check each answer
    results = []
    score = 0

    for q, answer_field in questions.items():
        user_answer = answer_field.value.strip().lower()
        correct_answer = answers[q].lower()

        if user_answer == correct_answer:
            results.append(f"✅ Question {q[-1]}: Correct!\n")
            score += 1
        else:
            results.append(f"❌ Question {q[-1]}: Incorrect. The answer is: {answers[q]}\n")

    answers_to_display = mo.md("Fill in your answers and click 'Check Answers' to evaluate your responses.")

    if form.value:
        # Display results
        answers_to_display = mo.vstack([
            mo.md(f"### Your Score: {score}/{len(questions)}"),
            mo.md("\n".join(results)),
        ])

    answers_to_display
    return (
        answer_field,
        answers,
        answers_to_display,
        correct_answer,
        q,
        results,
        score,
        user_answer,
    )


@app.cell
def _(mo, score):
    conclusion = mo.md("")

    if score == 5: 
        conclusion = mo.md("""
        ## Congratulations!

        You've completed the exercise on finding and reading device manuals. You've practiced:

        1. Navigating a manufacturer's website to find documentation
        2. Downloading and verifying technical manuals
        3. Extracting specific technical specifications from documentation

        These skills will serve you well throughout your career when working with laboratory equipment
        and other technical devices.

        ### Bonus

        - Share any interesting insights you found in the manual that weren't covered in the questions
        """)

    conclusion
    return (conclusion,)


if __name__ == "__main__":
    app.run()

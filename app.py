from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            # Get input values
            absences = int(request.form['absences'])
            prelim_grade = float(request.form['prelim_grade'])
            quizzes_grade = float(request.form['quizzes_grade'])
            requirements_grade = float(request.form['requirements_grade'])
            recitation_grade = float(request.form['recitation_grade'])
        except ValueError:
            result = "Invalid input. Please enter valid numbers."
            return render_template('index.html', result=result)

        # Logic from the Python script
        if absences >= 4:
            result = "FAILED due to too many absences."
        else:
            # Attendance Calculation
            attendance_grade = 100 - (10 * absences)

            # Class Standing Calculation
            class_standing = (0.4 * quizzes_grade +
                              0.3 * requirements_grade +
                              0.3 * recitation_grade)

            # Prelim Grade Calculation
            prelim_calculated = (0.6 * prelim_grade +
                                 0.1 * attendance_grade +
                                 0.3 * class_standing)

            # Prepare result output
            result = f"Prelim Grade: {prelim_calculated:.2f}\n"
            for target in [75, 90]:
                result += f"\nTo achieve {target}% overall grade:\n"
                for final_grade in [0, 50, 75, 100]:
                    midterm_grade = (target - 0.2 * prelim_calculated - 0.5 * final_grade) / 0.3
                    if 0 <= midterm_grade <= 100:
                        result += f" - Midterm Grade: {midterm_grade:.2f} when Final Grade is {final_grade}\n"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

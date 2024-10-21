# Deliverable 2: Final Data Product

This week, you are required to submit a draft version of your final data product, which will take the form of a Github project repository. The submission deadline can be found in the course syllabus. Here's an overview of the deadlines:

|     | Task Description                                                                                                                                                       | Date                  | Weight |
| --- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- | ------- |
| 1   | Submit your group Github repo                    | Oct 30th 2024, 11:59 PM | 20%      |
| 2   | Review other groups repo               | Oct 30th - Nov 6th, 11:59 PM                     | 5%       |


Your submission should meet the following key requirements:
You will be using the same criteria when peer reviewing others' group projects.

### 1. **Project Structure (25%)**

- **Repository Organization**: Ensure that the structure of your Github repository follows industry standards for data science projects. You can refer to the [Cookiecutter Data Science template](https://cookiecutter-data-science.drivendata.org) as a guide.
- **Naming Conventions**: Adopt a standard file naming convention throughout the project. Use [snake_case](https://en.wikipedia.org/wiki/Snake_case) for naming folders, files, and variables in your Python scripts. This will improve readability and maintain consistency.
- **README File**: Include a well-organized README file. The README should contain:
  - A detailed description of the project, its objectives, and its scope.
  - Information on team members and their roles.
  - Clear, step-by-step instructions on how to reproduce your analysis, including how to set up the environment and run the code.

### 2. **Code Quality (25%)**

- **Code Readability and Structure**: Your code should be clear, concise, and well-formatted. Adhere to Python best practices such as the DRY (Don't Repeat Yourself) principle, ensuring that your code is modular, reusable, and avoids redundancy.
- **Modularization**: Organize your code into distinct Python scripts and functions to promote reusability and maintainability.
- **Configuration Files**: Avoid hard-coding values in your scripts. Use configuration files (e.g., YAML, JSON) to store variables and constants that are used across the codebase.
- **Version Control**: Utilize Git version control properly. Ensure that your commits are frequent, meaningful, and that the progression of your work is well-documented.

### 3. **Reproducible Environment (25%)**

- **Environment Setup**: Provide clear and thorough instructions in the README on how to set up the environment necessary to run your analysis. For instance, you can include steps to set up a `conda` environment or a `virtualenv` to ensure consistency across systems.
- **Reproduction Instructions**: In the README, provide a step-by-step guide that explains how to re-run the entire analysis from start to finish, including data loading, pre-processing, model training, and results generation. This should ensure that others can replicate your work without any confusion.

### 4. **Application of MongoDB and PySpark (25%)**

- **MongoDB Usage**: Your project should showcase meaningful applications of MongoDB’s query language. At a minimum, MongoDB should be used for data pre-processing and cleaning. Merely importing data from MongoDB into Python is insufficient. You must demonstrate how you applied MongoDB queries (e.g., `$project`, `$match`, `$group`) to transform or analyze the data as part of your workflow.
- **PySpark Usage**: Similarly, your project must integrate PySpark for data pre-processing, transformation, or feature engineering. Demonstrating the ability to manipulate large datasets using PySpark is crucial.

### 5. **Equal Group Contributions**

- **Commit History and Contributions**: Your individual contribution to the project will be assessed based on your Github commit history and the amount of code you contributed. Active participation throughout the project is essential, and your grade will be proportional to your level of contribution.
  - If your contribution is minimal (e.g., few commits), your grade for this project will reflect that.
- **Peer Evaluations**: At the end of the project, every team member will submit a peer evaluation form. This evaluation, along with your commit history, will be used to assess your individual contribution. Failure to contribute adequately to the group project can result in a failing grade.

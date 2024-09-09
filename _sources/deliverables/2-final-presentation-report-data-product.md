![](../img/591_banner.png)

# Deliverable 2: Final Presentation, Report, and Data Product

## 1. Deliverable Description

This document describes several deliverables, representing the culmination of your group's work during capstone:

1. [Final report](#2-final-report);
2. [Final presentation](#3-final-presentation);
3. [Final data product](#4-data-product);
4. (Not graded) [Presentation of project at the end-of-year celebration](#5-end-of-year-celebration-presentations). A subset of groups will give short oral presentations.
5. (Not graded) You are strongly encouraged to give a [presentation to the capstone partner's organization](#6-partner-presentation-optional-but-strongly-recommended).

Here are the general tasks involved in the final deliverable process:

|     | Task Description                                                                                                                                                    | Date                             | Graded? |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- | ------- |
| 1   | Develop the components of the [final presentation](#3-final-presentation), [final report](#2-final-report), and [data product](#4-data-product) with your group.    | -                                | -       |
| 2   | Present the final presentation to your colleagues and project mentor.                                                                                               | Thursday June 13, Friday June 14 | Yes     |
| 3   | Submit a draft final report and data product to your project mentor.                                                                                                | Wednesday June 19, 16:00         | No      |
| 4   | Revise your report and data product by incorporating feedback from your project mentor (in some cases this may involve more than one round of revisions).           | -                                | -       |
| 5   | After receiving permission from the project mentor, submit the finalized report and data product to the capstone partner and project mentor.                        | Wednesday June 26, 16:00         | Yes     |
| 6   | Prepare to share your work at the end-of-program celebration, either as an oral presentation or electronic poster (we'll let you know which groups are doing what). | -                                | -       |

## 2. Final Report

The audience of your final report is primarily your capstone partner and your faculty mentor. The purpose of the report is to:

- Convince the capstone partner that your data product indeed addresses their needs; and,
- Indicate how you used data science to address the capstone partner's needs.

Try not to confuse this report with the data product -- the data product is something that your partner is intended to _use_, whereas this report is intended to justify the usefulness of your data product.

The report should be created using a reproducible tool (e.g., Jupyter, RMarkdown or LaTeX). For examples of reproducible tools and workflows, see [here](https://pages.github.ubc.ca/MDS-2023-24/DSCI_591_capstone-proj_students/deliverables/1-proposal-presentation-and-report.html#using-a-reproducible-tool).

### 2.1. Final Report Components

Your final report should contain the following sections, and should be reported in this order:

#### Executive summary

A brief and high level summary of the project.

#### Introduction

The introduction should start broad, introducing the question being asked/problem needing solving and why it is important. Any relevant information to understand the question/problem and its importance should be included. This may be similar to the problem statement of the proposal, but it has most likely evolved at least a little.

Over the course of the project, you've refined the problem statement into tangible objectives that can be directly assessed by data science techniques. Indicate these refined tangible objectives here, along with your reasoning for why these scientific objectives are useful for addressing the capstone partner's needs. You might need to describe the available data first before outlining the scientific objectives.

#### Data science methods

Next, describe the data science techniques you used to address the scientific objectives. In your discussion, you might want to include:

- Pros and cons of using this method;
- Justification over other methods;
- An indication of a method that might work better, or improvements one could make to your techniques. Also indicate the difficulties associated with making these improvements, and why you didn't implement the improvements.
- Discuss your feature pre-processing (including feature selection if applicable), including why and how you choose to create/remove certain features.
- Discuss which metrics you are using to evaluate the model's performance and why these were chosen.
    - Include who are the stakeholders that will be affected by the model and why your metrics are important for them. Note any potential ethical concerns that you have related to any step of the model pipeline and to what extent the metrics you have chosen can mitigate these as well as explicitly notice potential ethical issues that you don't think your model is addressing and that you would keep a closer eye on as the model is deployed (this last point can be noted briefly, just to show that you are aware of the impact the model might have in bigger context where it is deployed).

#### Data product and results

Describe your data product and any relevant results obtained from it. For the description of the data product, you might want to include:

- How you intend the partner to use the data product;
- Pros and cons of using this product/interface;
- Justification over other products/interfaces;
- An indication of a product/interface that might work better, or improvements one could make to your product/interface. Also indicate the difficulties associated with making these improvements, and why you didn't implement the improvements.

The description of your data product should _not_ include an indication of how to technically use the data product, nor any other documentation to your product. Such "_how-related_" topics belong with the product itself (e.g., in the README). Rather, this final report should focus on the "_why-related_" topics to communicate the purpose of the product's existence.

#### Conclusions and recommendations

Re-state the question being asked/problem needing solving and explain how your data product answers/solves it. Comment on how well your product answered their question/solved their problem, and discuss any limitations of the product in its ability of doing so. Include in what ways your data science question might fall short of addressing the partners business/high-level problem statement. Describe recommendations for the partner to continue/improve the project in the future.

### 2.2. Evaluation

You will be evaluated based on how well you refined the capstone partner's needs into scientific objectives, how effectively your data science techniques address these scientific objectives, and the appropriateness of your data product. While the rubric above gives an idea of how aspects of your report will be weighted during evaluation, the unique context and content of each capstone project will be taken into account when grading.

You will also be evaluated according to how well you communicate the usefulness of your product and scientific objectives for addressing the capstone partner's needs. The report should convince your capstone partner (or anyone in their organization) that your product is able to address their needs, and should do so concisely (without the reader to have to spend a long time reading). If there are limitations of the product in addressing the capstone partner's needs (there usually are!) these should be clearly and honestly stated. As explanation of how these limitations could be addressed in the future should also be included.

The report should not be longer than 2500 words (excluding figures, legends, tables and references). This is an upper limit and we expect most reports to be shorter; practice expressing yourself succinctly. We recommend using an appendix or linking to GitHub/GitLab repositories if you have additional details to refer to.

## 3. Final Presentation

The audience of this presentation is your classmates/colleagues and faculty mentors (the partners will not attend). The purpose is to communicate how your data product addresses your capstone partner's needs.

The presentation does not need to be created using a reproducible tool, but certainly can be if desired.

### 3.1. Final Presentation Components

Your presentation should contain the following elements, mirroring the components of the final report:

- A brief overview of the capstone partner's needs, possibly including some background if the audience is not familiar with your application area (though always keep jargon to a minimum).
- A description of the scientific objectives you ended up pursuing to address the capstone partner's needs.
- A showcasing of the data product you developed to be delivered to the capstone partner, along with:
- A description of the data science techniques making up the data product. Describe (briefly) how the technique works, if the audience is not familiar with it. Justify why your technique is appropriate (or perhaps not appropriate) for addressing the defined objectives, along with downfalls of the technique and how you might make improvements (and why you didn't).

Remember, the presentation goal is _not_ to outline what you _did_ over the capstone course. This means that it's possible (and likely) that not all of your work will be showcased. However, this doesn't mean that you can't mention techniques that weren't fruitful -- it might be useful to mention these things when justifying your data science approach.

### 3.2 Evaluation

The presentation is worth 10% of your final grade and will be graded according to the [presentation rubric on Canvas](https://canvas.ubc.ca/courses/130316/assignments/1780237). For the presentations, we expect you to:

1. End on time.
    - Presentations are to be __22 minutes__, followed by an __8-minute__ question/feedback period.
2. Include the same components as the report.
    - The exact format is flexible and can be modified based on consultation with your mentor (for example, an executive summary isn't usually included in a presentation).
    - For the intro, start with introducing your team members and then briefly introduce what the partner organization is doing and why they are doing it (why it is important). Follow with what issue they are currently facing, and how your capstone products will add value to their organization by solving this problem (what will they be able to do with your help). Make sure to include the success criteria for your capstone products.
3. Convey the message of the proposal effectively.
    - Slides should be easy to follow and understand, ideally focusing on one purpose per slide and not contain distractions such as irrelevant content or too much text on a slide. 
    - Avoid using word-heavy charts when possible and limit the number of bullets per slide. 
    - If you add an image or a diagram, you should give importance to them in the presentation. All the images and diagrams should be added for a reason.
    - Include a clear take-home message per slide, possibly as the slide title.
    - If a particular slide needs to be more busy, use animations to focus the audience attention on one concept at a time.
4. Use visual elements to help convey important messages.
    - This includes schematics and charts that are easy to read and digest.
    - The overall presentation design should also be visually appealing.
5. Gear your presentation towards the audience.
    - The audience of your presentation is the MDS mentors and your colleagues/classmates. The partner organizations will not be present.
    - Make your presentations accessible to everyone in the audience by using:
        - Effective color schemes with good contrast consistently throughout the presentation. For example, avoid using green and red to represent different values since these colors are hard to distinguish for many people.
        - Large enough font sizes, including on chart labels.
        - Appropriate speaking volume (often 10-20% louder than you think).
        - Effective & inclusive language choices. This includes explaining and limiting the use of jargon (your audience doesn't share your domain-specific project background), and using jargon in context so the audience does not need to constantly re-remember its definition. This also includes avoiding using expressions such as "Thanks guys" unless presenting to a solely male audience (you can use "Thanks everyone" or "Thank you all for listening" instead).
        - Include slide numbers so that it is easy to refer back to a slide during the Q&A.
6. Display excellent presentation skills.
    - Speaking clearly and audibly;
    - Engaging the audience with body language and eye contact.
    - Answer questions directly instead of trying to deflect/answer something else. Check with the question asker if you answered them in a satisfactory manner.
7. Be active during the presentation and the following discussion.
    - Each member needs to spend an equal amount of time presenting, and each needs to answer roughly the same amount of questions.
    - During Q&A there's no need to answer immediately; look at your teammates so you aren't stepping over each other trying to answer. Sometimes a single reply is enough, not everyone needs to answer the same question. If you do not know how to answer a question, look to your teammates to see if someone else might be able to, rather than starting to talk about something else just for the sake of saying something.

While the rubric and guidelines above gives an idea of how aspects of your presentation will be weighted during evaluation, the unique context and content of each capstone project will be taken into account when grading.

### 3.3. Confidentiality

For those who have entered into confidentiality agreements with your capstone partners, you will need to give the partner an opportunity to approve the slides before presenting them to your classmates. This means you will need to have your slides finished a few business days before the presentation. You may want to let the partner know that this is coming, so that they can set aside some time to look at your work and hopefully reduce the turnaround time required.

### 3.4. Peer-review activity
- Each student will be assigned 3-4 presentations for peer review. You will fill out the presentation rubric on Canvas and provide written feedback for the group that you are assigned to. 
- Peer review is worth 10% of your final presentation grade.
- Peer review activity is to be completed individually 

| 100%                                                                            | 75%                                                                                 | 50%                                                | 25%                              | 0%                                              |
|---------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|----------------------------------------------------|----------------------------------|-------------------------------------------------|
| Fill out the rubric with constructive feedback, asking questions during Q and A | Fill out the rubric with detailed comments, but most were not-constructive comments | Fill out rubric with short/unconstructive comments | Fill out rubric with no comments | Did not fill out rubric nor asking any question |

## 4. Data Product

As a group, you will deliver a data product to your capstone partner that addresses their questions/problems/needs. This is something that is meant to be _used_ in some way.

The data product will be evaluated based on its usefulness to the client, accuracy, ease of use, readability, and interpretability. The product is expected to be packaged in a way that makes it reproducible. The exact tools for reproducibilty depend on the type of product, but all data products should **at a minimum** include a GitHub/GitLab repository containing all code necessary to recreate and test the data product, as well as a list of all software and environment dependencies (names and versions) required to create and use the data product. It should also be very well documented so that it can be both used by the client and extended by other data scientists in the future.  

The grading scheme for your data product will be developed with your mentor. This helps take into account the uniqueness of each capstone project, helps the student team set goals for their product, and provides transparency in what constitutes the data product and how the mentor will grade it.

### 4.1. Expectations

- You will use a project board to transparently manage the project.
- You will have a Code of Conduct and a Contributing file in the root of the project's repo.
- You will work in a branch-pull request fashion, where master is protected (if your tooling allows for that) and someone other than the pull request creator reviews and merges the pull request. Code should be pushed to the branch being worked on at the end of every work session.
- Code should follow the DRY principle, and there should be unit tests for every function.
- Code is reproducible from end-to-end and from machine-to-machine.
- All project-related communications that have implications related to decisions about the project should be linked to the project via issues.

## 5. End-of-year Celebration Presentations

After the final presentations, you (the MDS cohort) will rate each of the groups presentations. A small number of groups with the most highly rated presentations will be invited to give short oral presentations at the end-of-year celebration. The audience will include faculty members from the departments of statistics and computer science and capstone partners. This presentation will __not be graded__. Once again, groups with confidentiality agreements will need to have their presentation materials approved in advance; this is especially important here as the presentations/e-posters will be viewed by a wider public audience.

## 6. Partner Presentation (optional, but strongly recommended)

You may also wish to give a presentation at your capstone partner's facility to present your data science approach and data product to their organization's members. We highly recommend doing this, as it allows you to network, showcase your skills to people outside of UBC, and to potentially have a bigger impact in their organization. Ask your capstone partner if this can be arranged. Even if you do this presentation, let your capstone partner know that they are still welcome to attend the UBC end-of-program presentations.

This presentation will __not be graded__, although your mentor may want to attend as well. What you present is up to you, but you probably shouldn't make it identical to your UBC presentation. Keep the following in mind:

- __The message you want to get across__. In most cases, the main purpose is to show how your work can impact their organization. Don't just focus on the results, though -- you need to build trust that your method is more than magic, by explaining _in plain language_ how your approach works (you can be more technical in your UBC presentation). As in all presentations, you should _not_ just run through all the things you _did_ during the project, rather construct your message and select things that you did to back up your message.
- __Who the audience is__. Your audience probably knows a lot about the organization and terminology in their field, so you don't need to go over that. They also are probably not all data scientists, so don't use any data science jargon (you can use data science jargon in your UBC presentation).

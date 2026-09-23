# CareerDash

CareerDash is a job application tracker that I built using Python, Flask, and SQLite.

I came up with the idea because I've been applying to a lot of internships and IT positions, and I wanted a better way to keep track of where I've applied and what stage each application is in. I didn't want to have to go to each company's website and log in just to view the status of my applications. I wanted a dashboard where I could see everything in one place.

This project has also been a way for me to get more hands-on experience with Python, databases, and web development.

## CareerDash Dashboard

![CareerDash Dashboard](images/careerdash-dashboard.png)

## What It Does

Right now, CareerDash allows me to:

- Add new job applications
- Edit applications I've already added
- Delete applications
- Track the status of an application which could be: Applied, Interview, Offer, or Rejected
- See dashboard statistics for my applications
- Search by company or position
- Filter applications by status

All of the application information is stored in a SQLite database, so the data stays saved even after closing the application.

## What I Used

I built CareerDash with:

- Python
- Flask
- SQLite
- HTML
- CSS
- Jinja2


## What I've Learned

Building CareerDash has helped me get more comfortable working with Flask and understanding how the frontend, backend, and database work together.

I've also gotten hands-on experience with CRUD operations, SQL queries, routing, HTML templates, forms, and taking user input and using it to interact with a database.

## What's Next

As a computer science student, I've faced the same issues and frustrations as many others trying to break into the industry. The job market is rough, and sometimes filling out application after application while keeping track of everything, learning new skills, working, and trying not to fall behind can feel impossible.

My goal with CareerDash is to make that process much easier. I don't want us newcomers to have to spend hours every week manually filling out 20 different applications and then trying to remember where we applied and what stage each application is in.

Eventually, I want CareerDash to be more than just a dashboard. I want to build an AI assistant that can help automate some of the most repetitive parts of the job search while still keeping the user in control.

Some of the features I want to work toward include:

- An AI assistant that can find jobs based on what the user is looking for
- Helping users complete job applications without having to manually enter the same information over and over
- Automatically adding submitted applications to the CareerDash dashboard
- Allowing users to upload and store multiple resumes on their account
- Comparing a user's resume with a job description before they apply
- Tailoring a copy of the user's resume to a specific job description while keeping their actual experience and qualifications accurate
- Saving different versions of a resume and tracking which version was used for each application
- Automatically updating application statuses when possible
- User accounts so CareerDash can eventually be used by more than one person

The bigger goal is to give people more of their time back. I want us to have the time and energy to keep learning while still working toward professional experience. At the end of the day, I think what's most important is having the opportunity to learn and then being able to put that knowledge to the test.

## Running CareerDash

To run the project locally:

1. Clone the repository.
2. Install Flask:

   `pip install flask`

3. Run:

   `python app.py`

4. Open:

   `http://127.0.0.1:5000`
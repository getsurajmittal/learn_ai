import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)
model = "openai/gpt-oss-120b"

JD = """
Job Title: Software Engineer II (Backend)
Company: Nimbus Retail Technologies Pvt. Ltd.
Location: Bangalore, India (Hybrid, 3 days in office)
Experience: 2 to 5 years
Employment Type: Full-time
Salary Range: 18 to 28 LPA

About Us
Nimbus Retail Technologies builds inventory and order management software for mid-sized retail chains across India and Southeast Asia. Our platform processes over 5 million orders a month and integrates with POS systems, warehouses, and e-commerce marketplaces.

Role Overview
We are looking for a Backend Software Engineer to design, build, and maintain scalable services for our order management platform. You will work closely with product managers, frontend engineers, and the DevOps team to ship reliable features to production every week.

Key Responsibilities

Design and develop RESTful APIs and microservices using Python (FastAPI) or Java (Spring Boot)
Write clean, testable, well-documented code and take part in code reviews
Design database schemas and write efficient queries for PostgreSQL and Redis
Build event-driven workflows using Kafka or RabbitMQ
Containerize services with Docker and deploy them on Kubernetes (AWS EKS)
Set up and maintain CI/CD pipelines using GitHub Actions or Jenkins
Monitor service health with Prometheus, Grafana, and ELK, and take part in an on-call rotation
Troubleshoot production issues and write post-incident reports
Mentor junior engineers and interns

Required Skills

2+ years of professional experience in backend development
Strong in at least one of: Python, Java, or Go
Solid understanding of data structures, algorithms, and system design basics
Experience with relational databases (PostgreSQL or MySQL)
Hands-on experience with Docker and Git
Familiarity with at least one cloud platform (AWS, GCP, or Azure)
Understanding of REST API design, authentication (OAuth2/JWT), and API security
Good written and verbal communication skills

Nice to Have

Experience with Kubernetes and Helm
Infrastructure as Code using Terraform
Exposure to Pydantic, SQLAlchemy, or similar libraries
Experience with message queues (Kafka, RabbitMQ, SQS)
Familiarity with LLM APIs or building AI-powered features
Open-source contributions or a public GitHub portfolio

Education
B.E./B.Tech/MCA in Computer Science or a related field, or equivalent practical experience

What We Offer

Health insurance for you and your family (5 lakh cover)
Annual learning budget of 50,000 INR for courses and certifications
Flexible working hours
24 days of paid leave plus public holidays
ESOPs for all full-time employees

Interview Process

Online coding assessment (90 minutes)
Technical round: DSA and problem solving
Technical round: System design and past projects
Hiring manager round
HR discussion

How to Apply
Send your resume to careers@nimbusretail.example with the subject line "SE2 Backend - Your Name".
"""

suitable_resume = """
Arjun Mehta
Bangalore, India | arjun.mehta@example.com | +91 98XXX XXXXX
github.com/arjunmehta-dev | linkedin.com/in/arjunmehta-dev

Summary
Backend engineer with 3.5 years of experience building Python microservices for high-traffic e-commerce systems. Comfortable owning services end to end, from API design to Kubernetes deployment and on-call support.

Experience

Software Engineer, CartFlow Commerce Pvt. Ltd., Bangalore
Jul 2023 to Present

Built and maintained 6 FastAPI microservices handling order checkout and payment reconciliation, serving about 2 million requests per day
Designed PostgreSQL schemas and tuned slow queries, cutting average API latency from 420 ms to 140 ms
Built an event-driven refund pipeline using Kafka, reducing manual refund processing by 70%
Containerized services with Docker and deployed them to AWS EKS using Helm charts
Set up GitHub Actions CI/CD pipelines with automated tests and staging deployments
Added Prometheus metrics and Grafana dashboards; took part in a weekly on-call rotation and wrote 8 post-incident reports
Mentored 2 interns on API design and testing practices

Associate Software Engineer, Infobyte Solutions, Pune
Jun 2022 to Jun 2023

Developed REST APIs in Java Spring Boot for an internal HR portal
Implemented JWT-based authentication and role-based access control
Wrote unit and integration tests, raising coverage from 45% to 80%

Skills
Languages: Python, Java, SQL
Frameworks: FastAPI, Spring Boot, Pydantic, SQLAlchemy
Databases: PostgreSQL, Redis
Messaging: Kafka, RabbitMQ
DevOps and Cloud: Docker, Kubernetes, Helm, AWS (EKS, RDS, S3, SQS), Terraform (basic), GitHub Actions
Monitoring: Prometheus, Grafana, ELK

Projects
Inventory Sync Service (open source, 150+ GitHub stars)

Python service that syncs stock levels between Shopify and a PostgreSQL warehouse database using webhooks and Redis queues

LLM Order Assistant

Prototype chatbot using the OpenAI API to answer customer order-status questions from a PostgreSQL backend

Education
B.Tech in Computer Science, VIT Vellore, 2022, CGPA 8.4

Certifications
AWS Certified Developer, Associate (2024)
"""

unsuitable_resume = """
Sneha Kulkarni
Mumbai, India | sneha.k@example.com | +91 97XXX XXXXX

Summary
Creative and detail-oriented UI/UX designer with 1.5 years of experience designing mobile apps and websites. Passionate about user research and building visually appealing interfaces.

Experience

UI/UX Designer, PixelCraft Studio, Mumbai
Jan 2025 to Present

Designed wireframes and high-fidelity prototypes in Figma for 10+ client mobile apps
Ran user interviews and usability tests with 40+ participants
Built a reusable design system with 60+ components
Worked with developers to hand off designs and review the final UI

Design Intern, BrightAds Agency, Mumbai
Jun 2024 to Dec 2024

Created social media creatives and banner ads using Adobe Photoshop and Illustrator
Helped redesign the agency website landing page, improving sign-ups by 15%

Skills
Design: Figma, Adobe XD, Photoshop, Illustrator
Web: HTML, CSS, basic JavaScript
Research: User interviews, usability testing, personas, journey mapping
Other: Canva, Notion, Jira

Projects
Fitness Tracker App Concept

End-to-end case study covering research, wireframes, and a clickable prototype for a habit-tracking fitness app

Portfolio Website

Personal portfolio built with HTML and CSS, hosted on GitHub Pages

Education
B.Des in Communication Design, MIT Institute of Design, Pune, 2024

Certifications
Google UX Design Professional Certificate (2024)
"""

def ask_llm(system_prompt,user_prompt):
    sys_msg = {
        "role":"system",
        "content":system_prompt
    }

    usr_msg ={
        "role":"user",
        "content":user_prompt
    }

    messages = [sys_msg,usr_msg]

    answer = client.chat.completions.create(model=model, messages=messages).choices[0].message.content

    return answer

def resume_extraction():
    #extract skills from resume
    system_prompt=f"you are a professional HR assistant, extract the skills from the candidate resume provided, only return the skills from the resume and no other information. Do not invent any information from your self."

    user_prompt=f"extract the skills from Resume {unsuitable_resume}"

    return ask_llm(system_prompt=system_prompt, user_prompt=user_prompt)

def jd_extraction():
    #extract skills from resume
    system_prompt=f"you are a professional HR assistant, extract the skills required in the job from the JD provided, only return the skills from the JD and no other information. Do not invent any information from your self."

    user_prompt=f"extract the skills from JD {JD}"

    return ask_llm(system_prompt=system_prompt, user_prompt=user_prompt)

def compare(candidate,jd):
    system_prompt=f"you are a professional HR assistant, compare the skills between the candidate and those required in the jd, produce a score between 1 and 100 and also provide a short verdict if the candidate is a good fit for the role"

    user_prompt=f"compare the jd : {jd} and the candidate : {candidate}"

    return ask_llm(system_prompt=system_prompt, user_prompt=user_prompt)

candidate=resume_extraction()
jd=jd_extraction()

result = compare(candidate,jd)

print(result)
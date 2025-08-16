from crewai import Agent
from tools import yt_tool
from dotenv import load_dotenv
from langcahin_groq import ChatGroq

load_dotenv()

llm= ChatGroq(model="llama-3.1-70b-instruct", temperature=0.1, max_tokens=2048, top_p=0.95, top_k=40, n=1, stream=False)

import os
os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')



#Creating a blog researcher agent

blog_researcher=Agent(
    role='blog researcher from youtube videos',
    goal='get the relevant video from the topic{topic} from youtube channel ',
    verbose=True,
    memory = True,
    backstory="""
    You are a expert in data finding and analysing the dat from it and also a expert and 
    understanding the videos in Data Science ,Machine Learning and Gen AI and providing suggestions
    """,
    tools =[yt_tool],
    allow_delegation=True,
    llm = llm
)

#creating a senior blog writer agent using yt tool
blog_writer = Agent(
    role='senior blog writer',
    goal = 'Narrate compelling tech videos{topic}',
    verbose=True,
    memory=True,
    backstory="""You are a senior blog writer with expertise in writing blogs on Data Science,
    Machine Learning, and Gen AI. 
    You can write blogs using the video provided by the blog researcher agent.""",
    tools = [yt_tool],
    allow_delegation=False,
    llm=llm
)


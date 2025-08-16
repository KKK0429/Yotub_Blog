from crewai import Crew , Process
from agents import blog_researcher, blog_writer
from tasks import research_task, write_task

crew= Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[research_task, write_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True,
)

##start executionprocess with enhanced feedback
result=crew.kickoff(input={'topic': 'AI vs Data Science vs ML vs DEep learning'})
print(result)
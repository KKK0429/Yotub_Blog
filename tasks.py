from crewai import Task
from tools import yt_tool
from agents import blog_researcher,blog_writer


##Research Task
research_task = Task(
    description="Research on the topic {topic} using YouTube videos"
    "Get detailed info from the channel and provide it to the blog writer",

    expected_output="Detailed research bullet point notes with introduction and a conclusion on the topic {topic} of video content",
    tools=[yt_tool],
    agents=blog_researcher,
)



write_task = Task(
    description="Write a blog post based on the research provided by the blog researcher agent",
    expected_output="A well-structured blog post on the topic {topic} with an engaging introduction, detailed content with bullet points and make sure whatevr info is it is actually accurate from video, and a conclusion",
    tools=[yt_tool],
    agents=blog_writer,
    async_execution=False,
    output_file="new-blog_post.md"
)
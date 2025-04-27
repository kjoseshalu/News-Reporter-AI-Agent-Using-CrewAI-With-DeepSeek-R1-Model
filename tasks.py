from crewai import Task
from tools import tool
from agents import news_researcher, news_writer

#research task
research_task = Task(
    description=(
    "Identify the next big trend in {topic}"
    "foucus on identifying pros and cons and the overall narrative."
    "Your final report shoukd clearly articulate key points,"
    "its market opportunities, and potential risks."
),
    expected_output='A comprehensive 3 paragraphs long report on the latest AI trends.',
    tools=[tool],
    agent=news_researcher,
)

# writing task with language model configuration
write_task = Task(
    description=(
    "Compose an insightful article on  {topic}"
    "foucus on the latesh trends and how it's impacting the industry."
    "This article should be easy to understand, engaging, and positive."
    ),
    expected_output='A 4 paragraph article on {topic} advancementsformatted as markdown.',
    agent=news_writer,
    tools=[tool],
    async_execution=False,
    output_file='output-file.md'
)

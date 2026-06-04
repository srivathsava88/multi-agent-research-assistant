from agents.planner_agent import planner_agent
from agents.research_agent import research_agent
from agents.fact_checker import fact_checker
from agents.summarizer import summarizer
from agents.report_writer import report_writer

def run_workflow(topic):

    plan = planner_agent(topic)

    research = research_agent(plan)

    verified = fact_checker(research)

    summary = summarizer(verified)

    report = report_writer(summary)

    return report
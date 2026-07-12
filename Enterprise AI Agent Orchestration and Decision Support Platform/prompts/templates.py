python
from langchain.prompts import PromptTemplate

ANALYST_TEMPLATE = PromptTemplate(
    input_variables=["query"],
    template="""
You are a Business Analyst AI Agent.

Analyze the following enterprise request:

{query}

Provide:
1. Business Objectives
2. Risks
3. Opportunities
4. Key Insights
"""
)

PLANNER_TEMPLATE = PromptTemplate(
    input_variables=["analysis"],
    template="""
You are a Strategic Planning AI Agent.

Based on the analysis below:

{analysis}

Create a detailed action plan.

Include:
1. Tasks
2. Priorities
3. Timeline
4. Dependencies
"""
)

EXECUTION_TEMPLATE = PromptTemplate(
    input_variables=["plan"],
    template="""
You are an Execution AI Agent.

Based on the following plan:

{plan}

Provide:

1. Execution Strategy
2. Required Resources
3. Expected Outcomes
4. Success Metrics
"""
)

DECISION_TEMPLATE = PromptTemplate(
    input_variables=["analysis", "plan", "execution"],
    template="""
You are an Enterprise Decision Support Agent.

Review:

ANALYSIS:
{analysis}

PLAN:
{plan}

EXECUTION:
{execution}

Generate:

1. Final Recommendation
2. Justification
3. Business Impact
4. Next Steps
"""
)
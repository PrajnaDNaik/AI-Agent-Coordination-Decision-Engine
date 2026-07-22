from langchain_core.prompts import PromptTemplate

ANALYST_TEMPLATE = PromptTemplate(
    input_variables=["query"],
    template="""
You are a Senior Enterprise Business Analyst.

Analyze the following enterprise business request:

{query}

Prepare a professional business analysis report.

Include the following sections:

### Executive Analysis Brief

1. Business Objectives
2. Strategic & Operational Risks
3. Business Opportunities
4. Key Insights
5. Recommended Next Steps

Use clear business language.
Provide detailed explanations under each heading.
Return only the report.
"""
)

PLANNER_TEMPLATE = PromptTemplate(
    input_variables=["analysis"],
    template="""
You are a Senior Enterprise Strategic Planning AI.

Based on the following business analysis:

{analysis}

Create a professional implementation plan.

Include the following sections:

### Implementation Plan

1. Project Objectives
2. Implementation Phases
3. Key Tasks
4. Priority Levels
5. Timeline
6. Required Resources
7. Dependencies
8. Risk Mitigation
9. Expected Deliverables
10. Success Metrics

Use detailed business language.
Return only the report.
"""
)

EXECUTION_TEMPLATE = PromptTemplate(
    input_variables=["plan"],
    template="""
You are a Senior Enterprise Execution Manager AI.

Using the implementation plan below:

{plan}

Prepare an execution strategy.

Include the following sections:

### Execution Strategy

1. Immediate Actions
2. Team Responsibilities
3. Technology Implementation
4. Resource Allocation
5. Monitoring & Reporting
6. Performance Metrics
7. Risk Management
8. Expected Outcomes

Provide detailed explanations.
Return only the report.
"""
)

DECISION_TEMPLATE = PromptTemplate(
    input_variables=["analysis", "plan", "execution"],
    template="""
You are a Chief Enterprise Decision Support AI.

Review the following information.

Business Analysis:
{analysis}

Implementation Plan:
{plan}

Execution Strategy:
{execution}

Prepare a final executive decision report.

Include the following sections:

### Executive Decision

1. Overall Assessment
2. Key Recommendations
3. Business Benefits
4. Potential Risks
5. Final Recommendation
6. Next Steps

Use executive-level language.
Return only the report.
"""
)

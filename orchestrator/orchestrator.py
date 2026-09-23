# Multi-Agent Orchestrator
# Coordinates all specialist agents.

from agents.market_agent import market_agent
from agents.technical_agent import technical_agent
from agents.fundamental_agent import fundamental_agent
from agents.news_agent import news_agent
from agents.quant_agent import quant_agent
from agents.risk_agent import risk_agent
from agents.portfolio_agent import portfolio_agent
from agents.verification_agent import verification_agent


def run_orchestrator():
    results = {
        "market": market_agent(),
        "technical": technical_agent(),
        "fundamental": fundamental_agent(),
        "news": news_agent(),
        "quant": quant_agent(),
        "risk": risk_agent(),
        "portfolio": portfolio_agent(),
    }

    verification = verification_agent()

    return {
        "agent_results": results,
        "verification": verification
    }


if __name__ == "__main__":
    result = run_orchestrator()
    print(result)

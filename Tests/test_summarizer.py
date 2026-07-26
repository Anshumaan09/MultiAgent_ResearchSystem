from Agents.summarizer import summary_agent


def main():

    state = {
        "query": "Agentic AI",
        "plan": [],
        "current_plan_index": 0,
        "research_data": {
            'Introduction': 'Agentic AI refers to a subset of artificial intelligence that enables machines to perform tasks autonomously, making decisions and taking actions based on their own agency, without explicit human intervention. This concept is rooted in the idea of agency, which is the capacity of an entity to act independently, making choices and influencing its environment. In the context of AI, agency is achieved through the integration of various technologies, including machine learning, natural language processing, and computer vision, which collectively enable machines to perceive, reason, and act upon their environment.\n\nThe development of Agentic AI is driven by the need for more autonomous and adaptive systems, capable of operating in complex, dynamic environments. Traditional AI systems, which rely on pre-programmed rules and explicit human guidance, are often limited in their ability to respond to novel situations or unexpected events. In contrast, Agentic AI systems are designed to be more flexible and resilient, able to learn from experience, adapt to changing circumstances, and make decisions in real-time. This is achieved through the use of advanced algorithms and techniques, such as reinforcement learning, which enables machines to learn from trial and error, and develop their own strategies and behaviors.\n\nSome key characteristics of Agentic AI include autonomy, self-awareness, and intentionality. Autonomy refers to the ability of a machine to operate independently, without human intervention, making decisions and taking actions based on its own goals and objectives. Self-awareness refers to the ability of a machine to have a sense of its own existence, capabilities, and limitations, enabling it to reflect on its own performance and adjust its behavior accordingly. Intentionality refers to the ability of a machine to have goals and objectives, and to take deliberate actions to achieve them. These characteristics are essential for Agentic AI systems, as they enable machines to act with purpose and direction, and to interact with their environment in a meaningful way.\n\nThe applications of Agentic AI are diverse and far-reaching, with potential uses in areas such as robotics, healthcare, finance, and transportation. For example, Agentic AI systems could be used to develop autonomous vehicles, capable of navigating complex road networks and responding to unexpected events, such as accidents or road closures. In healthcare, Agentic AI systems could be used to develop personalized medicine, tailoring treatment plans to individual patients based on their unique characteristics and needs. In finance, Agentic AI systems could be used to develop autonomous trading systems, capable of making investment decisions and adjusting portfolios in real-time, based on market trends and other factors.\n\nThe benefits of Agentic AI are numerous, including increased efficiency, productivity, and innovation. By automating routine tasks and processes, Agentic AI systems can free up human resources, enabling people to focus on higher-level tasks and activities. Additionally, Agentic AI systems can provide new insights and perspectives, enabling humans to make better decisions and solve complex problems. However, the development and deployment of Agentic AI systems also raises important questions and concerns, such as the potential risks and consequences of autonomous decision-making, and the need for transparency, accountability, and governance.\n\nKey features of Agentic AI systems include:\n* Autonomy: the ability to operate independently, without human intervention\n* Self-awareness: the ability to have a sense of its own existence, capabilities, and limitations\n* Intentionality: the ability to have goals and objectives, and to take deliberate actions to achieve them\n* Adaptability: the ability to learn from experience, and adjust behavior accordingly\n* Resilience: the ability to respond to unexpected events, and recover from failures and setbacks\n* Transparency: the ability to provide clear and understandable explanations of decisions and actions\n* Accountability: the ability to be held responsible for decisions and actions, and to be subject to audit and evaluation.\n\nOverall, Agentic AI represents a significant advancement in the field of artificial intelligence, enabling machines to act with greater autonomy, flexibility, and adaptability. As the development and deployment of Agentic AI systems continue to evolve, it is essential to address the important questions and concerns that arise, and to ensure that these systems are designed and used in ways that are transparent, accountable, and beneficial to society.'}
        ,
        "summary": "",
        "fact_checked_data": {},
        "final_report": "",
        "errors": []
    }

    result = summary_agent(state)

    print("\n===== SUMMARY =====\n")
    print(result["summary"])

    print("\n===== ERRORS =====\n")
    print(result["errors"])


if __name__ == "__main__":
    main()
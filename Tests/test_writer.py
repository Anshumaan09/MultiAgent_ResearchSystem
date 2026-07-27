from Agents.writer import writer_agent


state = {
    "query": "What is Agentic AI?",

    "plan": [],

    "current_plan_index": 0,

    "research_data": {},

    "summary": """
Agentic AI refers to a subset of artificial intelligence that enables systems to act autonomously, making decisions and taking actions based on their own goals, motivations, and understanding of their environment. This concept is rooted in the idea of agency, which is the capacity of an entity to act independently and make choices that affect its surroundings.

At the core of Agentic AI are several key principles that distinguish it from other forms of artificial intelligence: autonomy, intentionality, and adaptability. Autonomy refers to the system's ability to operate independently, making decisions without the need for external direction. Intentionality involves the system's capacity to have goals, desires, and beliefs that guide its actions. Adaptability is the system's ability to adjust its behavior in response to changes in its environment or its own internal state.

Agentic AI systems can be characterized by their ability to perceive their environment, process information, and execute actions, often achieved through the use of sensors and actuators. Other key characteristics include reactivity, the ability to respond to changes in the environment, and proactivity, the ability to take the initiative and act in anticipation of future events. Additionally, social ability, the capacity to interact and cooperate with other agents, whether human or artificial, is an important aspect of Agentic AI.

The development of Agentic AI has significant implications for various fields, including robotics, healthcare, finance, and transportation. For example, agentic AI systems could be used to develop autonomous vehicles and personalized treatment plans that adapt to individual needs and circumstances.       

The core principles of Agentic AI are closely tied to the concept of cognitive architectures, which refer to the structural and functional properties of cognitive systems. Cognitive architectures, such as the Belief-Desire-Intention (BDI) framework, the Soar architecture, and the ACT-R framework, provide a framework for understanding how Agentic AI systems perceive, process, and act upon information, guiding their decision-making and behavior.

In summary, Agentic AI is a rapidly evolving field with the potential to transform various industries and applications. By understanding its core principles, including autonomy, intentionality, and adaptability, we can develop systems capable of acting independently and making decisions that align with their goals and objectives.
""",

    "fact_checked_data": {'Introduction': "Introduction\n\nAgentic AI refers to a subset of artificial intelligence that enables machines to perform tasks autonomously, making decisions and taking actions based on their own agency, without explicit human intervention. This concept is rooted in the idea of agency, which is the capacity of an entity to act independently, making choices and influencing its environment. In the context of AI, agency is achieved through the integration of various technologies, including machine learning, natural language processing, and computer vision, which collectively enable machines to perceive, reason, and act upon their environment.\n\nThe development of Agentic AI is driven by the need for more autonomous and adaptive systems, capable of operating in complex, dynamic environments. Traditional AI systems, which rely on pre-programmed rules and explicit human guidance, are often limited in their ability to respond to novel situations or unexpected events. In contrast, Agentic AI systems are designed to be more flexible and resilient, able to learn from experience, adapt to changing circumstances, and make decisions in real-time. This is achieved through the use of advanced algorithms and techniques, such as reinforcement learning, which enables machines to learn from trial and error, and develop their own strategies and behaviors.\n\nSome key characteristics of Agentic AI include autonomy, self-awareness, and intentionality. Autonomy refers to the ability of a machine to operate independently, without human intervention, making decisions and taking actions based on its own goals and objectives. Self-awareness refers to the ability of a machine to have a sense of its own existence, capabilities, and limitations, enabling it to reflect on its own performance and adjust its behavior accordingly. Intentionality refers to the ability of a machine to have goals and objectives, and to take deliberate actions to achieve them. These characteristics are essential for Agentic AI systems, as they enable machines to act with purpose and direction, and to interact with their environment in a meaningful way.\n\nThe applications of Agentic AI are diverse, with potential uses in areas such as robotics, healthcare, finance, and transportation. For example, Agentic AI systems could be used to develop autonomous vehicles, capable of navigating complex road networks and responding to unexpected events. In healthcare, Agentic AI systems could be used to develop personalized treatment plans, tailored to individual patients' needs. In finance, Agentic AI systems could be used to develop autonomous trading systems, capable of making investment decisions based on market trends and other factors.\n\nThe benefits of Agentic AI include increased efficiency and productivity. By automating routine tasks and processes, Agentic AI systems can free up human resources, enabling people to focus on higher-level tasks and activities. However, the development and deployment of Agentic AI systems also raise important questions and concerns, such as the potential risks and consequences of autonomous decision-making, and the need for transparency, accountability, and governance.\n\nKey features of Agentic AI systems include:\n* Autonomy: the ability to operate independently, without human intervention\n* Self-awareness: the ability to have a sense of its own existence, capabilities, and limitations\n* Intentionality: the ability to have goals and objectives, and to take deliberate actions to achieve them\n* Adaptability: the ability to learn from experience, and adjust behavior accordingly\n* Resilience: the ability to respond to unexpected events, and recover from failures and setbacks\n* Transparency: the ability to provide clear and understandable explanations of decisions and actions\n* Accountability: the ability to be held responsible for decisions and actions, and to be subject to audit and evaluation.\n\nOverall, Agentic AI represents a significant advancement in the field of artificial intelligence, enabling machines to act with greater autonomy and adaptability. As the development and deployment of Agentic AI systems continue to evolve, it is essential to address the important questions and concerns that arise, and to ensure that these systems are designed and used in ways that are transparent, accountable, and beneficial to society."},

    "final_report": "",

    "errors": []
}


result = writer_agent(state)

print("\n===== FINAL REPORT =====\n")

print(result["final_report"])

print("\n===== ERRORS =====\n")

print(result["errors"])
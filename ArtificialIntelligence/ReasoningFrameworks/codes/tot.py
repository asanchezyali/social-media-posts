from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

# ToT prompt with multiple solution paths
tot_prompt = PromptTemplate(
    input_variables=["question"],
    template="""
    Question: {question}
    Let's explore multiple approaches:
    1. Approach 1: [First potential solution]
    2. Approach 2: [Alternative solution]
    3. Evaluation: [Compare approaches]
    """
)

# Higher temperature for creative exploration
llm = OpenAI(temperature=0.7)
chain = LLMChain(llm=llm, prompt=tot_prompt)

# Example: "What's the best way to reduce energy consumption in a home?"
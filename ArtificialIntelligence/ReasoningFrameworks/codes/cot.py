from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI

# Optimized CoT prompt 
cot_prompt = PromptTemplate(
    input_variables=["question"],
    template="""
    Question: {question}
    To solve this, I will break it down into steps:
    1. Identify key components of the question.
    2. Apply reasoning to each component.
    3. Combine results for final answer.
    """
)

# Lower temperature for precision in calculations
llm = OpenAI(temperature=0.3)
chain = LLMChain(llm=llm, prompt=cot_prompt)

# Example: "If a shirt costs $20 after a 20% discount, what was its original price?"
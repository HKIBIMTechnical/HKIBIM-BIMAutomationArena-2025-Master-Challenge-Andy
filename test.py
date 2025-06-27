import streamlit as st
import pandas as pd
from pandasai import Agent

# from pandasai.llm import LLM
from pandasai.helpers.logger import Logger
# import logging
from pandasai import SmartDataframe

# from langchain_openai import ChatOpenAI

from langchain_xai.chat_models import ChatXAI
from langchain_experimental.agents.agent_toolkits import create_csv_agent

from langchain_community.chat_models import ChatOpenAI  # 我们暂时用这个模拟，需替换为 xAI 的实现
import sys
from io import StringIO

old_stdout = sys.stdout
sys.stdout = captured_output = StringIO()


dfTransoms=pd.read_csv(r"pages/transoms.csv")

# llm = ChatXAI(
#     api_key=st.secrets["grok_ad_test_001_apikey"],
#     xai_api_base=st.secrets["grok_api_url"],
#     model="grok-2-latest",
# )
llm = ChatOpenAI(
    api_key=st.secrets["grok_ad_test_001_apikey"],
    model="grok-2-latest",  # 替换为 xAI 提供的模型名称
    temperature=1,
    base_url=st.secrets["grok_api_url"]  # 假设的 xAI API 端点，需根据文档调整
)



agent = create_csv_agent(
    llm,
    r"pages/transoms.csv",  # CSV 文件路径
    verbose=True,   # 显示详细的推理过程
    agent_type="zero-shot-react-description",
    allow_dangerous_code=True,  # 明确允许执行危险代码
    max_iterations=1
    # verbose=True,   # 显示详细的推理过程
    # agent_type="zero-shot-react-description"
)
question = "前两行数据的length的和"
response = agent.run(question)

sys.stdout = old_stdout
verbose_output = captured_output.getvalue()


print("--------------------------------")
print(verbose_output)
print("--------------------------------")










# # 使用 llm 进行对话或其他操作
# response = llm.generate("Hello, how are you?")

# # all_texts = [gen[0].text for gen in response.generations]
# first_text = response.generations[0][0].text

# # # 打印所有生成的文本
# # for text in all_texts:
# #     print(text)

# print(first_text)





# llm = ChatOpenAI(
#         max_tokens=None,
#         # model_kwargs=model_kwargs,
#         model= "grok-2-latest",
#         base_url=st.secrets["grok_api_url"],
#         api_key=st.secrets["grok_ad_test_001_apikey"],
#         # temperature=0.1,
#         # seed=123,
#     )

# dfTransoms=pd.read_csv(r"pages/transoms.csv")

# sdf = SmartDataframe(dfTransoms, config={"llm": llm})


#-------------------------------------------------------------- 


# pai.api_key.set(st.secrets["pandasai_apikey"])
# file = pai.load("pai-personal-3f69d/dataset-name")

# result=pai.chat("What is the total length of the transoms?",file)

# print(result)


#--------------------------------------------------------------



# file = pai.read_csv(r"pages/transoms.csv")


# df = pai.create(
#   path="pai-personal-3f69d/dataset-name",
#   df=file,
#   description="my transoms dataset"
# )

# df.push()


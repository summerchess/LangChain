import os
import dotenv
import time
import asyncio
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,SystemMessage

dotenv.load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("DASHSCOPE_API_KEY")
os.environ["OPENAI_BASE_URL"] = os.getenv("DASHSCOPE_BASE_URL")

llm = ChatOpenAI(model = "qwen-plus")

def sync_test():
    message1 = [SystemMessage(content="你是一位乐于助人的智能小助手"), HumanMessage(content="请帮我介绍一下什么是机器学习")]
    start_time = time.time()
    response = llm.invoke(message1)
    duration = time.time() - start_time
    print(f"同步调用耗时:{duration:.2f}秒")
    return response, duration

async def async_test():
    message1 = [SystemMessage(content="你是一位乐于助人的智能小助手"), HumanMessage(content="请帮我介绍一下什么是机器学习")]
    start_time = time.time()
    response = await llm.ainvoke(message1)
    duration = time.time() - start_time
    print(f"异步调用耗时:{duration:.2f}秒")
    return response, duration

if __name__ == "__main__":
    sync_response, sync_duration = sync_test()
    print(f"同步响应内容:{sync_response.content[:100]}...\n")

    async_response, async_duration = asyncio.run(async_test())
    print(f"同步响应内容:{async_response.content[:100]}...\n")

    print("\n===并发测试===")
    start_time = time.time()

    async def run_concurrent_tests():
        tasks = [async_test() for _ in range(3)]
        return await asyncio.gather(*tasks)
    
    results = asyncio.run(run_concurrent_tests())

    total_time = time.time() - start_time
    print(f"\n3个并发异步调用总耗时:{total_time:.2f}秒")
    print(f"平均每个调用耗时:{total_time/3:.2f}秒")
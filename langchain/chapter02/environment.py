import dotenv
from langchain_openai import ChatOpenAI
import os

# 1️⃣ 读取 .env 文件
dotenv.load_dotenv()

# 2️⃣ 设置环境变量
os.environ["OPENAI_API_KEY"] = os.getenv("DASHSCOPE_API_KEY")  # 通义API Key
os.environ["OPENAI_BASE_URL"] = os.getenv("DASHSCOPE_BASE_URL")

# 3️⃣ 创建模型实例（Qwen）
llm = ChatOpenAI(
    model = "qwen-plus"
)
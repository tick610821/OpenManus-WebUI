import asyncio

from app.agent.manus import Manus
from app.logger import logger


async def main():
    agent = Manus()
    while True:
        try:
            prompt = input("Enter your prompt (or 'exit' to quit): ")
            if prompt.lower() == "exit":
                logger.info("Goodbye!")
                break
            logger.warning("Processing your request...")
            await agent.run(prompt)
        except KeyboardInterrupt:
            logger.warning("Goodbye!")
            break


if __name__ == "__main__":
    asyncio.run(main())

    # 实测一：搜索 Manus Agent 的信息和报道，生成一个 html 用来汇总和报告这个 Agent，你的 html 应该尽可能美观。
    # 实测二：写一个 html 版本的贪吃蛇游戏，又开始按钮和和暂停按钮，贪吃蛇触碰到四周游戏结束，并且有渲染，使其美观。
    # 实测三：帮我写一个登录页面，并且用CSS渲染。
    # 实测四：帮我用python代码实现gmm方法，有一个概率序列，计算转移矩阵熵值差异
    # 请问已知初始状态,怎么估计转移矩阵，求熵率，提供python代码
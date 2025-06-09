from typing import TypedDict
from langgraph.graph import StateGraph, START, END


# 그래프의 상태를 정의하는 클래스


class MyState(TypedDict):
    counter: int


def increment(state):
    return {"counter": state["counter"] + 1}


graph = StateGraph(MyState)

# increment 노드 추가
graph.add_node("increment", increment)

# START에서 increment 노드로 엣지 추가
graph.add_edge(START, "increment")

# increment 노드에서 END로 엣지 추가
graph.add_edge("increment", END)

# 그래프 실행
app = graph.compile()

result = app.invoke({"counter": 0})
print(result)

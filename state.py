## 상태 관리
## https://wikidocs.net/261591

## https://wikidocs.net/264613

##타입 검사

##dict: 런타임에 타입 검사를 하지 않습니다.
##TypedDict: 정적 타입 검사를 제공합니다. 즉, 코드 작성 시 IDE나 타입 체커가 오류를 미리 잡아낼 수 있습니다.

# TypedDict가 dict 대신 사용되는 이유

# 타입 안정성

# TypedDict는 더 엄격한 타입 검사를 제공하여 잠재적인 버그를 미리 방지할 수 있습니다.
# 코드 가독성

# TypedDict를 사용하면 딕셔너리의 구조를 명확하게 정의할 수 있어 코드의 가독성이 향상됩니다.
# IDE 지원

# TypedDict를 사용하면 IDE에서 자동 완성 및 타입 힌트를 더 정확하게 제공받을 수 있습니다.
# 문서화

# TypedDict는 코드 자체가 문서의 역할을 하여 딕셔너리의 구조를 명확히 보여줍니다.

from typing import TypedDict


class MyState(
    TypedDict
):  # 딕셔너리의 키와 값의 타입을 미리 정의할 수 있게 해주는 도구입니다.
    counter: int


def increment(state):
    return {"counter": state["counter"] + 1}

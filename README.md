# coding-test


# Reference

* level-3/num_12.py
    - try, except 구문 사용법 및 EOFError(End Of File Error)
    - 입력값이 언제 끝나는지 모르는 상황
    - 입력을 input()으로 하면, 입력값이 없을경우 EOFError 를 반환하고, sys.stdin.readline() 을 사용할 경우 빈 문자열을 반화함.
    - 단, input() 사용시 시간이 약간 더 오래 걸린다.

* map 함수는 객체(object) 를 반환한다. 더 정확히는 반복가능한 객체(iterator) 를 반환한다. 여기서 객체란 메모리에 할당되있는 것으로 데이터, 식별자에 의해 참조될 수 있는 메모리 공간상의 값을 의미한다.

* level-4/num_2.py
    - 리스트 원소를 한줄로 출력하는 방법
        1. 반복문 + print(x, end=" ") 이용
        2. print(*arr) 이용, Asterisk(*)은 리스트 압축 해제

* level-4/num_4.py
    - 리스트의 특정값의 인덱스 찾는법 > arr.index(value)

* level-6/num_5.py
    - count() 사용법 확인, 배열이나 문자열에서 특정 값의 개수를 반환 (count() 사용여부에 따라 시간이 약 100배 차이남)

* level-6/num_6.py
    - replace(old, new) 함수를 사용하면 기존 문자열의 값을 새로운 값으로 대체 가능

* level-6/num_7.py
    - sorted(list, key=word.find)에서 key를 word.find 를 사용할 경우 word의 각 값에 대한 find 값을 얻고, 이를 오름차순으로 정렬한다. 이 때 동일한 값의 경우 기존 list의 순서가 유지되며 이를 stable 정렬이라한다. [a,b,a] -> [a,a,b] 이고 a의 순서는 정렬 이전과 동일함.

* level-13/num_11.py
    - list.index() 함수의 시간복잡도는 O(N)
    - sort(), sorted() 함수의 시간복잡도는 O(NlogN)
    - 이 문제 총 시간 1688 ms (왜일까?)

* level-14/num_1.py
    - x in arr 함수에서 arr 이 list 이면 1번 찾을 때 마다 O(N)
    - x in arr 함수에서 arr 이 set() 이면 O(1)
    - 파이썬에서는 set() 이 해시테이블 구조 (딕셔너리 자료형) 으로 구성되어 있기 때문이다.

* level-14/num_7.py
    - set() 자료형의 연산 방법
        - 교집합 : a.intersection(b)    | a&b
        - 합집합 : a.union(b)           | a|b
        - 차집합 : a.difference(b)      | a-b
        - 값추가 : a.add()
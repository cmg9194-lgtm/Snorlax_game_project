import random

midterm_questions = [

    {"unit":"조건문",

    "question":
    """
    x = 10

    if x > 5:
        print("A")
    else:
        print("B")

    실행 결과는?
    """,

    "choices":['A','B'], "answer":0},
    {"unit":"반복문",

    "question":
    """
    for i in range(3):
        print(i)

    마지막으로 출력되는 값은?
    """,

    "choices":['2','3'],"answer":0},

    {"unit": "재귀함수","question": "재귀함수에 대한 설명으로 '옳은' 것은?",
        "choices": [
            "자기 자신을 호출",
            "클래스를 생성"
        ],
        "answer": 0
    },

    {"unit": "배열",
        "question": "리스트의 인덱스는 어디서 시작하는가?",
        "choices": ["0","1"],
        "answer": 0
    }
]

final_questions = [

    {"unit": "Class",
        "question": "부모 클래스의 생성자를 호출하는 함수는?",
        "choices": ["super().__init__()","Class.__init__()"],
        "answer": 0
    },

    {"unit": "File IO",
        "question": "피클을 사용하면 저장된 파일을 \n 원래 데이터 타입으로 변환할 수 '없다'.",
        "choices": ["O","X"],
        "answer": 1
    },

    {
        "unit": "Chatper 13. Pygame",
        "question": "강의 pygame 파일에서 다음 코드가 필요한 이유는?\n<def collision(obj1, obj2): ~>",
        "choices": [
            "플레이어와 총알 충돌 확인",
            "충돌된 총알의 이미지를 생성"
        ],
        "answer": 0
    },

    {
        "unit": "Chapter 17. Numpy, Pandas, Matplotlib",
        "question": "df.groupby('반')의 의미로 옳은 것은?",
        "choices": [
            "같은 값의 데이터끼리 묶기",
            "해당 열 삭제"
        ],
        "answer": 0
    }
]
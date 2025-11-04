from flask import Flask, render_template, request

app = Flask(__name__)

QUESTIONS = [
    ("온 세상을 돌아다니며 많은 친구들과 포켓몬을 만나고 싶어!", "가까운 사람 몇 명과 조용히 어울리는 게 더 편해."),
    ("새로운 환경에 금방 적응하는 편이야!", "익숙한 루틴이 안정감을 줘."),
    ("세세한 부분보단 전체적인 그림을 먼저 보는 편이야.", "작은 디테일까지 꼼꼼히 챙기는 편이야."),
    ("감정보다 논리로 판단하는 편이야.", "논리보다 상대의 마음이 더 중요하다고 생각해."),
    ("결정을 미루기보단 바로 행동에 옮겨!", "좀 더 생각해본 뒤에 결정하는 편이야."),
    ("계획을 세워두고 움직이는 게 좋아.", "상황에 따라 유연하게 대처하는 게 좋아."),
    ("포켓몬 배틀에서 전략을 짜는 게 재밌어.", "배틀보다 포켓몬들과 교감하는 게 더 좋아."),
    ("즉흥적인 모험이 더 즐거워!", "예상 가능한 하루가 더 편해.")
]

MBTI_TO_POKEMON = {
    "INTJ": {"name": "후딘", "id": 65, "types": ["에스퍼"], "desc": "전략적이고 통찰력 있는 사고형."},
    "INTP": {"name": "메타그로스", "id": 376, "types": ["강철", "에스퍼"], "desc": "논리적이고 분석적인 사색가형."},
    "ENTJ": {"name": "루카리오", "id": 448, "types": ["격투", "강철"], "desc": "목표 지향적이며 리더십이 강한 지휘관형."},
    "ENTP": {"name": "피카츄", "id": 25, "types": ["전기"], "desc": "호기심 많고 아이디어가 넘치는 발명가형."},
    "INFJ": {"name": "루기아", "id": 249, "types": ["비행", "에스퍼"], "desc": "깊은 통찰력과 이상을 가진 조언자형."},
    "INFP": {"name": "토게키스", "id": 468, "types": ["페어리", "비행"], "desc": "이상주의적이고 따뜻한 감성의 몽상가형."},
    "ENFJ": {"name": "리자몽", "id": 6, "types": ["불꽃", "비행"], "desc": "사람을 이끄는 카리스마와 공감 능력을 지닌 리더형."},
    "ENFP": {"name": "피카츄", "id": 25, "types": ["전기"], "desc": "열정적이고 자유로운 영혼의 탐험가형."},
    "ISTJ": {"name": "보스로라", "id": 306, "types": ["강철", "바위"], "desc": "책임감 있고 신뢰할 수 있는 관리자형."},
    "ISFJ": {"name": "해피너스", "id": 242, "types": ["노말"], "desc": "헌신적이고 타인을 보살피는 보호자형."},
    "ESTJ": {"name": "메타그로스", "id": 376, "types": ["강철", "에스퍼"], "desc": "조직적이고 실무 중심의 현실주의자형."},
    "ESFJ": {"name": "샤미드", "id": 134, "types": ["물"], "desc": "사교적이고 따뜻한 공동체 지향형."},
    "ISTP": {"name": "개굴닌자", "id": 658, "types": ["악", "물"], "desc": "침착하고 실용적인 문제 해결자형."},
    "ISFP": {"name": "리피아", "id": 470, "types": ["풀"], "desc": "예술적이고 감성적인 자유로운 영혼형."},
    "ESTP": {"name": "윈디", "id": 59, "types": ["불꽃"], "desc": "행동력이 뛰어나고 적응력 있는 실행가형."},
    "ESFP": {"name": "마릴", "id": 183, "types": ["물"], "desc": "밝고 즉흥적인 분위기 메이커형."}
}

def calc_mbti(answers):
    ei = sn = tf = jp = 0
    # 각 문항 번호에 따라 축 분류
    for i, ans in enumerate(answers):
        if i in [0]:  # E/I
            ei += 1 if ans == "A" else -1
        elif i in [1, 2]:  # S/N
            sn += 1 if ans == "B" else -1
        elif i in [3, 6]:  # T/F
            tf += 1 if ans == "A" else -1
        elif i in [4, 5, 7]:  # J/P
            jp += 1 if ans == "A" else -1

    mbti = ""
    mbti += "E" if ei > 0 else "I"
    mbti += "S" if sn > 0 else "N"
    mbti += "T" if tf > 0 else "F"
    mbti += "J" if jp > 0 else "P"
    return mbti

@app.route('/')
def index():
    return render_template('index.html', questions=QUESTIONS)

@app.route('/submit', methods=['POST'])
def submit():
    answers = []
    for i in range(1, len(QUESTIONS) + 1):
        answers.append(request.form.get(f'answer{i}'))

    mbti = calc_mbti(answers)
    result = MBTI_TO_POKEMON.get(mbti)
    return render_template('result.html', mbti=mbti, result=result)

if __name__ == '__main__':
    app.run(debug=True)

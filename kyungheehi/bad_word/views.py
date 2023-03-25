# 필요한 라이브러리 import
import openai
import re
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# openai api key 설정
openai.api_key = "여기 설정하세여"

# 입력값이 나쁜말인지 판단하는 함수
def is_bad_word(input_text):
    # openai api를 이용하여 입력값이 나쁜말인지 판단
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"느금마,ㄴㄱㅁ,시1발,시2발,시빨,븅신,병1신,병형신,ㅄ,ㅂㅅ,ㅅㅂ,장애년,장애새끼,tlqkf,qudtls is bad word. ㅋㅋㅋ,ㅋㅋ,ㅋㅋㅋㅋ is not bad word. Is the following text bad? {input_text}",
        temperature=0.5,
        max_tokens=200,
        n=1,
        stop=None,
        frequency_penalty=0,
        presence_penalty=0
    )

    # openai api의 결과값에서 나쁜말 여부를 추출하여 반환
    return bool(re.search(r"\bbad\b|\bprofanity\b|\bvulgar\b|\boffensive\b", response.choices[0].text)), bool(re.search(r"\bYes\b|\byes\b", response.choices[0].text)), response.choices[0].text


def index(request):
    word = request.POST.get('input_value')
    print(word)
    x = ""
    y = ""
    z = ""
    if word == "." or "":
        checked=""
    else:
        x,y,z = is_bad_word(word)
    
        if x == True and y == True:
            checked = "badword"

        elif x == False or y == False:
            checked = "not badword"
    
        else:
            checked = ""
        print(z)
    return render(request, 'bad_word/wordcheck.html', {'checked':checked},)
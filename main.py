import json
import pandas as pd
import openai
import open_key
import csv

# CSV 파일 경로 설정
csv_file_path = './docs/train.csv'

# 파일을 읽기 모드로 열기
with open(csv_file_path, mode='r', encoding='utf-8') as file:
    # CSV 파일을 읽을 준비
    reader = csv.reader(file)

    cnt = -1
    # 한 줄씩 읽어서 출력
    for row in reader:
        cnt += 1
        if cnt == 0:
            continue
        print(row)
        break


# OpenAI API 키를 설정합니다.


# 문단을 받아 질문과 답변 쌍을 생성하는 함수


data = pd.read_csv(csv_file_path)

data_for_llm = data[['ID', 'lang', 'title', 'notes']]

print(data_for_llm)
print(len(data_for_llm))


user_prompt = f"Please follow these steps for each row of data:  1. Determine if the 'title' and 'notices' are related to automobiles. 2. If related, return only 1 if not, return only 0, Provide no additional information or text beyond '0' or '1'. \n {data_for_llm} "
system_prompt = "You are an AI that determines whether a document's title and content are related to automobiles. If the document is related to automobiles respond with 0. If it is not respond with 1. Do not say anything else."

question_response = openai.chat.completions.create(
    temperature=0.1,
    model="gpt-3.5-turbo-0125",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
)
question = question_response.choices[0].message.content.strip()

print(question)

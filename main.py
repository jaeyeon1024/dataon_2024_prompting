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

# # 각 줄에 대해 질문과 답변 쌍 생성 함수


# def generate_qa_pairs_for_rows(data, num_pairs=3):
#     all_qa_pairs = []

#     for id, row in data.iterrows():
#         paragraph = row['특별약관']  # CSV 파일의 열 이름에 맞게 수정

#         for _ in range(num_pairs):
#             # 질문 생성 프롬프트
#             question_prompt = f"쉽게 약관을 선택할 수 있게 약관의 주요 목적을 짧게 알려주세요 한국어로만 대답 :\n{paragraph}\n요약:"
#             question_response = openai.chat.completions.create(
#                 temperature=0.1,
#                 model="gpt-4o-mini",
#                 messages=[
#                     {"role": "system", "content": "You are a helpful assistant."},
#                     {"role": "user", "content": question_prompt}
#                 ]
#             )
#             question = question_response.choices[0].message.content.strip()

#             question_prompt = f"다음 문단은 특별약관들이야 어떤 특별약관인지 특별약관의 이름을 말해줘 한국어로만 대답 :\n{paragraph}\n요약:"
#             question_response = openai.chat.completions.create(
#                 temperature=0.1,
#                 model="gpt-4o-mini",
#                 messages=[
#                     {"role": "system", "content": "You are a helpful assistant."},
#                     {"role": "user", "content": question_prompt}
#                 ]
#             )
#             name = question_response.choices[0].message.content.strip()

#             print(f"요약: {question}", f"특별약관 이름: {name}")

#             # 질문과 답변 쌍 저장
#             qa_pairs = {"question": question, "id": id,
#                         "name": name, "content": paragraph}
#             all_qa_pairs.append(qa_pairs)
#             # print(all_qa_pairs)

#     return all_qa_pairs


# # 질문과 답변 쌍 생성
# qa_pairs = generate_qa_pairs_for_rows(data, num_pairs=1)

# # 결과를 JSON 파일로 저장
# json_file_path = 'summary4.json'
# with open(json_file_path, 'w', encoding='utf-8') as f:
#     json.dump(qa_pairs, f, ensure_ascii=False, indent=4)

# print(f"질문과 답변 쌍이 {json_file_path}에 저장되었습니다.")

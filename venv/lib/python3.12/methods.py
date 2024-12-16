from models import KeyWord, Sport
from crud import get_db, get_keywords, get_sports, get_answers


def parse_input(user_input):
    user_input.lower()
    input_list = user_input.split(" ")
    
    db = next(get_db())
    sports = get_sports(db)
    
    identified_sport = None
    
    identified_keyword = None
    
    for word in input_list:
        for sport in sports:
            if word == sport.content.lower():
                identified_sport = sport
                break
        if identified_sport:
            break
    
    possible_keywords = []   
    
    if identified_sport:
        keywords = get_keywords(db, identified_sport.id)

        keyword_map = {keyword.content.lower(): keyword for keyword in keywords}
    
        for keyword in keyword_map:
            if keyword in user_input:
                possible_keywords.append(keyword_map[keyword])

        for i in range(len(sports)):
            for j in range(i +1, len(input_list)+1):
                phrase = " ".join(input_list[i:j])
                if phrase in keyword_map:
                    possible_keywords.append(keyword_map[phrase])
    
    if possible_keywords:
        identified_keyword = max(possible_keywords, key=lambda kw: len(kw.content))
    
    return identified_keyword


def display_answers(keyword: KeyWord):
    db = next(get_db())
    if keyword is None:
        print("No keyword provided.")
        return []
    
    answers = get_answers(db, keyword.id)
    if answers is None:
        print(f"No answers found for keyword ID: {keyword.id}")
        return []
    
    answer_contents = [answer.content for answer in answers]
    # print(f"Answers for keyword '{keyword.content}': {answer_contents}")
    
    return answer_contents

print(display_answers(parse_input("when can I buy suu football tickets?")))
from sqlalchemy.orm import Session
from crud import get_db, get_keywords, get_answers, get_sport_by_content
from models import KeyWord, Answer

def display_keywords_and_answers(db: Session, sport_id: int):
    try:
        # Retrieve all keywords for the given sport_id
        keywords = get_keywords(db, sport_id)
        if not keywords:
            print("No keywords found for this sport.")
            return

        # Iterate over each keyword and print associated answers
        for keyword in keywords:
            print(f"Keyword: {keyword.content}")
            answers = get_answers(db, keyword.id)
            if not answers:
                print("  No answers found for this keyword.")
            else:
                for answer in answers:
                    print(f"  Answer: {answer.content}")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    with next(get_db()) as db:
        # Fetch a sport by its content (you might get this from user input or other sources)
        input_sport = input("Please enter the sport to view keywords and answers: ").strip().lower()
        sport = get_sport_by_content(db, input_sport)

        if not sport:
            print(f"Sport '{input_sport}' not found.")
            return

        # Display keywords and answers for the fetched sport
        display_keywords_and_answers(db, sport.id)

if __name__ == "__main__":
    main()

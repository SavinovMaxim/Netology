import json
from collections import Counter
import re


def read_json(file_path, word_max_len=6, top_words_amt=10):
    """
    Функция для чтения файла с новостями и вывода топ-N слов.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        all_words = []
        for item in data['rss']['channel']['items']:
            description = item.get('description', '')
            words = re.findall(r'\b\w+\b', description) #Find all words in the text
            all_words.extend(words) #Append the words to list

        filtered_words = [word for word in all_words if len(word) > word_max_len]
        word_counts = Counter(filtered_words)
        top_words = word_counts.most_common(top_words_amt)
        return [word for word, count in top_words] #Return list of words and ignore counts.
    
    except FileNotFoundError:
        print(f"Ошибка: файл '{file_path}' не найден.")
        return []
    except json.JSONDecodeError:
         print(f"Ошибка: Неверный формат JSON")
         return []
    except Exception as e:
        print(f"Возникла ошибка: {e}")
        return []



if __name__ == '__main__':
    dummy_data = {
        "rss": {
            "channel": {
                "items": [
                    {"description": "This is a longer description with some words example. Example words. Example."},
                    {"description": "Another news item with specific words. This news will be shown."},
                    {"description": "Short news."},
                     {"description": "This is another longer description with some new words words words words words"}
                ]
            }
        }
    }

    with open('newsafr.json', 'w', encoding='utf-8') as f:
        json.dump(dummy_data, f)

    top_words = read_json('newsafr.json')
    print(top_words)

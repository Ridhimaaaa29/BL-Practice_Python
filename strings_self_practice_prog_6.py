"""
PROG 6: News Data Processing
Take a paragraph of any news feed from the web and keep that as string and do the following operations:
=> Check if the presence of the word “Modi” is there or not.
=> Count number of words in the news feed
=> Count the numbers of word ‘the’ in the news feed
=> Check presence of digits
=> Create a compact news data and all the article words like ‘a’, ‘an’ and ‘the’ are removed.
=> Plan further compacting by removing vowels from each word

Plan organizing the code in modular way in different functions

Sample Paragraph :

“Government is set to issue Google a notice after the firm’s AI platform Gemini threw up unsubstantiated allegations in response to a query on PM Modi.
Minister of state for IT Rajeev Chandrasekhar took a serious view of the matter after it was flagged by a user on X.
“These are direct violations of Rule 3(1)(b) of Intermediary Rules (IT rules) of IT act and violations of several provisions of the criminal code,”
he posted on X,in a clear indication that govt intends to initiate action.
Gemini attributed allegations of rising authoritarianism and communalism under Modi to unnamed “experts”, as per the X post.”
Input =>
news_paragraph = "Government is set to issue Google a notice after the firm’s AI platform Gemini threw up unsubstantiated allegations in response to a query on PM Modi. Minister of state for IT Rajeev Chandrasekhar took a serious view of the matter after it was flagged by a user on X. “These are direct violations of Rule 3(1)(b) of Intermediary Rules (IT rules) of IT act and violations of several provisions of the criminal code,” he posted on X, in a clear indication that govt intends to initiate action. Gemini attributed allegations of rising authoritarianism and communalism under Modi to unnamed “experts”, as per the X post."

Output => \

Presence of 'Modi': True
Number of words: 105
Number of occurrences of 'the': 4
Presence of digits: True
Compact news data without articles: Government is set to issue Google notice after firm’s AI platform Gemini threw up unsubstantiated allegations in response to query on PM Modi. Minister of state for IT Rajeev Chandrasekhar took serious view of matter after it was flagged by user on X. “These are direct violations of Rule 3(1)(b) of Intermediary Rules (IT rules) of IT act and violations of several provisions of criminal code,” he posted on X, in clear indication that govt intends to initiate action. Gemini attributed allegations of rising authoritarianism and communalism under Modi to unnamed “experts”, as per X post.
Compact news data without vowels: Gvrnmnt s st t ss Ggl  ntc ftr th frm’s  pltfrm Gmn thrw p nsbstnttd llgtns n rspns t  qry n PM Md. Mnstr f stt fr T Rjv Chndrskhr tk  srs vw f th mttr ftr t ws flggd by  sr n X. “Ths r drct vltns f Rl 3(1)(b) f ntrmdry Rls (T rls) f T ct nd vltns f svrl prvsns f th crmnl cd,” h pstd n X, n  clr ndctn tht gvt ntnds t ntt ctn. Gmn ttrbtd llgtns f rsng thrtrnsm nd cmmnlsm ndr Md t nnmd “xprts”, s pr th X pst.
Hint => \

Use split()
Use count()
Use join()
Use List Comprehension
"""


# PROG 6: News Data Processing

news_paragraph = """Government is set to issue Google a notice after the firm’s AI platform Gemini threw up unsubstantiated allegations in response to a query on PM Modi.
Minister of state for IT Rajeev Chandrasekhar took a serious view of the matter after it was flagged by a user on X.
These are direct violations of Rule 3(1)(b) of Intermediary Rules (IT rules) of IT act and violations of several provisions of the criminal code,
he posted on X, in a clear indication that govt intends to initiate action.
Gemini attributed allegations of rising authoritarianism and communalism under Modi to unnamed experts, as per the X post."""


# Function to check presence of "Modi"
def check_modi(paragraph):
    return "Modi" in paragraph


# Function to count words
def count_words(paragraph):
    words = paragraph.split()
    return len(words)


# Function to count occurrences of "the"
def count_the(paragraph):
    words = paragraph.lower().split()
    return words.count("the")


# Function to check if digits are present
def has_digits(paragraph):
    for ch in paragraph:
        if ch.isdigit():
            return True
    return False


# Function to remove articles
def remove_articles(paragraph):
    articles = ["a", "an", "the"]
    words = paragraph.split()
    filtered = [word for word in words if word.lower() not in articles]
    return " ".join(filtered)


# Function to remove vowels
def remove_vowels(paragraph):
    vowels = "aeiouAEIOU"
    words = paragraph.split()

    new_words = []
    for word in words:
        new_word = ""
        for ch in word:
            if ch not in vowels:
                new_word += ch
        new_words.append(new_word)

    return " ".join(new_words)


# Output
print("Presence of 'Modi':", check_modi(news_paragraph))
print("Number of words:", count_words(news_paragraph))
print("Number of occurrences of 'the':", count_the(news_paragraph))
print("Presence of digits:", has_digits(news_paragraph))
print("\nCompact news data without articles:")
print(remove_articles(news_paragraph))
print("\nCompact news data without vowels:")
print(remove_vowels(news_paragraph))


"""
Concepts Used:
 split() → Convert paragraph into words.
 count() → Count occurrences of "the".
 join() → Join words back into a paragraph.
 List Comprehension → Remove articles (a, an, the).
 Functions (def) → Modular programming as required.
"""
import pickle
import re

loaded_classifier = pickle.load(open('server/spam_email_classifier.pickle','rb'))
loaded_vectorizer = pickle.load(open('server/vectorizer.pickle','rb'))

def classify_email(email):
    removed_tabs_newline = re.sub('[\n|\t]',' ',email)
    removed_spchar_digits = re.sub('[^a-zA-Z]',' ',removed_tabs_newline)
    lower_case_email = removed_spchar_digits.lower()
    vector = loaded_vectorizer.transform([lower_case_email]).toarray()
    return loaded_classifier.predict(vector)
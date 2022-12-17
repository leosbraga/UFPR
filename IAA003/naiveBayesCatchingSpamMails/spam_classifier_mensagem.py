# MODIFICAÇÕES:
# 1: avalia também a mensagem do e-mail (acha a primeira linha em branco e 
#    pega a informação até dessa linha até a última)
# 2: adicionado um heatmap da matriz de confusão
# 3: adicionado um percentual de assertividade com base na matriz de confusão
# CONCLUSÂO: nesse caso, incluir a mensagem (além do assunto) melhorou a 
# assertividade do algorítmo de 91,64% para 92,06%

from typing import TypeVar, List, Tuple, Dict, Iterable, NamedTuple, Set
from collections import defaultdict, Counter
import re
import random
import math
import pandas as pd
import seaborn as sn
import numpy as np

X = TypeVar('X')  # generic type to represent a data point

def split_data(data: List[X], prob: float) -> Tuple[List[X], List[X]]:
    """Split data into fractions [prob, 1 - prob]"""
    data = data[:]                    # Make a shallow copy
    random.shuffle(data)              # because shuffle modifies the list.
    cut = int(len(data) * prob)       # Use prob to find a cutoff
    return data[:cut], data[cut:]     # and split the shuffled list there.

def tokenize(text: str) -> Set[str]:
    text = text.lower()                         # Convert to lowercase,
    all_words = re.findall("[a-z0-9']+", text)  # extract the words, and
    return set(all_words)                       # remove duplicates.

assert tokenize("Data Science is science") == {"data", "science", "is"}

class Message(NamedTuple):
    text: str
    is_spam: bool

class NaiveBayesClassifier:
    def __init__(self, k: float = 0.5) -> None:
        self.k = k  # smoothing factor

        self.tokens: Set[str] = set()
        self.token_spam_counts: Dict[str, int] = defaultdict(int)
        self.token_ham_counts: Dict[str, int] = defaultdict(int)
        self.spam_messages = self.ham_messages = 0

    def train(self, messages: Iterable[Message]) -> None:
        for message in messages:
            # Increment message counts
            if message.is_spam:
                self.spam_messages += 1
            else:
                self.ham_messages += 1

            # Increment word counts
            for token in tokenize(message.text):
                self.tokens.add(token)
                if message.is_spam:
                    self.token_spam_counts[token] += 1
                else:
                    self.token_ham_counts[token] += 1

    def probabilities(self, token: str) -> Tuple[float, float]:
        """returns P(token | spam) and P(token | not spam)"""
        spam = self.token_spam_counts[token]
        ham = self.token_ham_counts[token]

        p_token_spam = (spam + self.k) / (self.spam_messages + 2 * self.k)
        p_token_ham = (ham + self.k) / (self.ham_messages + 2 * self.k)

        return p_token_spam, p_token_ham

    def predict(self, text: str) -> float:
        text_tokens = tokenize(text)
        log_prob_if_spam = log_prob_if_ham = 0.0

        # Iterate through each word in our vocabulary.
        for token in self.tokens:
            prob_if_spam, prob_if_ham = self.probabilities(token)

            # If *token* appears in the message,
            # add the log probability of seeing it;
            if token in text_tokens:
                log_prob_if_spam += math.log(prob_if_spam)
                log_prob_if_ham += math.log(prob_if_ham)

            # otherwise add the log probability of _not_ seeing it
            # which is log(1 - probability of seeing it)
            else:
                log_prob_if_spam += math.log(1.0 - prob_if_spam)
                log_prob_if_ham += math.log(1.0 - prob_if_ham)

        prob_if_spam = math.exp(log_prob_if_spam)
        prob_if_ham = math.exp(log_prob_if_ham)
        return prob_if_spam / (prob_if_spam + prob_if_ham)

###############################################################################
# Testes do Modelo
# 

messages = [Message("spam rules", is_spam=True),
            Message("ham rules", is_spam=False),
            Message("hello ham", is_spam=False)]

model = NaiveBayesClassifier(k=0.5)
model.train(messages)

assert model.tokens == {"spam", "ham", "rules", "hello"}
assert model.spam_messages == 1
assert model.ham_messages == 2
assert model.token_spam_counts == {"spam": 1, "rules": 1}
assert model.token_ham_counts == {"ham": 2, "rules": 1, "hello": 1}

text = "hello spam"

probs_if_spam = [
    (1 + 0.5) / (1 + 2 * 0.5),      # "spam"  (present)
    1 - (0 + 0.5) / (1 + 2 * 0.5),  # "ham"   (not present)
    1 - (1 + 0.5) / (1 + 2 * 0.5),  # "rules" (not present)
    (0 + 0.5) / (1 + 2 * 0.5)       # "hello" (present)
]

probs_if_ham = [
    (0 + 0.5) / (2 + 2 * 0.5),      # "spam"  (present)
    1 - (2 + 0.5) / (2 + 2 * 0.5),  # "ham"   (not present)
    1 - (1 + 0.5) / (2 + 2 * 0.5),  # "rules" (not present)
    (1 + 0.5) / (2 + 2 * 0.5),      # "hello" (present)
]

p_if_spam = math.exp(sum(math.log(p) for p in probs_if_spam))
p_if_ham = math.exp(sum(math.log(p) for p in probs_if_ham))

# Should be about 0.83
assert math.isclose(model.predict(text), p_if_spam / (p_if_spam + p_if_ham))

###############################################################################
# Exemplo com mensagens verdadeiras
# 

#def main():
import glob

# modify the path to wherever you've put the files
path = 'emails/*/*'

data: List[Message] = []

# glob.glob returns every filename that matches the wildcarded path
for filename in glob.glob(path):
    is_spam = "ham" not in filename


    # There are some garbage characters in the emails, the errors='ignore'
    # skips them instead of raising an exception.
    with open(filename, errors='ignore') as email_file:
       # data.append(Message(email_file.read(), is_spam))
        for line in email_file:
            if line.startswith("Subject:"):
                subject = line.lstrip("Subject: ")
                data.append(Message(subject, is_spam))
                #break  # done with this file
            if len(line)==1 and line.startswith(" "):
                current_line = id(line)
                last_line = email_file.readlines()[-1]
                while current_line <= last_line:
                   text = line.lstrip()  
                   data.append(Message(text, is_spam))
                   break
                   


random.seed(0)      # just so you get the same answers as me
train_messages, test_messages = split_data(data, 0.75)

model = NaiveBayesClassifier()
model.train(train_messages)

predictions = [(message, model.predict(message.text))
               for message in test_messages]

# Assume that spam_probability > 0.5 corresponds to spam prediction
# and count the combinations of (actual is_spam, predicted is_spam)
confusion_matrix = Counter((message.is_spam, spam_probability > 0.5 )
                           for message, spam_probability in predictions)

i = 0
while i < 4:
    print(list(confusion_matrix.keys())[i],": ", list(confusion_matrix.values())[i],sep="")
    i += 1


cm_val = pd.DataFrame(
    np.array([list(confusion_matrix.keys()),
              list(confusion_matrix.values())])).T
cm_val=cm_val.sort_values(by=[0],ignore_index=True)
array = np.array([list(cm_val[0:2][1]), list(cm_val[2:][1])])   
df_cm = pd.DataFrame(array, ["Spam","Ham"], ["Spam","Ham"])     
print("\n")
print(df_cm)
print("\n")
sn.set(font_scale=1.4)#for label size 
sn.heatmap(df_cm, annot=True,annot_kws={"size": 16})# font size
assertiveness = round((array[0][0]+array[1][1])/sum(sum(array))*100,2)
print(assertiveness)

    
def p_spam_given_token(token: str, model: NaiveBayesClassifier) -> float:
    prob_if_spam, prob_if_ham = model.probabilities(token)

    return prob_if_spam / (prob_if_spam + prob_if_ham)

words = sorted(model.tokens, key=lambda t: p_spam_given_token(t, model))

print("spammiest_words", words[-10:])
print("hammiest_words", words[:10])

#if __name__ == "__main__": main()
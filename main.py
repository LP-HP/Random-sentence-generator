import sys
import random
punctuation = ['.', ',', '!', '?', ';', '"', "(", ")", '\'']
end_punctuation = [".", "!", "?"]
def parse(text):
    words = []
    start = 0
    spaces = [' ', '\n', '\t', '\r']
    for cur, char in enumerate(text):
        if text[start] in spaces:
            start = cur
            continue
        if char in spaces or char in punctuation:
            word = text[start : cur]
            words.append(word)
            start = cur
    return words

def build_markov_chain(words):
    chains = {}
    for i, word in enumerate(words):

        if word not in chains and word not in end_punctuation:
            chains[word] = {}
        if i == 0:
            continue
        prev_word = words[i - 1]
        if prev_word in end_punctuation:
            continue
        if word not in chains[prev_word]:
            chains[prev_word][word] = 0
        chains[prev_word][word] += 1
    return chains

def generate_sentence(word, chains, sentence):
    sentence.append(word)
    if word in end_punctuation:
        return sentence

    next_words = chains[word]
    next_word = random.choices([k for k in next_words.keys()], weights = [v for v in next_words.values()]) [0]
    return generate_sentence(next_word, chains, sentence)


def main():
    filename = sys.argv[1]
    with open(filename) as f:
        text = f.read()
        words = parse(text)
        chains = build_markov_chain(words)
        start_words = [w for w in chains.keys() if w[0].isupper()]
        start_word = random.choice(start_words)
        sentence = generate_sentence(start_word, chains, [])
        sentenceSTR = ""
        for word in sentence:
            if word in punctuation:
                sentenceSTR = sentenceSTR[: -1]
            sentenceSTR += word
            sentenceSTR += " "
        print(sentenceSTR)

main()

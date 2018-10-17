from nltk.util import ngrams
from nltk.tokenize import sent_tokenize,word_tokenize

sample_text = '''NLP is marketed by some hypnotherapists and by some companies that organize seminars and workshops on management training for businesses.[9] There is no scientific evidence supporting the claims made by NLP advocates and it has been discredited as a pseudoscience by experts.[10][11] Scientific reviews state that NLP is based on outdated metaphors of how the brain works that are inconsistent with current neurological theory and contain numerous factual errors.[12][13] Reviews also found that all of the supportive research on NLP contained significant methodological flaws and that there were three times as many studies of a much higher quality that failed to reproduce the "extraordinary claims" made by Bandler, Grinder, and other NLP practitioners.[11][14] Even so, NLP has been adopted by some hypnotherapists and also by companies that run seminars marketed as leadership training to businesses and government agencies.
                Neuro-linguistic programming (NLP) is an approach to communication, personal development, and psychotherapy created by Richard Bandler and John Grinder in California, United States in the 1970s. NLP's creators claim there is a connection between neurological processes (neuro-), language (linguistic) and behavioral patterns learned through experience (programming), and that these can be changed to achieve specific goals in life.'''

data_wordtokens = word_tokenize(sample_text)
#data_senttokens = sent_tokenize(sample_text)

word_ngrams = ngrams(data_wordtokens,6)
sent_ngrams = ngrams(data_senttokens,5)

for data in word_ngrams:
    print(data)
    print('\n')

#for data in sent_ngrams:
#   print(data)
#   print('\n')

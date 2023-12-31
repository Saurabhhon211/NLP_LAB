'''Name:Saurabh Hon
Batch:B2
Roll no:25
Pract no 3: Generating the n gram model using nltk'''
from nltk import ngrams

from nltk.util import ngrams
#unigram model
n = 1
sentence = 'While unigram model sentences will only exclude the UNK token, models will also exclude all other words already in the sentence.NTK provides another function everygrams that converts a sentence into unigram, bigram, trigram, and so on till the ngrams, where n is the length of the sentence. In short, this function generates ngrams for all possible values of n.'
unigrams = ngrams(sentence.split(), n)

for item in unigrams:
    print(item)
#bigram model
n = 2
sentence = 'While unigram model sentences will only exclude the UNK token, models will also exclude all other words already in the sentence.NTK provides another function everygrams that converts a sentence into unigram, bigram, trigram, and so on till the ngrams, where n is the length of the sentence. In short, this function generates ngrams for all possible values of n.'
unigrams = ngrams(sentence.split(), n)

for item in unigrams:
    print(item)
#trigram model
n = 3
sentence = 'While unigram model sentences will only exclude the UNK token, models will also exclude all other words already in the sentence.NTK provides another function everygrams that converts a sentence into unigram, bigram, trigram, and so on till the ngrams, where n is the length of the sentence. In short, this function generates ngrams for all possible values of n.'
unigrams = ngrams(sentence.split(), n)

for item in unigrams:
    print(item)

#using text file input
from nltk import ngrams
file = open("/home/exam/Desktop/al.txt")
for i in file.readlines():
    cumulative = i
    sentences = i.split(".")
    counter = 0
    for sentence in sentences:
        print("For sentence", counter + 1, ", trigrams are: ")
        trigrams = ngrams(sentence.split(" "), 3)
        for grams in trigrams:
            print(grams)
        counter += 1
        print()
        
 #output    
'''('While',)
('unigram',)
('model',)
('sentences',)
('will',)
('only',)
('exclude',)
('the',)
('UNK',)
('token,',)
('models',)
('will',)
('also',)
('exclude',)
('all',)
('other',)
('words',)
('already',)
('in',)
('the',)
('sentence.NTK',)
('provides',)
('another',)
('function',)
('everygrams',)
('that',)
('converts',)
('a',)
('sentence',)
('into',)
('unigram,',)
('bigram,',)
('trigram,',)
('and',)
('so',)
('on',)
('till',)
('the',)
('ngrams,',)
('where',)
('n',)
('is',)
('the',)
('length',)
('of',)
('the',)
('sentence.',)
('In',)
('short,',)
('this',)
('function',)
('generates',)
('ngrams',)
('for',)
('all',)
('possible',)
('values',)
('of',)
('n.',)

#bigram model
('While', 'unigram')
('unigram', 'model')
('model', 'sentences')
('sentences', 'will')
('will', 'only')
('only', 'exclude')
('exclude', 'the')
('the', 'UNK')
('UNK', 'token,')
('token,', 'models')
('models', 'will')
('will', 'also')
('also', 'exclude')
('exclude', 'all')
('all', 'other')
('other', 'words')
('words', 'already')
('already', 'in')
('in', 'the')
('the', 'sentence.NTK')
('sentence.NTK', 'provides')
('provides', 'another')
('another', 'function')
('function', 'everygrams')
('everygrams', 'that')
('that', 'converts')
('converts', 'a')
('a', 'sentence')
('sentence', 'into')
('into', 'unigram,')
('unigram,', 'bigram,')
('bigram,', 'trigram,')
('trigram,', 'and')
('and', 'so')
('so', 'on')
('on', 'till')
('till', 'the')
('the', 'ngrams,')
('ngrams,', 'where')
('where', 'n')
('n', 'is')
('is', 'the')
('the', 'length')
('length', 'of')
('of', 'the')
('the', 'sentence.')
('sentence.', 'In')
('In', 'short,')
('short,', 'this')
('this', 'function')
('function', 'generates')
('generates', 'ngrams')
('ngrams', 'for')
('for', 'all')
('all', 'possible')
('possible', 'values')
('values', 'of')
('of', 'n.')
#tri-gram model
('While', 'unigram', 'model')
('unigram', 'model', 'sentences')
('model', 'sentences', 'will')
('sentences', 'will', 'only')
('will', 'only', 'exclude')
('only', 'exclude', 'the')
('exclude', 'the', 'UNK')
('the', 'UNK', 'token,')
('UNK', 'token,', 'models')
('token,', 'models', 'will')
('models', 'will', 'also')
('will', 'also', 'exclude')
('also', 'exclude', 'all')
('exclude', 'all', 'other')
('all', 'other', 'words')
('other', 'words', 'already')
('words', 'already', 'in')
('already', 'in', 'the')
('in', 'the', 'sentence.NTK')
('the', 'sentence.NTK', 'provides')
('sentence.NTK', 'provides', 'another')
('provides', 'another', 'function')
('another', 'function', 'everygrams')
('function', 'everygrams', 'that')
('everygrams', 'that', 'converts')
('that', 'converts', 'a')
('converts', 'a', 'sentence')
('a', 'sentence', 'into')
('sentence', 'into', 'unigram,')
('into', 'unigram,', 'bigram,')
('unigram,', 'bigram,', 'trigram,')
('bigram,', 'trigram,', 'and')
('trigram,', 'and', 'so')
('and', 'so', 'on')
('so', 'on', 'till')
('on', 'till', 'the')
('till', 'the', 'ngrams,')
('the', 'ngrams,', 'where')
('ngrams,', 'where', 'n')
('where', 'n', 'is')
('n', 'is', 'the')
('is', 'the', 'length')
('the', 'length', 'of')
('length', 'of', 'the')
('of', 'the', 'sentence.')
('the', 'sentence.', 'In')
('sentence.', 'In', 'short,')
('In', 'short,', 'this')
('short,', 'this', 'function')
('this', 'function', 'generates')
('function', 'generates', 'ngrams')
('generates', 'ngrams', 'for')
('ngrams', 'for', 'all')
('for', 'all', 'possible')
('all', 'possible', 'values')
('possible', 'values', 'of')
('values', 'of', 'n.')

#text file input
For sentence 1 , trigrams are: 
('Drawbacks', 'of', 'Social')
('of', 'Social', 'Issues\n')

For sentence 1 , trigrams are: 

For sentence 1 , trigrams are: 
('Social', 'issues', 'have')
('issues', 'have', 'a')
('have', 'a', 'lot')
('a', 'lot', 'of')
('lot', 'of', 'drawbacks')
('of', 'drawbacks', 'that')
('drawbacks', 'that', 'harms')
('that', 'harms', 'our')
('harms', 'our', 'society')

For sentence 2 , trigrams are: 
('', 'They', 'are')
('They', 'are', 'situations')
('are', 'situations', 'that')
('situations', 'that', 'have')
('that', 'have', 'an')
('have', 'an', 'adverse')
('an', 'adverse', 'and')
('adverse', 'and', 'damaging')
('and', 'damaging', 'result')
('damaging', 'result', 'on')
('result', 'on', 'our')
('on', 'our', 'society')

For sentence 3 , trigrams are: 
('', 'They', 'arise')
('They', 'arise', 'when')
('arise', 'when', 'the')
('when', 'the', 'public')
('the', 'public', 'leaves')
('public', 'leaves', 'nature')
('leaves', 'nature', 'or')
('nature', 'or', 'society')
('or', 'society', 'from')
('society', 'from', 'an')
('from', 'an', 'ideal')
('an', 'ideal', 'situation')

For sentence 4 , trigrams are: 

For sentence 1 , trigrams are: 

For sentence 1 , trigrams are: 
('If', 'you', 'look')
('you', 'look', 'closely,')
('look', 'closely,', 'you')
('closely,', 'you', 'will')
('you', 'will', 'realize')
('will', 'realize', 'that')
('realize', 'that', 'almost')
('that', 'almost', 'all')
('almost', 'all', 'types')
('all', 'types', 'of')
('types', 'of', 'social')
('of', 'social', 'issues')
('social', 'issues', 'have')
('issues', 'have', 'common')
('have', 'common', 'origins')

For sentence 2 , trigrams are: 
('', 'In', 'the')
('In', 'the', 'sense')
('the', 'sense', 'that')
('sense', 'that', 'they')
('that', 'they', 'all')
('they', 'all', 'are')
('all', 'are', 'interconnected')
('are', 'interconnected', 'somehow')

For sentence 3 , trigrams are: 
('', 'Meaning', 'to')
('Meaning', 'to', 'say,')
('to', 'say,', 'if')
('say,', 'if', 'one')
('if', 'one', 'solves')
('one', 'solves', 'the')
('solves', 'the', 'other')
('the', 'other', 'one')
('other', 'one', 'is')
('one', 'is', 'also')
('is', 'also', 'most')
('also', 'most', 'likely')
('most', 'likely', 'to')
('likely', 'to', 'resolve')

For sentence 4 , trigrams are: 

For sentence 1 , trigrams are: 

For sentence 1 , trigrams are: 
('Social', 'issues', 'have')
('issues', 'have', 'a')
('have', 'a', 'massive')
('a', 'massive', 'lousy')
('massive', 'lousy', 'effect')
('lousy', 'effect', 'on')
('effect', 'on', 'our')
('on', 'our', 'society')
('our', 'society', 'and')
('society', 'and', 'ultimately,')
('and', 'ultimately,', 'it')
('ultimately,', 'it', 'affects')
('it', 'affects', 'all')
('affects', 'all', 'of')
('all', 'of', 'us')

For sentence 2 , trigrams are: 
('', 'In', 'order')
('In', 'order', 'to')
('order', 'to', 'solve')
('to', 'solve', 'some')
('solve', 'some', 'social')
('some', 'social', 'issues,')
('social', 'issues,', 'we')
('issues,', 'we', 'need')
('we', 'need', 'a')
('need', 'a', 'common')
('a', 'common', 'approach')

For sentence 3 , trigrams are: 
('', 'No', 'society')
('No', 'society', 'is')
('society', 'is', 'free')
('is', 'free', 'from')
('free', 'from', 'social')
('from', 'social', 'issues,')
('social', 'issues,', 'almost')
('issues,', 'almost', 'every')
('almost', 'every', 'one')
('every', 'one', 'of')
('one', 'of', 'them')
('of', 'them', 'has')
('them', 'has', 'some')
('has', 'some', 'social')
('some', 'social', 'issue')
('social', 'issue', 'or')
('issue', 'or', 'the')
('or', 'the', 'other')

For sentence 4 , trigrams are: 

For sentence 1 , trigrams are: 

For sentence 1 , trigrams are: 
('For', 'instance,', 'in')
('instance,', 'in', 'India,')
('in', 'India,', 'you')
('India,', 'you', 'will')
('you', 'will', 'find')
('will', 'find', 'a')
('find', 'a', 'lot')
('a', 'lot', 'of')
('lot', 'of', 'social')
('of', 'social', 'issues')
('social', 'issues', 'which')
('issues', 'which', 'the')
('which', 'the', 'country')
('the', 'country', 'is')
('country', 'is', 'facing')

For sentence 2 , trigrams are: 
('', 'It', 'ranges')
('It', 'ranges', 'from')
('ranges', 'from', 'the')
('from', 'the', 'caste')
('the', 'caste', 'system')
('caste', 'system', 'to')
('system', 'to', 'child')
('to', 'child', 'labour')
('child', 'labour', 'and')
('labour', 'and', 'gender')
('and', 'gender', 'inequality')
('gender', 'inequality', 'to')
('inequality', 'to', 'religious')
('to', 'religious', 'conflicts')

For sentence 3 , trigrams are: 
('', 'Thus,', 'we')
('Thus,', 'we', 'are')
('we', 'are', 'going')
('are', 'going', 'through')
('going', 'through', 'a')
('through', 'a', 'critical')
('a', 'critical', 'time')
('critical', 'time', 'where')
('time', 'where', 'we')
('where', 'we', 'all')
('we', 'all', 'must')
('all', 'must', 'come')
('must', 'come', 'together')
('come', 'together', 'to')
('together', 'to', 'free')
('to', 'free', 'our')
('free', 'our', 'society')
('our', 'society', 'from')
('society', 'from', 'undesirable')
('from', 'undesirable', 'social')
('undesirable', 'social', 'evils')

For sentence 4 , trigrams are: 

For sentence 1 , trigrams are: 

For sentence 1 , trigrams are: 
('Get', 'the', 'huge')
('the', 'huge', 'list')
('huge', 'list', 'of')
('list', 'of', 'more')
('of', 'more', 'than')
('more', 'than', '500')
('than', '500', 'Essay')
('500', 'Essay', 'Topics')
('Essay', 'Topics', 'and')
('Topics', 'and', 'Ideas\n')

For sentence 1 , trigrams are: 
('Major', 'Social', 'Issues\n')

For sentence 1 , trigrams are: 

For sentence 1 , trigrams are: 
('There', 'are', 'a')
('are', 'a', 'lot')
('a', 'lot', 'of')
('lot', 'of', 'social')
('of', 'social', 'issues')
('social', 'issues', 'we')
('issues', 'we', 'are')
('we', 'are', 'facing')
('are', 'facing', 'right')
('facing', 'right', 'now,')
('right', 'now,', 'some')
('now,', 'some', 'more')
('some', 'more', 'prominent')
('more', 'prominent', 'than')
('prominent', 'than', 'the')
('than', 'the', 'others')

For sentence 2 , trigrams are: 
('', 'First', 'of')
('First', 'of', 'all,')
('of', 'all,', 'poverty')
('all,', 'poverty', 'is')
('poverty', 'is', 'a')
('is', 'a', 'worldwide')
('a', 'worldwide', 'issue')

For sentence 3 , trigrams are: 
('', 'It', 'gives')
('It', 'gives', 'birth')
('gives', 'birth', 'to')
('birth', 'to', 'a')
('to', 'a', 'lot')
('a', 'lot', 'of')
('lot', 'of', 'other')
('of', 'other', 'social')
('other', 'social', 'issues')
('social', 'issues', 'which')
('issues', 'which', 'we')
('which', 'we', 'must')
('we', 'must', 'try')
('must', 'try', 'to')
('try', 'to', 'get')
('to', 'get', 'away')
('get', 'away', 'with')
('away', 'with', 'at')
('with', 'at', 'the')
('at', 'the', 'earliest')

For sentence 4 , trigrams are: 

For sentence 1 , trigrams are: 

For sentence 1 , trigrams are: 
('Further,', 'countries', 'like')
('countries', 'like', 'India,')
('like', 'India,', 'Nepal,')
('India,', 'Nepal,', 'Bangladesh,')
('Nepal,', 'Bangladesh,', 'Sri')
('Bangladesh,', 'Sri', 'Lanka,')
('Sri', 'Lanka,', 'Pakistan')
('Lanka,', 'Pakistan', 'and')
('Pakistan', 'and', 'more')
('and', 'more', 'are')
('more', 'are', 'facing')
('are', 'facing', 'the')
('facing', 'the', 'issue')
('the', 'issue', 'of')
('issue', 'of', 'the')
('of', 'the', 'caste')
('the', 'caste', 'system')
('caste', 'system', 'since')
('system', 'since', 'times')
('since', 'times', 'unknown')

For sentence 2 , trigrams are: 
('', 'It', 'results')
('It', 'results', 'in')
('results', 'in', 'a')
('in', 'a', 'lot')
('a', 'lot', 'of')
('lot', 'of', 'caste')
('of', 'caste', 'violence')
('caste', 'violence', 'and')
('violence', 'and', 'inequality')
('and', 'inequality', 'which')
('inequality', 'which', 'takes')
('which', 'takes', 'the')
('takes', 'the', 'lives')
('the', 'lives', 'of')
('lives', 'of', 'many')
('of', 'many', 'on')
('many', 'on', 'a')
('on', 'a', 'daily')
('a', 'daily', 'basis')

For sentence 3 , trigrams are: 

For sentence 1 , trigrams are: 

For sentence 1 , trigrams are: 
('Moreover,', 'child', 'labour')
('child', 'labour', 'is')
('labour', 'is', 'another')
('is', 'another', 'major')
('another', 'major', 'social')
('major', 'social', 'issue')
('social', 'issue', 'that')
('issue', 'that', 'damages')
('that', 'damages', 'the')
('damages', 'the', 'lives')
('the', 'lives', 'of')
('lives', 'of', 'young')
('of', 'young', 'children')

For sentence 2 , trigrams are: 
('', 'Similarly,', 'illiteracy')
('Similarly,', 'illiteracy', 'also')
('illiteracy', 'also', 'ruins')
('also', 'ruins', 'the')
('ruins', 'the', 'lives')
('the', 'lives', 'of')
('lives', 'of', 'many')
('of', 'many', 'by')
('many', 'by', 'destroying')
('by', 'destroying', 'their')
('destroying', 'their', 'chances')
('their', 'chances', 'of')
('chances', 'of', 'a')
('of', 'a', 'bright')
('a', 'bright', 'future')

For sentence 3 , trigrams are: 

For sentence 1 , trigrams are: 

For sentence 1 , trigrams are: 
('In', 'developing', 'countries')
('developing', 'countries', 'mostly,')
('countries', 'mostly,', 'child')
('mostly,', 'child', 'marriage')
('child', 'marriage', 'still')
('marriage', 'still', 'exists')
('still', 'exists', 'and')
('exists', 'and', 'is')
('and', 'is', 'responsible')
('is', 'responsible', 'for')
('responsible', 'for', 'ruining')
('for', 'ruining', 'many')
('ruining', 'many', 'lives')

For sentence 2 , trigrams are: 
('', 'Similarly,', 'dowry')
('Similarly,', 'dowry', 'is')
('dowry', 'is', 'a')
('is', 'a', 'very')
('a', 'very', 'serious')
('very', 'serious', 'and')
('serious', 'and', 'common')
('and', 'common', 'social')
('common', 'social', 'issue')
('social', 'issue', 'that')
('issue', 'that', 'almost')
('that', 'almost', 'all')
('almost', 'all', 'classes')
('all', 'classes', 'of')
('classes', 'of', 'people')
('of', 'people', 'partake')
('people', 'partake', 'in')

For sentence 3 , trigrams are: 

For sentence 1 , trigrams are: 

For sentence 1 , trigrams are: 
('Another', 'prominent', 'social')
('prominent', 'social', 'issue')
('social', 'issue', 'is')
('issue', 'is', 'gender')
('is', 'gender', 'inequality')
('gender', 'inequality', 'which')
('inequality', 'which', 'takes')
('which', 'takes', 'away')
('takes', 'away', 'many')
('away', 'many', 'opportunities')
('many', 'opportunities', 'from')
('opportunities', 'from', 'deserving')
('from', 'deserving', 'people')

For sentence 2 , trigrams are: 
('', 'Domestic', 'violence')
('Domestic', 'violence', 'especially')
('violence', 'especially', 'against')
('especially', 'against', 'women')
('against', 'women', 'is')
('women', 'is', 'a')
('is', 'a', 'serious')
('a', 'serious', 'social')
('serious', 'social', 'issue')
('social', 'issue', 'we')
('issue', 'we', 'must')
('we', 'must', 'all')
('must', 'all', 'fight')
('all', 'fight', 'against')

For sentence 3 , trigrams are: 

For sentence 1 , trigrams are: 

For sentence 1 , trigrams are: 
('Other', 'social', 'issues')
('social', 'issues', 'include')
('issues', 'include', 'starvation,')
('include', 'starvation,', 'child')
('starvation,', 'child', 'sex')
('child', 'sex', 'abuse,')
('sex', 'abuse,', 'religious')
('abuse,', 'religious', 'conflicts,')
('religious', 'conflicts,', 'child')
('conflicts,', 'child', 'trafficking,')
('child', 'trafficking,', 'terrorism,')
('trafficking,', 'terrorism,', 'overpopulation,')
('terrorism,', 'overpopulation,', 'untouchability,')
('overpopulation,', 'untouchability,', 'communalism')
('untouchability,', 'communalism', 'and')
('communalism', 'and', 'many')
('and', 'many', 'more')

For sentence 2 , trigrams are: 
('', 'It', 'is')
('It', 'is', 'high')
('is', 'high', 'time')
('high', 'time', 'we')
('time', 'we', 'end')
('we', 'end', 'these')
('end', 'these', 'social')
('these', 'social', 'issues')

For sentence 3 , trigrams are: 

For sentence 1 , trigrams are: 
('Conclusion', 'of', 'the')
('of', 'the', 'Essay')
('the', 'Essay', 'on')
('Essay', 'on', 'Social')
('on', 'Social', 'Issues\n')

For sentence 1 , trigrams are: 

For sentence 1 , trigrams are: 
('A', 'society', 'can')
('society', 'can', 'successfully')
('can', 'successfully', 'end')
('successfully', 'end', 'social')
('end', 'social', 'issues')
('social', 'issues', 'if')
('issues', 'if', 'they')
('if', 'they', 'become')
('they', 'become', 'adamant')

For sentence 2 , trigrams are: 
('', 'These', 'social')
('These', 'social', 'issues')
('social', 'issues', 'act')
('issues', 'act', 'as')
('act', 'as', 'a')
('as', 'a', 'barrier')
('a', 'barrier', 'to')
('barrier', 'to', 'the')
('to', 'the', 'progress')
('the', 'progress', 'of')
('progress', 'of', 'society')

For sentence 3 , trigrams are: 
('', 'Thus,', 'we')
('Thus,', 'we', 'must')
('we', 'must', 'all')
('must', 'all', 'come')
('all', 'come', 'together')
('come', 'together', 'to')
('together', 'to', 'fight')
('to', 'fight', 'against')
('fight', 'against', 'them')
('against', 'them', 'and')
('them', 'and', 'put')
('and', 'put', 'them')
('put', 'them', 'to')
('them', 'to', 'an')
('to', 'an', 'end')
('an', 'end', 'for')
('end', 'for', 'the')
('for', 'the', 'greater')
('the', 'greater', 'good')

'''
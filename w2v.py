from gensim.models import word2vec
import logging


sg = 0
window_size = 10
vector_size = 250
min_count = 1
workers = 8
epochs = 10
batch_words = 10000

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
train_data = word2vec.LineSentence('law_data/big_law_data.txt')
model = word2vec.Word2Vec(
    train_data,
    min_count=min_count,
    vector_size=vector_size,
    workers=workers,
    epochs=epochs,
    window=window_size,
    sg=sg,
    batch_words=batch_words
)

model.save('models/law_word2vec_CB_new.model')
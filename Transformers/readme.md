The objective of a language model is to predict the next word.
BERT is a language model, while GPT is a Large Language model (LLM)
--------------------------------------------------------------
                   WORD EMBEDDINGS
--------------------------------------------------------------

ML models does not understand text but numbers, so we need to represent texts as numbers. Vectors represent word based on various features asked as part of identifying the word. Math with word hence is possible (e.g., King - Man + Woman = Queen). The features of a word capture the meaning of the word.

Static embeddings like word2vec and GloVe are popular. Static embedding means fixed embeddings for words.

These vectors are created once training is completed on huge amount of text data to understand the relation between words and vectors pop up as a by-product.

Limitations of static embeddings -> same words can have different meanings in a sentence based on its context. (e.g., The train will run on the track. My package is late and I can't track it.)

To summarize, to build a good LLM, a static word embedding is not enough, but contextual embedding (e.g., dish. sweet indian rice dish) 

Mathematically speaking, contextual embedding can be realized by taking static embedding value of 'dish' and adding 'riceness', 'indianness' and 'sweetness' vectors.

-----------------------------------------------------------------------
                    Transformer
------------------------------------------------------------------

Transformer architecture has both encoder and decoder.

words are different from tokens (e.g.,for word 'playing', play -- token 1, ing -- token 2).

Based on the model, the dimension of embedding vector can vary (e.g., BERT has 768 dims, while GPT has 12228 dims). During training, every token in the vocab has static embedding associated.
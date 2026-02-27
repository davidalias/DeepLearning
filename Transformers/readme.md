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

___________________________________________________________________
                Encoder
___________________________________________________________________

When text is given as an input, it is first tokenized with 'CLS' (beginning) and "SEP" (separator) tokens. Token IDs are then generated for these tokens based on the entire vocabulaoty list. Then static embeddings are retrieved for each of the tokens, and also positional embedding is generated based on the order of the words and this embedding is added to the static embedding of each token. The resultant vector will have the knowledge of position of the word.

Word need attention of the surrounding words in order to produce the contextual embedding (e.g., "I made a sweet Indian rice dish called ", here the words 'sweet'(36%), 'Indian'(14%), 'rice'(18%) are attending to the word 'dish'. These adjectives will enrich the meaning of 'dish', while the other words have less attention score for 'dish'). After identifying the values associated between each word, the concept of 'Query', 'Key' and 'Value' are used to come up with contextual embedding.

DOT PRODUCT INTUITION of A.B -> How much of A is pointing in direction of B. 
Imagince B vector is casting a shadow onto vector A. 
The dot product measures:

- the length of this shadow,
- multiplied by the length of A.

Hence, 
Bigger dot product → vectors point more in the same direction
Zero → vectors are perpendicular
Negative → vectors point in opposite directions
# Development of Unsupervised and Semi-supervised algorithms for protein sequences
A Protein molecule is made from a long chain of twenty amino acids, each linked to its neighbour through a covalent peptide bond. Proteins are also known as polypeptides. Each type of protein has a unique sequence of amino acids. The ﬁnal protein structure ultimately depends on this sequence. It plays role in determining the function of a protein. A protein sequence is a sequence of amino acids and each amino acid is represented as an alphabet. Protein sequence clustering can help in assigning functions to proteins, where proteins in one group can be said to be having similar functions.

Before clustering the protein sequences have to be processed so that they can be represented in mathematical form to aid calculation of distances between pair of sequences. For this protein sequences are represented as n-grams and frequency of each n-gram act as feature to represent a protein sequence as vector. Another method to ﬁnd distance between two protein sequences is to calculate similarity between them. This is accomplished by local and global alignment of sequences and then ﬁnding the alignment scores using substitution matrices. A similarity matrix containing alignment scores is obtained which is used to cluster the sequences.

For clustering, vector representation of proteins and similarity matrix of proteins can be used. After obtaining vectors, K-means clustering and hierarchical clustering is applied to get clusters. When a similarity matrix is available hierarchical and spectral clustering methods are used to get clusters. After cluster and cluster label for each protein is obtained Silhouette scores are used to evaluate the clusters. These clusters can aid in function annotation with proteins in same clusters showing same fucntions.

Sequence Similarity
---

Protein sequences are a sequence of 20 amino acids. These amino acids are represented using english alphabets therefore the sequences can be seen as sequence of alphabets. To ﬁnd similarity between two Protein sequences we have to adopt a distance metric which can help us to know the measure of similarity between a pair of proteins. Any traditional clustering algorithm can ﬁnd clusters once a similarity matrix or a similarity graph is available. For this purpose we can use four types of methods: Alignment-based similarity, Keyword-based similarity, Kernel-based similarity and Model-based similarity. For this project I have tried to ﬁnd similarity using Alignment of proteins and keywords extraction using n-grams.

Alignment-based similarity
---

To measure relatedness between two strings similarity is considered an eﬀective measure rather than measuring distances such edit distance. Edit distance is related to the operations of insertion, deletion and substitutions needed to be carried out in order to transform one string to another. On the contrary, alignment refers to the concept that one string is placed against another with insertion of gaps in strings to make the strings equal in length. Two strings can be aligned against each other using space characters which facilitate that length of both the strings is same . In case of protein sequences after aligning the sequences, BLOSUM and PAM Matrices can be used to calculate the score of alignment of proteins. The matches are accounted for a positive value in the score and gaps (the space characters) are penalized. 

Keyword-based Similarity
---

In this approach a sequence is divided into small fragments. A segment is sequence of n-characters appearing in the sequence, this is called as an n-gram. The n-grams obtained are counted as features and a vector for each sequence is constructed. Each protein sequence has a corresponding vector associated with it. Using the vector similarity can be computed. For this purpose the concept of Term frequency and Inverse Document Frequency has been used. For n-grams the value of n can be changed and consequently the results change. Each n-gram is a feature and value for that feature is used to compute distance between two protein sequences. Typically, the tf-idf weight is composed by two terms: the ﬁrst computes the normalized Term Frequency (TF), athat is the number of times a word appears in a document, divided by the total number of words in that document. The second term is the Inverse Document Frequency (IDF), computed as the logarithm of the number of the documents in the corpus divided by the number of documents where the speciﬁc term appears.



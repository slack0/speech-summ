%run extract_topics.py
%run extract_topics.py
%run extract_topics.py
Wmat
pp.pprint(Wmat)
for _each_doc in Wmat[,:]:
    print _each_doc
for _each_doc in Wmat[:,:]:
    print _each_doc
for _each_doc in Wmat:
    print _each_doc
for _each_doc in Wmat:
    print _each_doc
    print "------------"
for _each_doc in Wmat:
    print _each_doc 
    type(_each_doc)
for _each_doc in Wmat:
    print _each_doc 
    print type(_each_doc)
for _each_doc in Wmat:
    print _each_doc 
    np.argmax(_each_doc)
import numpy as np
for _each_doc in Wmat:
    print _each_doc 
    np.argmax(_each_doc)
for _each_doc in Wmat:
    print _each_doc 
    print np.argmax(_each_doc)
model.components_[0]
len(model.components_[0])
len(model.components_[2])
model.components_[2]
pp.pprint(model.components_[2])
model.components_[2]
print model.components_[2]
for _each_doc in Wmat:
    print _each_doc 
    print np.argmax(_each_doc)
speech_tfs
Wmat.shape
model.components_[1]
len(model.components_[1])
most_repr_topic_vec = model.components_[1]
speech_tfs_doc6 = speech_tfs.todense()
type(speech_tfs_doc6)
speech_tfs_doc6.shape
for matrow in speech_tfs_doc6:
    print matrow
for matrow in speech_tfs_doc6:
    print matrow[0]
for matrow in speech_tfs_doc6[:,:]:
    print matrow
for matrow in speech_tfs_doc6:
    print matrow
for matrow in speech_tfs_doc6:
    cosine_similarity(most_repr_topic_vec,matrow)
for matrow in speech_tfs_doc6:
    print matrow.reshape(1, -1)
for matrow in speech_tfs_doc6:
    cosine_similarity(most_repr_topic_vec,matrow)
most_repr_topic_vec
for matrow in speech_tfs_doc6:
    print np.array(matrow)
for matrow in speech_tfs_doc6:
    cosine_similarity(most_repr_topic_vec,np.array(matrow))
most_repr_topic_vec.shape
most_repr_topic_vec.reshape(2067,1)
most_repr_topic_vec.shape
THE_TOPIC_VECTOR = most_repr_topic_vec.reshape(2067,1)
THE_TOPIC_VECTOR.shape
for matrow in speech_tfs_doc6:
    cosine_similarity(THE_TOPIC_VECTOR,matrow)
matrow.shape
for matrow in speech_tfs_doc6:
    cosine_similarity(matrow,THE_TOPIC_VECTOR)
THE_TOPIC_VECTOR.shape
cosine_similarity(matrow,THE_TOPIC_VECTOR)
cosine_similarity(THE_TOPIC_VECTOR,matrow)
THE_TOPIC_VECTOR.shape
matrow.shape
cosine_similarity(matrow,THE_TOPIC_VECTOR)
THE_TOPIC_VECTOR = most_repr_topic_vec.reshape(1,2067)
cosine_similarity(matrow,THE_TOPIC_VECTOR)
for matrow in speech_tfs_doc6:
    cosine_similarity(matrow,THE_TOPIC_VECTOR)
for matrow in speech_tfs_doc6:
    print cosine_similarity(matrow,THE_TOPIC_VECTOR)
speech_hash.keys()
print doc
speech_hash['20070116.txt']
for topic_index in xrange(num_topics):
        print ""
        pp.pprint("-- Top words in topic:")
        topic_importance = dict(zip(id2word.values(),list(model.components_[topic_index])))
        sorted_topic_imp = sorted(topic_importance.items(), key=operator.itemgetter(1),reverse=True)
        pp.pprint([i[0] for i in sorted_topic_imp[:10]])
Wmat
Wmat
speech_tfs
speech_hash.keys()
sentence_tfidf.fit_transform(speech_hash['20070321.txt'].values())
speech_tfs_doc4 = sentence_tfidf.fit_transform(speech_hash['20070321.txt'].values()).todense()
speech_tfs_doc4
Wmat
%history
%history -f foo.py

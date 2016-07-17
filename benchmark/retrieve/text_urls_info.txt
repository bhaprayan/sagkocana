The Canterbury Corpus (cantrbry.tar.gz)
This collection is the main benchmark for comparing compression methods. The Calgary collection is provided for historic interest, the Large corpus is useful for algorithms that can't "get up to speed" on smaller files, and the other collections may be useful for particular file types.

This collection was developed in 1997 as an improved version of the Calgary corpus. The files were chosen because their results on existing compression algorithms are "typical", and so it is hoped this will also be true for new methods.

The Artificial Corpus (artificl.tar.gz)
This collection contains files for which the compression methods may exhibit pathological or worst-case behaviour--files containing little or no repetition (e.g. random.txt), files containing large amounts of repetition (e.g. alphabet.txt), or very small files (e.g. a.txt).

As such, "average" results for this collection will have little or no relevance, as the data files have been designed to detect outliers. Similarly, times for "trivial" files will be negligible, and should not be reported.

The Large Corpus (large.tar.gz)
This is a collection of relatively large files. While most compression methods can be evaluated satisfactorilly on smaller files, some require very large amounts of data to get good compression, and some are so fast that the larger size makes speed measurement more reliable. New files can be added to this collection.

The Miscellaneous Corpus (misc.tar.gz)
This is a collection of "miscellaneous" files that is designed to be added to by researchers and others wishing to publish compression results using their own files.

The Calgary Corpus (calgary.tar.gz)
This was developed in the late 1980s, and during the 1990s became something of a de facto standard for lossless compression evaluation. The collection is now rather dated, but it is still reasonably reliable as a performance indicator. It is still available so that older results can be compared. The collection will not be changed, although there are four files (paper3, paper4, paper5 and paper6) that have been used in some evaluations but are no longer in the corpus because they don't add to the evaluation.

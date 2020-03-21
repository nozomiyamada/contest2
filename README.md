# contest2

- kenLM 5-gram model
- use gigaword nyt 2004, 2005, 2006
- alternate verb forms
- alternate singular/plural noun
- alternate preposition
- alternate article
- score difference threshold (original <> new candidate)

# benchmark (dev set)

|threshold|Precision|Recall|F0.5|
|:-:|:-:|:-:|:-:|
|0|0.0624|0.1484|0.0706|
|0.5|0.0667|0.1223|0.0733|
|1|0.0700|0.0959|0.0740|

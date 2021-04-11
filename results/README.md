these .gv files can be used seperately independent of the python codes(that has been used to generate these in first place) in clubAnalyser.py
e.g you have this file called *sample.gv* 
```
digraph {
	paper_1 [color="#A44F87" penwidth=2]
	paper_2 [color="#A44F87" penwidth=2]
	paper_3 [color="#A44F87" penwidth=2]
	paper_4 [color="#A44F87" penwidth=2]
	subgraph cit {
		paper_1 -> paper_2
		paper_3 -> paper_2
		paper_3 -> paper_3
		paper_4 -> paper_1
		paper_4 -> paper_2
	}
}
```
based on you OS, install graphviz from their official website.
then compile this file like this,
```
$ <engine> -Tpng sample.gv > sample.png
```
where <engine> could be 'dot', 'circo', 'neato' etc. 
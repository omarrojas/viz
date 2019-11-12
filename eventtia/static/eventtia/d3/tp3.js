var promiseWrapper = (d) => new Promise(resolve => d3.csv(d, (p) => resolve(p)))
	
    Promise.all([promiseWrapper("static/eventtia/d3/nodelist.csv"),promiseWrapper("static/eventtia/d3/edgelist.csv")]).then(resolve => {
        createAdjacencyMatrix(resolve[0],resolve[1])    
     })
	//console.log(Promise.all([promiseWrapper("static/eventtia/d3/nodelist.csv"),promiseWrapper("static/eventtia/d3/edgelist.csv")]))
	
    function createAdjacencyMatrix(nodes,edges){
		
		var width = 400
		var height = 400
		var widthSquare=35
		var widthSquareDiv2=17.5
		
		
		var edgeHash = {};
		edges.forEach(edge =>{
			var id = edge.source + "-" + edge.target
			edgeHash[id] = edge
		})
		console.log(edgeHash)		
		var matrix = []
		let i=1;
		nodes.forEach((source, a) => {		
			if(source.role =="evento"){				
				let j=1;
				nodes.forEach((target, b) => {
					if(target.role =="participante"){						
						var grid = {id: source.id + "-" + target.id, x: j, y: i, weight: 0};
						j++;						
						if(edgeHash[grid.id]){
							grid.weight = edgeHash[grid.id].weight;							
						}						
						matrix.push(grid)
					}				
				})
				i++;
			}
			
		})
		
		console.log(matrix)
		

	var svg = d3.select("svg")

	d3.select("svg").append("g")
		.attr("transform","translate(15,15)")
		.attr("id","adjacencyG")
		.selectAll("rect")
		.data(matrix)
		.enter()
		.append("rect")
		.attr("class","grid")
		.attr("width",widthSquare)
		.attr("height",widthSquare)
		.attr("x", d=> d.x*widthSquare)
		.attr("y", d=> d.y*widthSquare)
		.style("fill-opacity", d=> d.weight * .2)//*/
		
	d3.select("svg")
		.append("g")
		.attr("transform","translate(50,45)")
		.selectAll("text")
		.data(nodeParticipantes(nodes))
		.enter()
		.append("text")
		.attr("x", (d,i) => i * widthSquare + widthSquareDiv2)
		.text(d => d.id)
		.style("text-anchor","middle")
		.style("font-size","10px")//*/
		
	d3.select("svg")
		.append("g").attr("transform","translate(45,50)")
		.selectAll("text")
		.data(nodeEventos(nodes))
		.enter()
		.append("text")
		.attr("y",(d,i) => i * widthSquare + widthSquareDiv2)
		.text(d => d.id)
		.style("text-anchor","end")
		.style("font-size","10px")

	
	d3.selectAll("rect.grid").on("mouseover", gridOver); 
	
	function nodeEventos(nodes){
			return nodes.filter(function (d){ 
				return d.role =="evento";				
			})
	}
	
	function nodeParticipantes(nodes){
			return nodes.filter(function (d){ 
				return d.role =="participante";				
			})
	}
	
	function gridOver(d) {
		d3.selectAll("rect").style("stroke-width", function(p) { return p.x == d.x || p.y == d.y ? "3px" : "1px"});
	};
		
    };


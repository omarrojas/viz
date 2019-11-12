
Promise.all([            
d3.json("static/eventtia/d3/countries.geo.json"),                 
d3.json("static/eventtia/d3/ts3_2.json")
    ]).then(function(data){
    
      showData(data);
    
    });


d3.select("#consola").text("Cargando los datos");

var seleccion = new Set();

var tabla = new Array();


function showData(datasources) {    



        let body = d3.select("#bodyVIZ");
    
        console.log("showData");
        let bodyHeight = 900
        let bodyWidth = 1024

        let mapInfo = datasources[0];
        let dataOrginal = datasources[1];
    
           console.log("dataOrginal",dataOrginal);
       let dataGraficar = dataOrginal;
    
      /*console.log("dataGraficar"+dataGraficar);    
      console.log(JSON.stringify(dataGraficar)); //*/
	  
       
        
        var projection = 
            d3.geoMercator()
                .scale(200)
                .translate([bodyWidth / 2, bodyHeight / 2])


        var path = d3.geoPath()
            .projection(projection);    
			
			 body.selectAll("path").data(mapInfo.features)
            .enter().append("path")
            .attr("d", d => path(d))
            .attr("stroke", "#999")
            .attr("fill", "#eee")

	  
        body.selectAll("circle")
            .data(dataGraficar)
            .enter()
            .append("circle")
            .attr("r", 5)
            .attr("fill", "#0055AA")
            .style("opacity", 0.5)
            .attr("cx", d => projection([+d.longitude, +d.latitude])[0])
            .attr("cy", d => projection([+d.longitude, +d.latitude])[1]);  
    
      let brush = d3.brush();
    
      brush.on("brush", function (a,b) {
            let coords = d3.event.selection
            body.selectAll("circle")
                .style("fill", function(d) {
                    let cx = d3.select(this).attr("cx");
                    let cy = d3.select(this).attr("cy");                    
                    let selected = isSelected(coords, cx, cy)
                    if(selected){                         
                      mostrarTabla(d);                      
                    }
                    return selected ? "red" : "blue"
                })            
        });

        body.append("g")
            .attr("class", "brush")
            .call(brush);
    
    
     d3.select("#limpia").on("click", function (e) { 
           limpiarTabla();
     });
    

    }
  
  function isSelected(coords, x, y) {
        let x0 = coords[0][0],
            x1 = coords[1][0],
            y0 = coords[0][1],
            y1 = coords[1][1];
        
        return x0 <= x && x <= x1 && y0 <= y && y <= y1;
    }
  

  function mostrarTabla(d){
    //console.log("2="+d.NombrePais);
    
    seleccion.add(d.event_id);
    //console.log("seleccion="+seleccion.size);
    
    for (let value of seleccion){
      let agregar = true;
     // console.log(value);
      let object={
        event_id:d.event_id,
        amountAttend:d.amountAttend
      }
      tabla.forEach(function(e){
          console.log(e);
         if(e.event_id==value){
            agregar=false;
         }
      });
      if(agregar){
        tabla.push(object);	
      }
    }
        
    let out = d3.select("#preText")  
    out.text(d3.tsvFormat(tabla.slice(0,60)));
    
    let sumTotal = tabla.reduce(function(sum, d) {
        return sum + d.amountAttend;
    }, 0);     
    
    d3.select("#consola").text("Total cantidades de exportaciones en la tabla = "+sumTotal);
 
  }
  
  function limpiarTabla(){
    console.log("limpio");
    seleccion.clear();
    tabla.splice(0, tabla.length);
    var out = d3.selectAll("#preText")  
    out.text(d3.tsvFormat(tabla.slice(0,60)));
    d3.select("#consola").text("Total cantidades de exportaciones en la tabla = 0");
  
  }  
  
  

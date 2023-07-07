// // function Choropleth(){
// //   //Set up
// //   var w = 1000;
// //   var h = 500;
// //   var margin = {top: 100, right: 20, bottom: 60, left: 50};

// //   var projection = d3.geoMercator()
// //                      .center([145, -37.8])
// //                      .scale(3800)
// //                      .translate([w/2, h/2]);

// //   var path = d3.geoPath()
// //                .projection(projection);
               
// //   var svg = d3.select("#map")
// //                .append("svg")
// //                .attr("width", w + margin.left + margin.right)
// //                .attr("height", h + margin.top + margin.bottom)
// //                .append("g")
// //                .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
// //   var color = d3.scaleQuantize()
// //                 .range(['rgb(237,248,233)','rgb(199,233,192)','rgb(161,217,155)','rgb(116,196,118)','rgb(65,171,93)','rgb(35,139,69)','rgb(0,90,50)']);

// //   d3.json("https://cdn.freecodecamp.org/testable-projects-fcc/data/choropleth_map/for_user_education.json")
// //   .then(function(data) {
    
// //     //Set Up color
// //     color.domain([
// //       d3.min(data, function(d) { return d.bachelorsOrHigher}),
// //       d3.max(data, function(d) { return d.bachelorsOrHigher})
// //     ]);

// //     d3.json("https://cdn.freecodecamp.org/testable-projects-fcc/data/choropleth_map/counties.json")
// //       .then(function(json) { 
// //         //Merge 2 json files
        

        
// //         for (var i = 0; i < data.length; i++){
// //           var datafips = data[i].fips;

// //           var dataBachelorsOrHigher = parseFloat(data[i].bachelorsOrHigher);

// //           for (var j = 0; j< json.objects.counties.geometries.length; j++){
// //             var jsonid = json.objects.counties.geometries[j].id || "";

// //             if (datafips == jsonid) {
// //                json.objects.counties.geometries[j].higherEduPercent =  dataBachelorsOrHigher;

// //                break;

// //             }
// //           }
// //         }
// //         console.log("json", json.objects.counties.geometries);
// //         const title = d3.select("#title")
// //                         .append("text")
// //                         .text("United States Educational Attainment")
// //                         .attr("id", "title")
// //                         .attr("left", "20px")
// //                         .attr("font-size", "450");

// //         const subtitle = d3.select("#description")
// //                            .append("text")
// //                            .text("Percentage of adults age 25 and older with a bachelor's degree or higher (2010-2014)")
// //                            .attr("id","description");
// \
// //         console.log("geometries", json.objects.counties.geometries);

// //         //Bind data 
// //         svg.selectAll("path")
// //            .data(json.objects.counties.geometries)
// //            .enter()
// //            .append("path")
// //            .attr("d", path)
// //           //  .style("fill", function(d) {
// //           //   var value = d.higherEduPercent;
// //           //   if (value) {
// //           //     return color(value);

// //           //   } else {
// //           //     return"#ccc";
// //           //   }
// //           //  })


// //       });

// //   });

// // }

// // function main(){
// //   Choropleth();
// // }

// // window.onload = function() {
// //   main();
// // };

function Choropleth() {
  var w = 500;
  var h = 300;
  var projection = d3.geoMercator()
    .center([145,-36.5])
    .translate([w/2 , h/2])
    .scale(2450);

  var path = d3.geoPath()
    .projection(projection);

  var svg = d3.select("#map")
    .append("svg")
    .attr("width", w)
    .attr("height", h);

  d3.json("https://cdn.freecodecamp.org/testable-projects-fcc/data/choropleth_map/counties.json").then(function(data) {
    if (data) {
      svg.selectAll("path")
        .data(data.objects.counties.geometries)
        .enter()
        .append("path")
        .attr("d", path)
        .attr("fill", "grey");
      console.log(data.objects.counties.geometries);
    } else {
      console.error("Data is null or undefined.");
    }
  });
}

function main() {
  Choropleth();
}

window.onload = function() {
  main();
}

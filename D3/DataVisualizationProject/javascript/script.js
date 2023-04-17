function BarChart() {
  var title = d3.select("h1")
              .append("text")
              .text("United State GDP");

    d3.json("https://raw.githubusercontent.com/freeCodeCamp/ProjectReferenceData/master/GDP-data.json")
      .then((data) => {
        var data = data.data;
        
        var dataset = data.map((d) => {
            var date = d[0].split("-");
            var year = date[0];
            var month = date[1];
             var quarter;
        switch(month){
            case "01":
                quarter = "Q1"
                break;
            case "04":
                quarter = "Q2"
                break;
            case "07":
                quarter = "Q3"
                break;
            case "10":
                quarter = "Q4"

        }
            return { 
              date: new Date(year, month-1, date[2]), 
              gdp: d[1],
              year: year,
              quarter:quarter
              
            };
          });

        var w = 900;
        var h = 400;
        var barPadding = 0.5;
        var margin = {top: 100, right: 20, bottom: 60, left: 50};

        var svg = d3.select("#chart1")
          .append('svg')
          .attr("width", w + margin.left + margin.right)
          .attr("height", h + margin.top + margin.bottom)
          .append("g")
          .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
  
        var xScale = d3.scaleTime()
          .domain([d3.min(dataset, (d) => d.date), d3.max(dataset, (d) => d.date)])
          .range([0, w-100]);
  
        var yScale = d3.scaleLinear()
          .domain([0, d3.max(dataset, (d) => d.gdp)])
          .range([h, 0]);
  
        //Create xAxis
        var xAxis = d3.axisBottom()
          .ticks(10)
          .scale(xScale);
  
        //Create yAxis
        var yAxis = d3.axisLeft()
          .ticks(10)
          .scale(yScale);
  
        //Draw bar Chart
        svg.selectAll("rect")
          .data(dataset)
          .enter()
          .append("rect")
          .attr("class", "bar")
          .attr("x", (d) => xScale(d.date))
          .attr("y", (d) => yScale(d.gdp))
          .attr("width", w / dataset.length - barPadding)
          .attr("height", (d) => h - yScale(d.gdp))
          .attr("fill", "#03c6fc")
          .on("mouseover", function( event, d) {
            //change color
            d3.select(this)
               .style("fill", "orange");

      
            //Add tooltip

var tooltip = d3.select("#tooltip");

          tooltip.style("visibility", "visible")
                 .html(d.year + " " + d.quarter + "<br>" + "$" + d.gdp + " Billion")
                 .classed("visible", true) // add the "visible" class to the tooltip
                 .style("left", (event.pageX - 175) + "px")
                 .style("top", 450 + "px");

      
 
              })
          
          .on("mouseout", function () {
            d3.select(this)
            .style("fill", "#03c6fc");
          var tooltip = d3.select("#tooltip");
          tooltip.style("visibility", "hidden")
            .classed("visible", false); 
          });
          

        
        //Draw xAxis
        svg.append("g")
          .attr("id", "x_axis")
          .attr("transform", "translate(0, " + (h - barPadding) + ")")
          .call(xAxis);
  
        //Draw yAxis
        svg.append("g")
          .attr("id", "y_axis")
          .attr("transform", "translate(" + (barPadding) + ",0)")
          .call(yAxis);
  
        //GDP label
        svg.append("text")
          .attr("text-anchor", "middle")
          .attr("transform", "rotate(-90) translate(-" + (h / 2 - 50) + ", 20)")
          .text("Gross Domestic Product");
  
      });
  }
  
  function main() {
    BarChart();
  }
  
  window.onload = function () {
    main();
  };
  
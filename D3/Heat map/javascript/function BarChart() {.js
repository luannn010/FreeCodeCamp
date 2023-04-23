function BarChart() {
  var title = d3.select("h1")
              .append("text")
              .text("United State GDP");

    d3.json("https://raw.githubusercontent.com/freeCodeCamp/ProjectReferenceData/master/GDP-data.json")
      .then((data) => {
        var activeArea = null;
        
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
            // Update date format in dataset creation
        return { 
          date: new Date(year, month-1, 1),  // always set day to 1
          gdp: d[1],
          year: year,
          quarter: quarter
        };

          })
          ;

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
          .range([0, w - 100]);
          
          
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
          .attr("data-date", (d) => { return d3.timeFormat("%Y-%m-%d")(d.date); })
          .attr("data-gdp", (d) => {  return d.gdp ;})
          .attr("width", w / dataset.length - barPadding)
          .attr("height", (d) => h - yScale(d.gdp))
          .attr("fill", "#03c6fc")
          .on("mouseover", function(event, d) {
            // Set active area
            activeArea = d3.select(this);
          
            // Change color
            activeArea.style("fill", "orange");
            var date = activeArea.attr('data-date'); // e.g. 'Tue Jul 01 1986 00:00:00 GMT+1000 (AEDT)'
            var formattedDate = d3.timeFormat('%Y-%m-%d')(new Date(date)); // e.g. '1986-07-01'
            // Add tooltip
            var tooltip = d3.select("#tooltip");
          
            tooltip.style("visibility", "visible")
              .html(d.year + " " + d.quarter + "<br>" + "$" + d.gdp + " Billion")
              .classed("visible", true) // add the "visible" class to the tooltip
              .style("left", (event.pageX - 175) + "px")
              .style("top", 450 + "px")
              .attr('data-date', formattedDate); // set "data-date" attribute of tooltip
          })
                    
          .on("mouseout", function() {
            // Clear active area
            activeArea = null;
          
            // Change color
            d3.select(this).style("fill", "#03c6fc");
          
            var tooltip = d3.select("#tooltip");
            tooltip.style("visibility", "hidden")
              .classed("visible", false)
              .attr("data-date", ""); // clear "data-date" attribute of tooltip
          });
                    

        
        //Draw xAxis
        svg.append("g")
          .attr("id", "x-axis")
          .attr("transform", "translate(0, " + (h - barPadding) + ")")
          .call(xAxis);
  
        //Draw yAxis
        svg.append("g")
          .attr("id", "y-axis")
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
  
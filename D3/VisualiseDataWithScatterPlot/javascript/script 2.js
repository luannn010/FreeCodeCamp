// Set the margin and dimensions of the chart
var margin = { top: 50, right: 50, bottom: 50, left: 100 };
var w = 800 - margin.left - margin.right;
var h = 500 - margin.top - margin.bottom;

function DataScatterPot() {
  d3.json("https://raw.githubusercontent.com/freeCodeCamp/ProjectReferenceData/master/cyclist-data.json")
    .then(function (data) {
      // Process data
      var dataset = data.map(function(d) {

        var parsedTime = d.Time.split(':');
      d.Time = new Date(1970, 0, 1, 0, parsedTime[0], parsedTime[1]);
        return {
          
          Time: d.Time,
          Name: d.Name,
          Year: d.Year,
          Doping: d.Doping,
          Country: d.Nationality
        };
      });

      // Create x and y scales
      var xScale = d3.scaleLinear()
                     .domain([d3.min(dataset, function(d) { return d.Year - 1; }),
                              d3.max(dataset, function(d) { return d.Year + 1; })])
                     .range([0, w]);
      var yScale = d3.scaleTime()
                     .domain([d3.max(dataset, function(d) { return d.Time; }),
                              d3.min(dataset, function(d) { return d.Time; })])
                     .range([h, 0]);
      var timeFormat = d3.timeFormat('%M:%S');
      // Create x and y axes
      var xAxis = d3.axisBottom()
                    .scale(xScale)
                    .tickFormat(d3.format("d"));
      var yAxis = d3.axisLeft()
                    .scale(yScale)
                    .tickFormat(timeFormat);
      


      // Create SVG container
      var svg = d3.select("#chart")
                  .append("svg")
                  .attr("width", w + margin.left + margin.right)
                  .attr("height", h + margin.top + margin.bottom)
                  .append("g")
                  .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

      // Draw Scatter Plot
      svg.selectAll(".dot")
      .data(dataset)
      .enter()
      .append("circle")
      .attr("class", "dot")
      .attr("cx", function(d) { return xScale(d.Year); })
      .attr("cy", function(d) { return yScale(d.Time); })
      .attr("data-xvalue", function (d) { return d.Year; })
      .attr("data-yvalue", function (d) { return d.Time;})

      .attr("r", 5)
      .attr("fill", function(d) { return (d.Doping == "") ? "orange" : "lightblue"; })
      .attr("stroke", "black")
      .attr("stroke-width", 1);


      svg.selectAll("circle")
      .on("mouseover", function(event, d) {
        var tooltip = d3.select("#tooltip");
        tooltip.style("visibility", "visible")
               .attr("id", "tooltip")
               .attr('data-year', d.Year)
               .html(d.Name +": " +d.Country +"<br/>" + 
               "Year: " + d.Year +", Time: " +timeFormat(d.Time)  +
               (d.Doping ? '<br/><br/>' + d.Doping : ''))

               .style("left", (event.pageX + 10) + "px")
               .style("top", (event.pageY - 28) + "px");
        // Change border style
        d3.select(this)
          .style("stroke", "black")
          .style("stroke-width", 2);
      })
      .on("mouseout", function() {
        // Hide tooltip
        var tooltip = d3.select("#tooltip");
        tooltip.style("visibility", "hidden");
        // Revert border style
        d3.select(this)
          .style("stroke", null)
          .style("stroke-width", null);
      });
      


      // Draw X-axis
      svg.append("g")
         .attr("id", "x-axis")
         .attr("transform", "translate(0," + h + ")")
         .call(xAxis);

      // Draw Y-axis
      svg.append("g")
         .attr("id", "y-axis")
         .call(yAxis);
        
      svg.append('text')
         .attr('transform', 'rotate(-90)')
         .attr('x', -160)
         .attr('y', -44)
         .style('font-size', 18)
         .text('Time in Minutes');
      // Legends
      var legend = svg.append("g")
                  .attr("class", "legend")
                  .attr("transform", "translate(" + (w-80) + "," + 20 + ")")
                  .style("font-size", "20px");
      var legendData = [
        { label: " No doping allegations" ,color: "orange"   },
        { label: " Riders with doping alegations ", color: "lightblue"}
      ]
     var legendRect = legend.selectAll("rect")
                            .data(legendData)
                            .enter()
                            .append("rect")
                            .attr("x",70)
                            .attr("y",(d,i) => {
                              return i * 12 + 200;
                            })
                            .attr("width",10)
                            .attr("height",10)
                            .attr("fill", (d,i)=> d.color)
    var legendText = legend.selectAll("#legend")
                            .data(legendData)
                            .enter()
                            .append("text")
                            .attr("x",65)
                            .attr("y", (d, i) => {
                              return i * 12 + 208;
                            })
                            .text(function(d, i) {
                              return d.label;
                            })
                            .attr("font-size", "9px")
                            .attr("text-anchor", "end");
                          
                          
      
    })
}

function main() {
  DataScatterPot();
}

window.onload = function() {
  main();
}

function HeatMap() {
  d3.json("https://raw.githubusercontent.com/freeCodeCamp/ProjectReferenceData/master/global-temperature.json")
  .then((data) => {
    console.log(data); // Output the loaded data to the console
    const baseTemp = data.baseTemperature;
    const dataset = data.monthlyVariance;
    
    // Set up description
    const description = d3.select("#description");
    description.html(d3.min(dataset, function(d){return d.year;}) + " - " + d3.max(dataset, function(d){return d.year;})+": base temperature " + baseTemp +'&#8451;')
               .attr("id","description")
    
    const months = d3.range(12);
    const monthName = months.map(function(d) {
      Name = new Date(2000, d).toLocaleString('default', {month: 'long'});
      return Name;

    });
    
    // Set up svg
    const margin = {top: 10, right: 100, bottom: 100, left: 100};
    const w = 1600 - margin.left - margin.right;
    const h = 800 - margin.top - margin.bottom;

    // Set up Scale 
    const xScale = d3.scaleBand()
                     .domain(dataset.map(function(d){return d.year}))
                     .range([0,w])
                     .paddingInner(0.05);
    const yScale = d3.scaleBand()
                     .domain(monthName)
                     .range([0,h])
                     .paddingInner(0.05);
    // Set up Stack
    const stack = d3.stack()
                    .keys(monthName);
    const series = stack(dataset);
    // Set up Color
    const color = d3.scaleQuantize()
                // get color range from https://colorbrewer2.org/#type=sequential&scheme=YlGnBu&n=5
                    .range(['rgb(215,48,39)','rgb(244,109,67)','rgb(253,174,97)','rgb(254,224,144)','rgb(255,255,191)','rgb(224,243,248)','rgb(171,217,233)','rgb(116,173,209)','rgb(69,117,180)'].reverse());
    color.domain([
      d3.min(dataset, function(d){ return baseTemp + d.variance}),
      d3.max(dataset, function(d){ return baseTemp + d.variance})
    ]);
    console.log(d3.max(dataset, function(d){ return baseTemp + d.variance}))
    // Set up svg
    const svg = d3.select("#chart")
                  .append("svg")
                  .attr("width", w + margin.left + margin.right)
                  .attr("height", h + margin.top + margin.bottom)
                  .append("g")
                  .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
    const groups = svg.selectAll("g")
                    .data(series)
                    .enter()
                    .append("g")
                    .attr("fill", function(d) {
                      return color(baseTemp + d[0][2])
                    });
   
    //Draw cells
    const rects = groups.selectAll("rect")
    .data(function(d) {return d;})
    .enter()
    .append("rect")
    .attr("class", "cell")
    .attr("x", function(d) {
      return xScale(d.data.year);
    })
    .attr("y", function(d) {
      return yScale(monthName[d.data.month - 1]);
    })
    .attr("data-month", function(d) {return d.data.month -1})
    .attr("data-year", function(d) { return d.data.year})
    .attr("data-temp", function(d) { return (baseTemp + d.data.variance)})
    .attr("height", yScale.bandwidth())
    .attr("width", xScale.bandwidth())
    .attr("fill", function(d) {
      return color(baseTemp + d.data.variance)})
    .on("mouseover", function(event, d) {
      const tooltip = d3.select("#tooltip");
      tooltip.style("visibility", "visible")
      .html(d.data.year + " - " +monthName[d.data.month - 1] + 
      "<br>" +  (baseTemp + d.data.variance).toFixed(1) + '&#8451;' + 
      "<br>" + d.data.variance.toFixed(1) + '&#8451;'
      )
      .attr("data-year", d.data.year)
      .style("left", (event.pageX + 10) + "px")
      .style("top", (event.pageY - 28) + "px");
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
      

    //Add Axises
    const xAxis = d3.axisBottom(xScale)
    .tickValues(xScale.domain().filter(function (year) {
        return year % 10 === 0;
      })
    )
    .tickSize(10, 1);

    svg.append("text")
    .attr("x", w/2)
    .attr("y", h + margin.top + 50)
    .attr("text-anchor", "middle")
    .text("Year");
 
    
    svg.append("g")
    .attr("id", "x-axis")
    .attr("transform", "translate(0," + h + ")")
    .call(xAxis);


    const yAxis = d3.axisLeft(yScale);
    svg.append("g")
    .attr("id", "y-axis")
    .call(yAxis);
    
    svg.append("text")
   .attr("transform", "rotate(-90)")
   .attr("x", -h/2)
   .attr("y", -margin.left + 20)
   .attr("text-anchor", "middle")
   .text("Month");
    
    // Add legend

    const legendColors = color.range();
    var legendWidth = 400;
    var legendHeight = 300 / legendColors.length;

    var variance = data.monthlyVariance.map(function (val) {
      return val.variance;
    });
    var minTemp = data.baseTemperature + Math.min.apply(null, variance);
    var maxTemp = data.baseTemperature + Math.max.apply(null, variance);

    var legendThreshold = d3
      .scaleThreshold()
      .domain(
        (function (min, max, count) {
          var array = [];
          var step = (max - min) / count;
          var base = min;
          for (var i = 1; i < count; i++) {
            array.push(base + i * step);
          }
          return array;
        })(minTemp, maxTemp, legendColors.length)
      )
      .range(legendColors);

    var x = d3
      .scaleLinear()
      .domain([minTemp, maxTemp])
      .range([0, legendWidth]);

    var legendXAxis = d3
      .axisBottom()
      .scale(x)
      .tickSize(10, 0)
      .tickValues(legendThreshold.domain())
      .tickFormat(d3.format('.1f'));

    var legend = svg
      .append('g')
      .classed('legend', true)
      .attr('id', 'legend')
      .attr(
        'transform',
        'translate(' +
          margin.left +
          ',' +
          (margin.top + h + margin.bottom - 2 * legendHeight) +
          ')'
      );

  legend
    .append('g')
    .selectAll('rect')
    .data(
      legendThreshold.range().map(function (color) {
        var d = legendThreshold.invertExtent(color);
        if (d[0] === null) {
          d[0] = x.domain()[0];
        }
        if (d[1] === null) {
          d[1] = x.domain()[1];
        }
        return d;
      })
    )
    .enter()
    .append('rect')
    .style('fill', function (d) {
      return legendThreshold(d[0]);
    })
    .attr('x', d => x(d[0]))
    .attr('y', 0)
    .attr('width', d =>
      d[0] && d[1] ? x(d[1]) - x(d[0]) : x(null)
    )
    .attr('height', legendHeight);

  legend
    .append('g')
    .attr('transform', 'translate(' + 0 + ',' + legendHeight + ')')
    .call(legendXAxis);

    })
}

function main(){
  HeatMap();
}

window.onload = function() {
  main();
}

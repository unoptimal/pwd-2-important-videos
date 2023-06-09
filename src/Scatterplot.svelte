<script>
  import { onMount } from "svelte";
  import * as d3 from 'd3';
  import Axis from './Axis.svelte';
  
  export let data;
  let filteredData = [];
  let minValue = 0;
  let maxValue = 2000000000;
  let tooltipData = null;

  const margin = { top: 20, right: 20, bottom: 40, left: 140 };
  const width = 900;
  const height = 600;
  const innerHeight = height - margin.top - margin.bottom;
  const innerWidth = width - margin.left - margin.right;

  let xScale, yScale;

  const updateFilteredData = () => {
    filteredData = Object.values(data).filter(d => +d.view_count > minValue && +d.view_count < maxValue);
  }

  $: updateFilteredData();
  
  $: {
    xScale = d3.scaleBand()
      .domain([0, filteredData.length + 1]) 
      .range([0, innerWidth]);
  
    yScale = d3.scaleLinear()
      .domain([0, d3.max(filteredData, d => +d.view_count)])
      .range([innerHeight, 0]);
  }

  const xAxis = d3.axisBottom(xScale);
  const yAxis = d3.axisLeft(yScale);
  
  let svgEl;

  onMount(() => {
    d3.select(svgEl).append("g")
      .attr("class", "x-axis")
      .attr("transform", `translate(${margin.left}, ${innerHeight + margin.top})`)
      .call(xAxis);
      
    d3.select(svgEl).append("g")
      .attr("class", "y-axis")
      .attr("transform", `translate(${margin.left}, ${margin.top})`)
      .call(yAxis);
  });
  
  const handleFilterChange = () => {

    updateFilteredData();
    xScale.domain([0, filteredData.length + 1]);
    yScale.domain([0, d3.max(filteredData, d => +d.view_count)]);
    d3.select(".x-axis").transition().duration(500).call(xAxis);
    d3.select(".y-axis").transition().duration(500).call(yAxis);
  }

  const handleCircleMouseover = (event, data) => {
    tooltipData = data;
  }

  const handleCircleMouseout = (event, data) => {
    tooltipData = null;
  }

</script>


<p>And here's an interactive, if not very messy, broken, and suboptimal scatterplot of the videos in the playlist. You can hover over the points for more information.</p>


<div class='controls'>
  <label for="minValue">Min Value:</label>
  <input type="number" id="minValue" bind:value={minValue} on:input={handleFilterChange} style="margin-right: 10px;">
  <label for="maxValue">Max Value:</label>
  <input type="number" id="maxValue" bind:value={maxValue} on:input={handleFilterChange}>
</div>

<p>Showing {filteredData.length} out of {Object.values(data).length} results</p>

{#if tooltipData}
  <div class="tooltip">
    <p>{tooltipData.title}</p>
    <p>{parseInt(tooltipData.view_count).toLocaleString()} views</p>
  </div>
{/if}

<svg {width} {height} bind:this={svgEl} style="marginTop: {margin.top}px">
  <g transform={`translate(${margin.left},${margin.top})`}>

    <Axis {innerHeight} {margin} scale={xScale} position="bottom" />
    <text transform={`translate(${innerWidth/2},${innerHeight + 20} )`}>Playlist Position</text>

    <Axis {innerHeight} {margin} scale={yScale} position="left" />
    <text transform={`translate(${-80},${innerHeight / 2}) rotate(-90)`}>View Count (millions)</text>

      {#each filteredData as data, i}
      <a href={`https://www.youtube.com/watch?v=${data.video_id}&list=PLFsQleAWXsj_4yDeebiIADdH5FMayBiJo`} target="_blank">
        <circle
          cx={(i + 0.5) * (innerWidth / filteredData.length)}
          cy={yScale(data.view_count) - margin.top}
          r="5"
          title={`Title: ${data.title}, Views: ${data.view_count}`}
          on:mouseover={(event) => handleCircleMouseover(event, data)}
          on:mouseout={(event) => handleCircleMouseout(event, data)}
        />
      </a>
      {/each}

  </g>
</svg>



<style>
.tooltip {
  position: absolute;
  top: 120%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: white;
  border: 1px solid gray;
  padding: 10px;
}

.controls, p{
  display: flex;
  justify-content: center;
  align-items: center;
}

</style>
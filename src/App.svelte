<script>
	import Scatterplot from "./Scatterplot.svelte";
	import data from "../public/data.json";
  </script>

<div class='intro'>
	<h1>Playing with Data #2: important videos</h1>
	<p id='byline'><i>by <a href='http://unoptimal.com/'>unoptimal</a></i></p>
	<p>Paying homage to the legendary <a href="https://www.youtube.com/playlist?list=PLFsQleAWXsj_4yDeebiIADdH5FMayBiJo">important videos playlist</a>.</p>
	<p>The data only contains 309 (out of 312) total entries because the API couldn't get  data from 3 videos.</p>
	<p>Note: not mobile friendly, and things are broken. It's fine.</p>
	<p><i>Source data can be found <a href="https://github.com/unoptimal/pwd-2-important-videos/blob/master/public/data.json">here</a>, and source code <a href='https://github.com/unoptimal/pwd-2-important-videos'>here</a>,</i></p>
	
	<div class="chart">
		<Scatterplot {data} />
	</div>

</div>

<style>
	.intro {
		display: flex;
		justify-content: center;
		align-items: center;
		flex-direction: column;
		margin: 0 auto;
	}
	#byline{
		text-align:center;
	}
</style>
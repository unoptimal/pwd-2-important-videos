<script>
	import Scatterplot from "./Scatterplot.svelte";
	import data from "../public/data.json";
  </script>

<div>
	<h1>Playing with Data #2: important videos</h1>
	<p><i>Source data (scraped with the <a href="https://developers.google.com/youtube/v3/getting-started">YouTube API</a> and a custom <a href="https://github.com/unoptimal/pwd-2-important-videos/blob/master/clean_data.py">Python script</a>) can be found <a href="https://github.com/unoptimal/pwd-2-important-videos/blob/master/public/data.json">here</a>, and source code <a href='https://github.com/unoptimal/pwd-2-important-videos'>here</a>,</i></p>
	<p><i>by <a href='http://unoptimal.com/'>unoptimal</a></i></p>

	<p>Paying homage to the all-time <a href="https://www.youtube.com/playlist?list=PLFsQleAWXsj_4yDeebiIADdH5FMayBiJo">important videos playlist</a></p>
	<p>The data only contains 309 total entries, since I couldn't get the data from 3 of the videos.</p>
	<Scatterplot {data} />

</div>

  
<script>
	import Scatterplot from "./Scatterplot.svelte";
	import Stats from "./Stats.svelte";
	import data from "../public/data.json";
  </script>

<div class='intro'>
	<h1>Playing with Data #2: important videos</h1>
	<p style="text-align:center;"><i>by <a href='http://unoptimal.com/'>unoptimal</a></i></p>
	<p><i>Source data can be found <a href="https://github.com/unoptimal/pwd-2-important-videos/blob/master/public/data.json">here</a>, and source code <a href='https://github.com/unoptimal/pwd-2-important-videos'>here</a>.</i></p>
	
	<p>The 
		<a href="https://www.youtube.com/playlist?list=PLFsQleAWXsj_4yDeebiIADdH5FMayBiJo">important videos playlist</a>
		is an iconic part of YouTube's history.
		The playlist, containing 312 short and humorous meme clips, was originally created by YouTube user eljito in 2015. After it was taken down by Youtube, it has since been recreated by user kierancaspian (however, the new playlist only contains 310 of the original 312 videos).
		Two personal favorites of mine are <a href='https://www.youtube.com/watch?v=CIdXPIN3j38&list=PLFsQleAWXsj_4yDeebiIADdH5FMayBiJo&index=49'>"Nicholas Cage Driving"</a> and "<a href='https://www.youtube.com/watch?v=LZgeIReY04c&list=PLFsQleAWXsj_4yDeebiIADdH5FMayBiJo&index=105'>Never Illegally Download"</a>.
	</p>
	<p>Anyways, I thought it'd be fun to investigate the data behind the videos. Here are some things I found (as of March 28, 2023):</p>
	<p>Note: I couldn't scrape data from three of the videos because they've been privated. Also, this is not mobile friendly at all.</p>


	<div class="chart">
		<Stats {data}/>
		<Scatterplot {data} />
	</div>

</div>
